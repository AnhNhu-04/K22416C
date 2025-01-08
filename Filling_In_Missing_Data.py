# fill na bằng mean
from numpy import nan as NA
import pandas as pd
data = pd.DataFrame([[1., 6.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 6.5, 3.]])
print(data)
print("fill na bàng mean")
print("-"*10)
cleaned1=data.fillna(data.mean())
print(cleaned1)

#fill na bằng 0
print("fill na bằng 0")
print("-"*10)
cleaned2 = data.fillna(0)
print(cleaned2)

#fill na bằng trung vị
print("fill na bằng MEDIAN")
print("-"*10)
cleaned3 = data.fillna(data.median())
print(cleaned3)

#fill na bằng mode
print("fill na bằng MODE")
print("-"*10)
cleaned4 = data.fillna(data.mode().iloc[0])
print(cleaned4)
