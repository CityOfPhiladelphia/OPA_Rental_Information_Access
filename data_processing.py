import requests
from config import GATEKEEPERKEY
from db import get_db
from sqlalchemy import text

def get_opa_num_from_ais(address):
    r = requests.get(f'https://api.phila.gov/ais/v1/search/{address}?gatekeeperKey={GATEKEEPERKEY}').json()
    try:
        opa_account_num = r['features'][0]['properties']['opa_account_num']
        return opa_account_num
    except:
        return None

def query(opa_account_num):
    db = get_db()
    sql = f"SELECT * FROM rental_payments_opa_mvw WHERE opaaccountnumber LIKE '{opa_account_num}'"
    licenses = db.engine.execute(text(sql)).fetchall()
    return licenses

def get_licenses(address):
    if address is None:
        return None
    opa_account_num = get_opa_num_from_ais(address)
    licenses = query(opa_account_num)
    return licenses

if __name__ == '__main__':
    licenses = get_licenses('7151 GERMANTOWN AVE')
    print(licenses)