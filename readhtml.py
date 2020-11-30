from bs4 import BeautifulSoup
print("hello")
html = open("index.html").read()
soup = BeautifulSoup(html, features = "lxml")
print(soup.find(id='userinfo'))