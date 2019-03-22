import requests, bs4
res = requests.get('https://nostarch.com/automatestuff/')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
# type(noStarchSoup)
# print("Here comes the money! \n")
# print(noStarchSoup)
author = noStarchSoup.select('.notice')
print(author)
