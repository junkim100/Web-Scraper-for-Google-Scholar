import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk
from tkinter import simpledialog

# Open csv file
f = open('./file.csv', 'w')
writer = csv.writer(f)

# Write header for csv file
header = ["Article Name", "URL"]
writer.writerow(header)

# Create popup window for user input
ROOT = tk.Tk()
ROOT.withdraw()
user_input = simpledialog.askstring(title="Google Scholar Search",
                                  prompt="Search:")

# Web scraping
address = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C10&q=" + user_input
url = requests.get(address)
html = url.text
soup = BeautifulSoup(html, 'html.parser')

items = soup.findAll('h3', class_='gs_rt')
for item in items:
    data = []
    data.append(item.get_text())
    # print(item.get_text())

    text = str(item.findAll('a', href=True))
    index_start = text.index('href=')+6
    text = text[index_start:]
    index_end = text.index('\"')

    data.append(text[:index_end])
    # print(text[:index_end])
    writer.writerow(data)

# Close csv file
f.close()