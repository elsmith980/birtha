import requests 
from bs4 import BeautifulSoup
page = requests.get("https://www.drugs.com/mtm/previfem.html")
soup = BeautifulSoup(page.content, 'html.parser')


description = soup.find_all("p")[2]


f = open("description.txt", "a")
f.write(str(description))
f.close()