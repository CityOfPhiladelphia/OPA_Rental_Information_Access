# OPA_Rental_Information_Access
A lightweight Flask application to validate paid rental license fees.

## Installation
- Set environment variables as shown below.
- Get the config.py file.
- Change to the project directory and execute flask run in a command prompt/bash.

## TODO
- Update etl/etl.py to bring in LI_ADDRESS_KEY then update getdata.py to query based on that. Currently the query is based around OPA_ACCOUNT_NUMBER and some instances of OPA_ACCOUNT_NUMBER in ECLIPSE do not seem to match up with what is spit back from AIS
- Make requirements.txt file
- Set scheduled etl process on a VM
- Make a front end
  - Make the front end responsive
- Make all routes other than "/address" reroute to "/address"

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
|   base.html
app.py
auth.py
data_processing.py
db.py
```
## Environment Variables
| Variable     | Value                       | Description                                      |
| ------------ | --------------------------- | ------------------------------------------------ |
| FLASK_APP    | app.py                      | Where the app lives                              |
| FLASK_ENV    | development                 | Tells Flask to start app in development mode     |
| FLASK_DEBUG  | 1                           | Activate Flask's debugger                        |
