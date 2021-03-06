from flask import Flask, request, g, flash, render_template
from config import SECRET_KEY
from db import close_db
from auth import requires_auth
from data_processing import get_licenses
from gevent.pywsgi import WSGIServer


app = Flask(__name__)
# Close the database when the app shuts down
app.teardown_appcontext(close_db)
app.secret_key = SECRET_KEY

# Send all routes to the search page (it's the only page in this application)
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>')
@requires_auth
def address(path):
    if request.method == 'POST':
        
        error = None
        address = request.form.get('addressform')

        # Flash a message when AIS breaks
        try:
            licenses = get_licenses(address)
        except:
            error = 'An error has occurred. Either AIS is down or this application has encountered a bug. Please try again later or contact LIGISTeam through the link in the footer of this page.'
            flash(error)
            return render_template('address.html')

        if licenses is None:
            error = 'Please enter a valid address.'
            flash(error)
            return render_template('address.html')

        elif len(licenses) == 0:
            error = 'No results found for that address.'
            flash(error)
            return render_template('address.html') 
        
        return render_template('address.html', licenses=licenses)
    
    return render_template('address.html')
    

if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 8100), app)
    http_server.serve_forever()