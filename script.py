
from bs4 import BeautifulSoup
import requests


url = "https://www.businessinsider.in/thelife/personalities/news/top-100-richest-people-in-the-world/articleshow/74415418.cms"

html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'html.parser')

data = []
div = soup.find('div', attrs={'class':'inline-table'})
table = div.find('table')
table_body = table.find('tbody')

rows = table_body.find_all('tr')

richest_person_list = []
for row in rows:
    cells = row.find_all('td')
    if len(cells) == 5:
        position = cells[0].find(text=True)
        name = cells[1].find(text=True)
        worth = cells[2].find(text=True)
        company_name = cells[3].find(text=True)
        country = cells[4].find(text=True)
        
        new_richest_person = { 'position':position , 'name': name, 'worth': worth, 'company_name': company_name, 'country': country}
        
        richest_person_list.append(new_richest_person)

        
def get_richest_person_worth(name):
    for single_person in richest_person_list: 
        if single_person['name'].lower() == name.lower():
            return single_person['worth']


        
        

# print(data)