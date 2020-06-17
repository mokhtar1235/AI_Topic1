import pandas as pd
xl=pd.ExcelFile("Travel Agent KB (2 sheets).xlsx")
df=xl.parse('Flights')
print(df)
from Searching import As_searching


start=input("enter start city: ")
dest=input("enter destination city: ")
list=input("enter travel day: ").split()

As_searching(start,dest,list)

