#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:52:37 2021

@author: hannes
"""

from flask import Flask, redirect, url_for, render_template, request, session, flash, json
import os

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
    if request.method =="POST":
        return redirect(url_for("Gene_name"))
    else:
        return render_template('index.html', bigtitle=title)


#function to get the genes present in folder
##CAUTION: that this command works: make shure that the working directory of spyder is in /treebrowser ! ohterwise will only get empty list!
def get_all_genenames():

    #store genename with genefile
    all_files={}
    
    #get the pictures of the genefiles in the folder
    genefiles=[]

    
    #extract all the files ending with .png and store the names in list
    for files in os.walk("static/treefiles"):
        #print(files)
        for file in files[2]:
        
            name=str(file)
            if name.endswith("png"):
                genefiles.append(name)
     
    
    #only take out the genename out of the complete filename            
    genenames=[]
    for filename in genefiles:
        gene= filename.split(".")[1]
        genenames.append(gene)
        
        
    #make a dictionary with teh genename and its filename    
    for counter, fyle in enumerate(genenames):
        all_files[genenames[counter]]=genefiles[counter]
    
    
    #return the genename list and the dictionary all_files in a touple
    return genenames, all_files


#store the genenames and all_fyles in two different variables
genen, af = get_all_genenames()
#print(genen)

#define gene input square and redirect to its url
@app.route("/<Gene_name>", methods =["POST", "GET"])
def Gene_name(Gene_name):
    if request.method == "POST":
        gene = request.form["nm"]
 
        return redirect(url_for("gene_phylo", Gene = gene))
    else:
        return render_template("drop.html", lyst=genen)


#redirect to requested site to see the tree of the wanted gene
@app.route("/image/<Gene>")
def gene_phylo(Gene):

   return render_template('gene.html', name = af.get(Gene), short=Gene)



#define the about page
@app.route("/About")
def About():
    return render_template('abt.html')


#define the report page
@app.route("/Report")
def Report():
    return render_template("rep.html")

#run the app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
    

