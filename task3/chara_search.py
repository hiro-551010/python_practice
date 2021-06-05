import os 
import pandas as pd
import eel


def search(chara_name, csv_name):
    path = os.path.join(os.path.dirname(__file__), csv_name)
    file = pd.read_csv(path)
    source = list(file['name'])

    if chara_name in source:
        print('{}を見つけました'.format(chara_name))
        eel.log_js('{}を見つけました'.format(chara_name))
    else:
        source.append(chara_name)
        name_df = pd.DataFrame(data=source, columns=['name'])
        name_df.to_csv(path, encoding="utf-8")
        print('{}を保存しました'.format(chara_name))
        eel.log_js('{}を保存しました'.format(chara_name))