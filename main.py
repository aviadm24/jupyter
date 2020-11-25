import pandas as pd

checkFile = pd.read_excel("check.xls", na_values=['לא ידוע', 'אין'])
print(checkFile.head())