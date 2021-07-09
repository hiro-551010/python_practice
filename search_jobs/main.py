import eel
import search_keyword

@eel.expose
def search_jobs(keyword, csv_name):
    search_keyword.search(keyword, csv_name)

eel.init("web")
eel.start("index.html") 