from bs4 import BeautifulSoup
import urllib2

url = "https://www.pythonforbeginners.com"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

print(soup.prettify())

# print title


# print soup.title.string
# >> ? Python For Beginners

# print soup.p
 


# print soup.a