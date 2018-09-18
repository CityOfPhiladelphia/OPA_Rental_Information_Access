from li_dbs import GISLNI
from config import GATEKEEPERKEY
import requests


def query(opa_account_num):
    with GISLNI.GISLNI() as con:
        cursor = con.cursor() 
        sql = f"SELECT * FROM rental_payments_opa_mvw WHERE opaaccountnumber LIKE '{opa_account_num}'"
        cursor.execute(sql)
        licenses = cursor.fetchall()
        cursor.close()
    return licenses

def get_opa_num_from_ais(address):
    r = requests.get(f'https://api.phila.gov/ais/v1/search/{address}?gatekeeperKey={GATEKEEPERKEY}').json()
    opa_account_num = r['features'][0]['properties']['opa_account_num']
    return opa_account_num

def get_licenses(address):
    opa_account_num = get_opa_num_from_ais(address)
    licenses = query(opa_account_num)
    return licenses

if __name__ == '__main__':
    licenses = get_licenses('7151 GERMANTOWN AVE')
    print(licenses)