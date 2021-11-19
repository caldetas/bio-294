#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:52:37 2021

@author: hannes
"""

from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import pandas as pd
import time
from datetime import datetime

#create a class for permanent storage of values
class data:
    def __init__(self):
            self.df = {}
            self.settings = {}

#initiate class
data = data() 

#create app
app = Flask(__name__)

#define landing page
@app.route('/', methods=["POST", "GET"])
def home():
    #here you can do something before rendering
    title = 'grayscale'
    return render_template('index.html', bigtitle=title)

#run the app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
