# OPA_Rental_Information_Access
A lightweight Flask application to validate paid rental license fees.

![OPA_RENTAL](https://github.com/CityOfPhiladelphia/OPA_Rental_Information_Access/blob/master/OPA_RENTAL.PNG)

## Project Outline
- OPA requested an application in which they can enter an address and see the following:
  - associated rental licenses
  - if the address is owner occupied 
  - how many units the property has
  - license fees paid  per rental license
- To create a view of rental license fees, data from various tables in ECLIPSE is pulled. Due to long query times in ECLIPSE, data is extracted from ECLIPSE, transformed into a useful format, and then loaded into a table called "rental_payments_opa_mvw" in GISLNI. This materialized view will be refreshed nightly, allowing for fast query times while using the application.
- This Flask application allows the user to enter an address which is then passed through AIS. AIS allows the address to be standardized and matched to data in "rental_payments_opa_mvw". This data is then queried and served to the client in the form of a table.

To answer the question "why wasn't this an API" - the OPA wanted something with a UI.

## Installation
- git clone https://github.com/CityOfPhiladelphia/OPA_Rental_Information_Access
- cd to OPA_Rental_Information_Access
- Install requirements via pip install -r requirements.txt
- Set environment variables as shown below.
- Get the config.py file.
- Start the application by typing "flask run" in a command prompt/bash.

## File structure
```
etl
|___SQL
|   |   OPARentalAPI_ECLIPSE.sql
|   etl.py
|   sql_queries.py
static
|   styles.css
templates
|   address.html
app.py
auth.py
data_processing.py
db.py
```
## Environment Variables
| Variable     | Value                       | Description                                      |
| ------------ | --------------------------- | ------------------------------------------------ |
| FLASK_APP    | app.py                      | Where the app lives                              |
