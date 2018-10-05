import requests
from bs4 import BeautifulSoup
import json


r = requests.get('https://www.google.co.in/search?q=ayush+aggawral&rlz=1C1CHBF_enIN765IN765&oq=ayush+aggawral&aqs=chrome..69i57j0l5.2221j0j9&sourceid=chrome&ie=UTF-8')
#print(r.content,'\n\n\n\n')

"""bs4 = BeautifulSoup(r.content,'html.parser')
#print(bs4)
soup = bs4.prettify()
print(bs4.div,'\n')
print(bs4.body())
"""

soup = BeautifulSoup(r.content,'html.parser')
#print(soup.find_all('cite'))
soup1 = soup.find_all('cite')
soup2 = soup.find_all('a',{'class':'gs4'})

for i in soup1:
    print(i,'\n')

print('starting classes\n')
for j in soup2:
    print(j)
