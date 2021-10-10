import tkinter as tk
from tkinter import ttk
import webbrowser
import re

ws = tk.Tk()
ws.geometry("500x900")
ws.title("Job Search")

zipcodeurl = 'https://www.zipcodes.org'

jobsearch = ttk.Frame(ws)
jobsearch.pack(padx=0, pady=0, fill='x', expand=True)

#Labels and Entries for user input to build out each URL str
entries = []
search1_label = ttk.Label(ws,text = "Job Search")
search1_label.pack(fill='x', expand=True)
search1 = ttk.Entry(ws)
search1.pack(fill='x', expand=True)
entries.append(search1)

zipcode_label = ttk.Label(ws ,text = "Zipcode")
zipcode_label.pack(fill='x', expand=True)
zipcode1 = ttk.Entry(ws)
zipcode1.pack(fill='x', expand=True)
entries.append(zipcode1)

distance_label = ttk.Label(ws ,text = "Radius")
distance_label.pack(fill='x', expand=True)
distance1 = ttk.Entry(ws)
distance1.pack(fill='x', expand=True)     
entries.append(distance1)

#zipcode lookup button 
zipcodelookup = ttk.Button(ws, text='Zip Code Lookup', command =lambda:zipcodeurl_clicked())
zipcodelookup.pack(fill='x',expand=True,pady=0)

#zipcode lookup button function
def zipcodeurl_clicked():
    webbrowser.open(zipcodeurl,new=2,autoraise=False)

#URL Checkboxes
indeedv = tk.IntVar()
indeedcheck = ttk.Checkbutton(ws, text='Indeed', variable=indeedv)
indeedcheck.pack(fill='x', expand=True)

zipv = tk.IntVar()
zipcheck = ttk.Checkbutton(ws, text='ZipRecruiter', variable=zipv)
zipcheck.pack(fill='x', expand=True)

#submit button runs check box variables
submit = ttk.Button(ws, text='Search',command =lambda:submit_clicked())
submit.pack(fill='x', expand=True, pady=0)

def submit_clicked():
    """Callback when submit button clicked
    """
    #transforming answers from user into indeed.com search results url and then opening webbrowser with results.
    if indeedv.get() == 1:
        print(indeedv)
        s = ""
        indeedurl = 'https://www.indeed.com/jobs'
        i = search1.get()
        indeedsearch = i.replace(" ","+")
        indeedurldict = {'?q=':indeedsearch,'&l=':zipcode1.get(), '&radius=':distance1.get()}
        indeedurlstr = str(indeedurldict)
        indeedstr = indeedurlstr.replace(',',"").replace("'","").replace(" ","").replace("{","").replace("}","").replace(":","")
        indeed = s.join(indeedurl+indeedstr)
        webbrowser.open(indeed,new=2,autoraise=True)
        print(indeed)
    if zipv.get() == 1:
        #transforming answers from user into ziprecruiter.com search results url and then opening webbrowser with results.
        s = ""
        zipurl = 'https://www.ziprecruiter.com/candidate/search'
        z = search1.get()
        ziprecsearch = z.replace(" ","+")
        zipurldict = {'?search=':ziprecsearch, '&location=':zipcode1.get(),'&radius=':distance1.get()}
        zipurlstr = str(zipurldict)
        zipstr = zipurlstr.replace(',',"").replace("'","").replace(" ","").replace("{","").replace("}","").replace(":","")
        ziprecruiter = s.join(zipurl+zipstr)
        webbrowser.open(ziprecruiter,new=2,autoraise=True)
        print(ziprecruiter)

ws.mainloop()
