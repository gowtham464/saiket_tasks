import requests
from bs4 import BeautifulSoup

def web_scrape():
    url="https://www.w3schools.com/html/html_tables.asp"
    permission=requests.get(url)
    
    if permission.status_code != 200:
        print("failed to fetch the page")    
    soup=BeautifulSoup(permission.text, "html.parser")
    headlines=soup.find_all("h2")
    for i, headline in enumerate(headlines,start=1):
        text=headline.get_text(strip=True)
        print(f"{i}. {text}\n")
        
    with open("web_headline.text","w",encoding="utf-8") as f:
       for i, headline in enumerate(headlines,start=1):
           text=headline.get_text(strip=True)
           f.write(f"{i}. {text}\n")
        
if __name__ =="__main__": 
    web_scrape()     
        

        