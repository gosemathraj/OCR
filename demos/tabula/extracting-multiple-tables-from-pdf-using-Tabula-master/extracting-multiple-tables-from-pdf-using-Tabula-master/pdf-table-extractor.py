#the table will be returned in a list of dataframe,for working with dataframe you need pandas
#import pandas as pd
#first install tabula library and jdk from the command line and set it to environment variable
import tabula
#for looping through the pdf files present in a directory
import os

files = os.listdir(r'D:\RajeshG\Projects\OCR\demos\tabula\extracting-multiple-tables-from-pdf-using-Tabula-master\extracting-multiple-tables-from-pdf-using-Tabula-master\docs') #files contain the list of files present in the folder


#For extracting all the tables in pdf file
for file in files:
    path = 'D:\\RajeshG\\Projects\\OCR\\demos\\tabula\\extracting-multiple-tables-from-pdf-using-Tabula-master\\extracting-multiple-tables-from-pdf-using-Tabula-master\\docs\\'  + file
    df = tabula.read_pdf(path, pages = '1', multiple_tables = True) #page no which you want to
                                                                    #extract,or 'all' for all the pages
    print(df)


#For extracting particular tables you need coordinates of that table
#Please refer README
for file in files:
    path = path = 'D:\\RajeshG\\Projects\\OCR\\demos\\tabula\\extracting-multiple-tables-from-pdf-using-Tabula-master\\extracting-multiple-tables-from-pdf-using-Tabula-master\\docs\\'  + file
    df = tabula.read_pdf(path, area=(35.006,502.824,335.059,478.603), pages=1)
    print(df)
