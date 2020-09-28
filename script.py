import pandas as pd
df = pd.read_csv('csvExampl.csv')
df["Blank A"]=""
df["Blank B"]=""
df["Blank C"]=""
df["Blank D"]=""
df["Blank E"]=""
df["Blank F"]=""
df["Blank G"]=""
df["Blank H"]=""
df["Blank I"]=""
df["Blank J"]=""
df["Blank K"]=""
df["Blank L"]=""
df["Blank M"]=""
df["Blank N"]=""


df = df[['Logo','Location','Title','Company','Description','Blank A','ApplyLink','salary','Blank B','Blank C','Blank D','Blank E','Blank F','Blank G','Blank H','Blank I','Blank J','Blank K','Blank L','Blank M','Blank N',]]
df.to_csv('csvEXAMPLE.csv',index=False)