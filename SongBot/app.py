from flask import Flask, render_template, request, url_for, redirect, session,flash
import pymongo
import bcrypt
from pymongo import MongoClient, ssl_support
#set app as a Flask instance 
app = Flask(__name__)
#encryption relies on secret keys so they could be run
#app.secret_key = "testing"
#connoct to your Mongo DB database
#mongo = MongoClient("mongodb+srv://manasvi:man14@queenman.rrrho.mongodb.net/test", ssl_cert_reqs=ssl_support.CERT_NONE)

#get the database name
#db = mongo.get_database('reg_records')
#get the particular collection that contains the data
#records = db.register
#test = mongo.get_database('prod_details')
#details = test.prod_details

#assign URLs to have a particular route
@app.route('/') 
@app.route('/dashboard', methods=['POST'])
def dashboard():
    
        return render_template('dashboard.html')
    # except Exception as e:
    #     return dumps({'error' : str(e)})



if __name__ == "__main__":
 
  app.run(host='0.0.0.0',debug=True)
