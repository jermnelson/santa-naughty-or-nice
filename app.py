# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 09:47:05 2015

@author: Jeremy Nelson
"""
__author__ = "Jeremy Nelson"

import redis
from flask import Flask, render_template

app = Flask(__name__)
datastore = redis.StrictRedis()

@app.route("/")
def index():
    return render_template("index.html", ds=datastore)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=20153,
            debug=True)
