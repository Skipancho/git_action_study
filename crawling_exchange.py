import requests
from bs4 import BeautifulSoup

def parsing_bs(url):

    data = requests.get(url)

    html = data.text

    soup = BeautifulSoup(html,'html.parser')
    return soup

def extract_data(soup):

    data_rows = soup.find("table", attrs={"class":"tbl_exchange today"}).find("tbody").find_all("tr")
    row = data_rows[0]
    cols = row.find_all("td")
    date = row.find("td",attrs={"class":"date"}).get_text()
    num = row.find("td",attrs={"class":"num"}).get_text()
    num = num.replace(",","")

    contents = f'Date : {date} , 매매 기준율 : {num}'

    return contents
