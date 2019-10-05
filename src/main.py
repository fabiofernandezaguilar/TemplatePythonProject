import pandas as pd 
import numpy
import os
import yaml

#config = yaml.load(open('config/config.yml'))
#print(config)
inputfile ='/data/input_data.csv'
print (inputfile)

#se cargan los datos a un dataframe
#data = pd.read_csv('data/CobrosAutomaticos_original.txt')
data = pd.read_csv(inputfile, sep=',')
data.head(10)





