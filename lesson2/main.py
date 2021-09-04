import random

import requests
from bs4 import BeautifulSoup
import json
import csv

# url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
#
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;\
              q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like \
                  Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36'
}
#
# req = requests.get(url=url, headers=headers)
# src = req.text
# # print(src)
#
# with open('index.html', 'w') as file:
#     file.write(src)

# with open('index.html') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
# links = soup.find_all(class_='mzr-tc-group-item-href')
#
# all_categories_links = {}
#
# for link in links:
#     link_name = link.text
#     link_href = 'https://health-diet.ru' + (link.get('href'))
#     all_categories_links[link_name] = link_href
#
# # save dict into json
# with open('all_categories_links.json', 'w') as file:
#     json.dump(all_categories_links, file, indent=4, ensure_ascii=False)

with open('all_categories_links.json') as file:
    all_categories = json.load(file)

rep = [',', '-', ' ', '\'', '\n']

iteration_count = int(len(all_categories)) - 1
print(f'Всего итераций: {iteration_count}')
count = 0
for category_name, category_href in all_categories.items():

    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, '_')
    req = requests.get(url=category_href, headers=headers)
    src = req.text
    with open(f'data/{count}_{category_name}.html', 'w') as file:
        file.write(src)

    with open(f'data/{count}_{category_name}.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    # проверка на наличие таблицы на странце
    alert_danger = soup.find(class_='uk-alert-danger')
    if alert_danger is not None:
        print("ТЕБЕ ПИЗДА, ПОЭТОМУ ПРОПУСКАЮ")
        continue

    # # проверка страницы на наличие таблицы с продуктами
    # alert_block = soup.find(class_="uk-alert-danger")
    # if alert_block is not None:
    #     continue

    product_info = []

    # собираем заголовки таблицы
    table_head = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text
    for item in rep:
        if item in product:
            product.replace(item, '_')

    with open(f'data/{count}_{category_name}.csv', 'w', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )

    # собираем данные таблицы
    table_body = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')
    for item in table_body:
        product_tds = item.find_all('td')
        title = product_tds[0].text
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text

        for item in rep:
            if item in title:
                title.replace(item, '_')

        product_info.append({
            'title': title,
            'calories': calories,
            'proteins': proteins,
            'fats': fats,
            'carbohydrates': carbohydrates,

        })

        with open(f'data/{count}_{category_name}.json', 'w', encoding='UTF-8') as file:
            json.dump(product_info, file, indent=4, ensure_ascii=False)

        with open(f'data/{count}_{category_name}.csv', 'a', encoding='UTF-8') as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )

    count += 1
    if iteration_count == 0:
        print('[100%] Done')
        break
    print(f'#{count} итерация')
    print(f'Пройдено {count}/ осталось: {iteration_count - 1}')
    iteration_count -= 1
