import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data = {
    'sales': [100000,222000,1000000,522000,111111,222222,1111111,20000,75000,90000,1000000,10000],
    'city': ['Tampa','Tampa','Orlando','Jacksonville','Miami','Jacksonville','Miami','Miami','Orlando','Orlando','Orlando','Orlando'],
    'size': ['Small', 'Medium','Large','Large','Small','Medium','Large','Small','Medium','Medium','Medium','Small',]
}

df = pd.DataFrame(data=data)
print(df)

encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False).set_output(transform='pandas')
one_hot_encoded = encoder.fit_transform(df[['city']])
print(one_hot_encoded)