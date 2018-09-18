from flask import Flask, jsonify, flash, render_template
from auth import requires_auth
from getlicenses import get_licenses


app = Flask(__name__)

@app.route('/address/<address>', methods=['GET'])
@requires_auth
def address(address):
    error = None
    licenses = get_licenses(address)

    if licenses is None:
        error = 'Please enter a valid address.'
        flash(error) 
        
    return render_template('address.html', licenses=licenses)

if __name__ == '__main__':
    app.run(debug=True)