import requests, bs4
res = requests.get('https://nostarch.com/automatestuff/')
res.raise_for_status()
resText = res.text
exampleSoup = bs4.BeautifulSoup(resText)
# elems = exampleSoup.select('#author')
# type(elems)
# len(elems)
# print(exampleSoup)
# elems[0].getText()
print(resText)
print("****** BREAK BREAK BREAK")

print(exampleSoup.find_all('*'))