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
git clone https://github.com/caldetas/bio-294.git   
cd bio-294
```

   
### Create anaconda environment
The dependencies.yml file creates an environment with some programs and packages you will need.
```
conda env create --file dependencies.yml
conda activate bio294
```

   
```hello```
---
## Create sequences from VCF
Download the vcf and the index.
```
wget 'http://www.caldetas.com:8080/s/YV2VokbiA6uSnhz/download?path=%2F&files=Bdis333_5_1_21.renamed.SNPs.vcf.bgz.tbi'
wget 'http://www.caldetas.com:8080/s/YV2VokbiA6uSnhz/download?path=%2F&files=Bdis333_5_1_21.renamed.SNPs.vcf.bgz'
```

---
https://www.geeksforgeeks.org/how-to-create-dynamic-autocomplete-search-using-bootstrap-typeahead/
