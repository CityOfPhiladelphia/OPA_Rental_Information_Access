import requests
from config import GATEKEEPERKEY
from db import get_db
from sqlalchemy import text

def get_eclipse_location_id_from_ais(address):
    r = requests.get(f'https://api.phila.gov/ais/v1/search/{address}?gatekeeperKey={GATEKEEPERKEY}').json()
    try:
        eclipse_location_id = r['features'][0]['properties']['eclipse_location_id']
        return eclipse_location_id
    except:
        return None

def query(eclipse_location_id):
    db = get_db()
    sql = f"SELECT * FROM rental_payments_opa_mvw WHERE eclipse_addressobjectid LIKE '{eclipse_location_id}'"
    licenses = db.engine.execute(text(sql)).fetchall()
    return licenses

def get_licenses(address):
    eclipse_location_id = get_eclipse_location_id_from_ais(address)
    if eclipse_location_id is None:
        return None
    licenses = query(eclipse_location_id)
    return licenses