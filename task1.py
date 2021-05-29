import pandas as pd
path = './task1.csv'

def search():
    file = pd.read_csv(path)
    if 'name' in file.columns:
        source = list(file['name'])
        name = input('名前を入れてください')
        if name in source:
            print('{}を見つけました'.format(name))
            print(source)
        else:
            source.append(name)
            print('{}を保存しました'.format(name))
            name_df = pd.DataFrame(data=source, columns=['name'])
            name_df.to_csv(path, encoding="utf-8")
            print(source)

search()

