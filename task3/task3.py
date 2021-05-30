import eel
import pandas as pd


@eel.expose
def search(name, csv_name):
    path = './{}'.format(csv_name)
    file = pd.read_csv(path)
    if name in file.columns:
        source = list(file['name'])
        # name = input('名前を入れてください')
        if name in source:
            return print('{}を見つけました'.format(name)), name
        else:
            source.append(name)
            name_df = pd.DataFrame(data=source, columns=['name'])
            name_df.to_csv(path, encoding="utf-8")
            return print('{}を保存しました'.format(name)), name


eel.init("task3")
eel.start("main.html")




