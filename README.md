# Bio-294
---
### Install anaconda
You can get anaconda from here:   
https://docs.conda.io/en/latest/miniconda.html   
### Install git

```
sudo apt install git-all
```
### Install github repository bio-294

```
git clone https://github.com/leonkrap/bio-294 
cd bio-294
```

   
### Create anaconda environment
The dependencies.yml file creates an environment with some programs and packages you will need.
```
conda env create --file dependencies.yml
conda activate bio294
```
   
### Open the genome browser with the terminal
Make shure that you are in the treebrowser folder!

To open the genome browser use the following command:
```
python treebrowser.py
```
Then Flask will then load the browser. To open it you can copy the https:// link (it comes up in the line starting with " * Running on ") into your internet browser.

### Possible issue
It might be, that the browser cannot load all possible gene trees to display them in the dynamic autocomplete search bar. If this error occurs you can open the treebrowser.py file in Spyder and then make shure that the "IPython console" has its working directory set to the folder "../bio294/treebrowser" 
