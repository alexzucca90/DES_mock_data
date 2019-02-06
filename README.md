DES 1YR mock data for MGCosmoMC
==================================

The code in this repo is used to produce the Dark Energy Survey (DES) 1 YR mock data  (in the format of [CosmoMC](https://github.com/cmbant/CosmoMC)) .

To use this code, you need to have the code [MGCosmoMC](https://github.com/sfu-cosmo/MGCosmoMC). 

## 1. Installing:
To install this code on your machine, type the following commands on the terminal
```bash
git clone https://github.com/alexzucca90/DES_mock_data
```

## 2. Method. 
This code allows the user to run MGCosmoMC and produce the theoretical predictions for the DES two-point correlation functions from a desired model. Then the mock data is obtained by adding gaussian multivariate  noise from the covariance matrix of the DES data. The dependence on the cosmological model is ignored here.

## 3. Running the code:
To create the DES mock dataset, first run MGCosmoMC using the  files provided in the folder [```mgcosmomc```](/mgcosmomc/). To do so, copy/paste (and replace if needed) the MGCosmoMC file with the one provided in this repo. Then recompile MGCosmoMC using 
```bash
make cosmomc
```
from your MGCosmoMC directory.
You can now run MGCosmoMC with the  [```DES_mock.ini```](/mgcosmomc/DES_mock.ini) initializing file. Type 
```bash
./cosmomc DES_mock.ini
```
Make sure to fix your model parameters in ```params_CMB_defaults.ini```, so that you are sure that you are getting the theoretical predictions for your desired model.

MGCosmoMC will run a likelihood test and will return a set of output files containing the theoretical predictions for your model and the inverse covariance. Put them in this directory (or in the [```input```](/input/) directory). You can now run this code.

Type
```bash
python create_DES_mock_data.py -t theory -i invcov -o output
```
where ```theory``` is a string that declares the theoretical predictions file (such as [this file](/input/DES_theory_vec_linear_weyl_mg1.dat) ), ```invcov``` is the string declaring the file for the inverse covariance matrix (see [this file](/input/) ) and ```output``` is the name of the output file.

## 4. Outputs:
The code will return a set of data files in the output directory that need to be inserted in the MGCosmoMC directory ```data/DES/```. They contain the mock two-point correlation functions. Make sure to edit the file ```data/DES/DES_1YR_final.dataset``` if you want to use this data.
    



