from tkinter import *
import requests
from tkinter import messagebox
from PIL import Image, ImageTk


def fetchNews():
    country = country_text.get()
    api = "https://api.printful.com/countries"
    response = requests.get(api)
    data = response.json()
    results = data['result']
    cc = ''
    for r in results:
        if(country.lower() == r["name"].lower()):
            cc = r["code"].lower()
    print(cc)
    if(cc == ''):
        messagebox.showerror("News App", "invalid country name")
    else:
        displayNews(cc)


def displayNews(cc):
    api = "https://newsapi.org/v2/top-headlines?country=" + \
        cc+"&apiKey=bdc912d442614e15846f1804f1b751d8"
    response = requests.get(api)
    data = response.json()
    articles = data["articles"]
    myArticles = ''

    for a in articles:
        myArticles = myArticles+a["title"]+'\n'

    news_label["text"] = myArticles


root = Tk()
root.geometry("700x450")


root.title("News App")

news_label = Label(root, text="", font=("bold", 15))
news_label.place(x=200, y=150)
country_text = StringVar()
country_entry = Entry(root, textvariable=country_text,
                      bg="lightgrey").place(x=600, y=40)

searchbar = Button(root, text="Search News", width=12,
                   command=fetchNews).place(x=600, y=70)

root.mainloop()
