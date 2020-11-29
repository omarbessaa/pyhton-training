#-*-coding:utf-8 -*-
''' build an api with flask
'''

#import the flask library
from flask import Flask #, jsonify

#inalisation of the app
app = Flask(__name__)

#now we will start routing the app
@app.route('/' , methods = ['GET'])
def welcome() :
    return 'Hello you '

#now we have to run the service
app.run(debug = True)
