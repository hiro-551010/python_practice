import pandas as pd

path = './task2.csv'
file = pd.read_csv(path, sep=",")
exp_name_list = list(file['company'])
df = pd.DataFrame(data=exp_name_list, columns=['company'])
print(df.head(3))
