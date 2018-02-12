import pandas as pd

def compare(f1,f2):
  df1 = pd.read_csv(f1)
  df2 = pd.read_csv(f2)
  
  if df1.equals(df2):
    return 0
  else:
    return 1
  
  
 
f1= 'angles_UCI_CS.csv'
f2 = 'angles_UCI_CS_out.csv'

print(compare(f1,f2))
