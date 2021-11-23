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
   
      
      

---
## Create sequences from VCF
Download the vcf and the index.
```
wget 'http://www.caldetas.com:8080/s/YV2VokbiA6uSnhz/download?path=%2F&files=Bdis333_5_1_21.renamed.SNPs.vcf.bgz.tbi'
wget 'http://www.caldetas.com:8080/s/YV2VokbiA6uSnhz/download?path=%2F&files=Bdis333_5_1_21.renamed.SNPs.vcf.bgz'
http://www.caldetas.com:8080/s/YV2VokbiA6uSnhz
```
``` 
# send command to shell and read output
import subprocess

proc = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE)

for line in proc.stdout:
    line = str(line.rstrip())[2:-1].encode().decode('unicode_escape').split(sep='\t')
    if True == True:
        print('\t'.join(line))
```
``` 
# send command to shell and read output
import subprocess
vcf = 'filename'
#get the samplenames and positions in vcf
 proc = subprocess.Popen('bcftools view {}'.format(data.settings['vcf']), shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)
        
            for line in proc.stdout:
                line = str(line.rstrip())[2:-1].split(sep='\\t')
                if line[0] == '#CHROM':
                    lyst_samples = line[9:]
                    print('samples =', (lyst_samples))
                    os.killpg(os.getpgid(proc.pid), signal.SIGTERM)

```
---
https://www.geeksforgeeks.org/how-to-create-dynamic-autocomplete-search-using-bootstrap-typeahead/
