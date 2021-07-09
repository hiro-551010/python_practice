import eel
import chara_search 

@eel.expose
def kimetu_search(chara_name, csv_name):
   chara_search.search(chara_name, csv_name)



eel.init("task3")
eel.start("main.html")




