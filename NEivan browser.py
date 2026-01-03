from customtkinter import *
import webbrowser

root = CTk()

root.geometry('600x600')
root.title('NEivan browser')

custom_font = CTkFont(family='GruntGrotesk', size=100, weight='bold')

def search(event=None):
    query = entry2.get().strip()
    if not query:
        return

    if '.' in query and ' ' not in query:
        if not query.startswith("http"):
            query = "https://" + query
        webbrowser.open(query)
    else:
        search_url = "https://www.google.com/search?q=" + query.replace(' ', '+')
        webbrowser.open(search_url)


entry2 = CTkEntry(root, width=550, height=20)
entry2.place(x=25, y= 250)
entry2.bind('<Return>', search)

Welcome = CTkLabel(root, text='Welcome', text_color='blue', width=400, height=150, font=custom_font)
Welcome.place(x=75, y=50)

root.mainloop()