# add your code here
import pandas as pd
print(pd.__version__)

data = {'Apples': [35, 41],'Bananas': [21, 34]}

index = ['2017 Sales', '2018 Sales']

fruits = pd.DataFrame(data, index=index)

#Ignore. For testing in python
#print(fruits)

fruits.to_csv('fruit.csv')