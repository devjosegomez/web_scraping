import os
import glob
import pandas
import csv

def concatenate(indir="C:\\Users\\FBI", outfile =  "C:\\Users\\FBI\\All.csv"):
    os.chdir(indir)
    fileList = glob.glob("*.csv")
    dfList = []
    colnames= ["Status", "Categoria", "descuento", "old_price", "new_price",
               "url_product", "product_name"]
    for filename in fileList:
        print(filename)
        df = pandas.read_csv(filename, header= None, delimiter="\t", quoting=csv.QUOTE_NONE, encoding='utf-8')
        dfList.append(df)
        concatDf= pandas.concat(dfList, axis=0)
        concatDf.to_csv(outfile, index=0)


concatenate()
    		
