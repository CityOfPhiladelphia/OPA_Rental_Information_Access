from flask import Flask, request, g, flash, render_template
from config import SECRET_KEY
from db import close_db
from auth import requires_auth
from data_processing import get_licenses


app = Flask(__name__)
# Close the database when the app shuts down
app.teardown_appcontext(close_db)
app.secret_key = SECRET_KEY

@app.route('/address', methods=['GET', 'POST'])
@requires_auth
def address():
    if request.method == 'POST':
        
        error = None
        address = request.form.get('addressform')
        licenses = get_licenses(address)

        if licenses is None:
            error = 'No results found for that address.'
            flash(error)
            return render_template('address.html') 
        
        return render_template('address.html', licenses=licenses)
    
    return render_template('address.html')
    

if __name__ == '__main__':
    app.run(debug=True)