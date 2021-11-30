#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:52:37 2021

@author: hannes
"""

from flask import Flask, redirect, url_for, render_template, request, session, flash, json
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
    title = 'GENOMEBROWSER'
    return render_template('index.html', bigtitle=title)


#function to get the genes present in folder
def get_all_genenames():
    import os
    
    #get all the files ending with .png from folder
    genefiles=[]

    for files in os.walk("static/treefiles"):
        print(files)
        for file in files[2]:
        
            name=str(file)
            if name.endswith("png"):
                genefiles.append(name)
   
    #get the name of the gene out of the file names (get rid of tree. and .png)    
    genenames=[]
    for filename in genefiles:
        genex= filename.split(".")[1]
        genenames.append(genex)
        
        
    return genenames

#store the genenames in a variable
lyst_genenames = get_all_genenames()


#define gene input square and redirect to its url
@app.route("/<Gene_name>", methods =["POST", "GET"])
def Gene_name(Gene_name):
    if request.method == "POST":
        gene = request.form["nm"]
        
        return redirect(url_for("gene_phylo", Gene = gene))
    else:
        return render_template("genenamedropdown.html", lyst = lyst_genenames)

#, list1 = json.dumps(Gene_name)
#redirect to requested site
@app.route("/image/<Gene>")
def gene_phylo(Gene):

   return render_template('gene.html', name = Gene)

#run the app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
    

