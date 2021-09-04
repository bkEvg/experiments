from bs4 import BeautifulSoup
import re


with open('blank/index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

# find_h1 = soup.find_all('h1')
# print(find_h1)

# username = soup.find('div', class_='user__name')
# print(username.text.strip())

# username = soup.find('div', class_='user__birth__date').find('span')
# print(username.text)

# username = soup.find_all('div', {'class': 'user__name'})
# print(username)

# username = soup.find('div', class_='user__info').find_all('span')
# for i in username:
#     print(i.text)

# social_links = soup.find('div', class_='social__networks').find('ul').find_all('a')
# print(social_links)

# all_a = soup.find_all('a')
# for a in all_a:
#     link = a.get('href')
#     text = a.text
#     print(f'{link} --- {text}')

# .find_parent() and .find_parents()

# post_text = soup.find('div', class_='post__text').find_parents()
# print(post_text)

# .next_element and .previous_element

# next_el = soup.find('div', class_='post__title').next_element.next_element
# print(next_el.text)

# find_next_el = soup.find('div', class_='post__title').find_next()
# print(find_next_el.text)

# previous_el = soup.find('div', class_='post__title').previous_element.previous_element
# print(previous_el.text)

# .find_next_sibling() and .find_previous_sibling()

# next = soup.find(class_='post__title').find_next_sibling()
# print(next)

# links = soup.find(class_='some__links').find_all('a')
# for link in links:
#     link_url = link.get('href')
#     link_data_attr = link.get('data-attr')
#     # link_data_attr = link['data-attr'] # does the same as above!
#     link_text = link.text
#     print(f'{link_url}   {link_data_attr}   {link_text}')


# filter by a text 

# filter = soup.find('h3', text='Twitter будет банить')
# print(filter)

# filter = soup.find('h3', text='Twitter будет банить пользователей, которые желают смерти другим')
# print(filter)

filter = soup.find('a', text=re.compile("welcome"))
print(filter)

filter = soup.find_all(text=re.compile('([Ww]elcome)'))
print(filter)