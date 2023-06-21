import pandas as pd
animalset={'animals': ['Tiger', 'Bear', 'Moose'], 'age': [12, 21, 13]}
myvar=pd.DataFrame(animalset)
a= [1, 7, 2]
myvar2=pd.Series(a)
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar3=pd.Series(calories)
myvar4=pd.read_csv('./Iris.csv')
print(myvar)
print(myvar2)
print(myvar3)