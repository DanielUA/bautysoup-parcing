from bs4 import BeautifulSoup

with open('html/spain.html') as file:
    soup = BeautifulSoup(file, 'lxml')

# title = soup.title
# print(title.text)
# print(title.get_text())
# print(title.string)

h1 = soup.h1

# print(h1)
# print(h1.string)
# print(h1.attrs)
# print(h1.attrs['id'])
# print(h1.get('id'))
# print(h1.get('id2'))
# print(h1.has_attr('id'))
# print(h1.has_attr('id2'))
# print(h1.text.strip())
# print(h1.get_text(strip=True))

#find(),find_all() this methotds use for searching ih html, method find() search only one element
print(soup.find('a'))
print(soup.a)
