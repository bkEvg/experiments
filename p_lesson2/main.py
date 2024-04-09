import requests
from bs4 import BeautifulSoup
import json

url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\
    image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36'
}


class WebParser:
    """Allow you to scrap web site"""
    counter = 0

    def __init__(self):
        self.request = requests.get(url=url, headers=headers)
        self.soup = BeautifulSoup(self.request.text, 'lxml')
        # self.save_main_page()
        # self.get_all_categories()
        # self.save_categories()
        self.main()

    def save_main_page(self):
        src = self.request.text
        with open('index.html', 'w') as file:
            file.write(src)
        print('[INFO] Main page saved')

    def get_all_categories(self):
        categories = self.soup.find_all(class_='mzr-tc-group-item-href')
        return categories

    def save_as_json(self, object, filename='data.json'):
        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump(object, file, indent=4, ensure_ascii=False)
            print('[INFO] JSON file saved')

    def clear_word(self, word):
        rep = [' ', '\'', '-', ',']
        for item in rep:
            if item in word:
                word = word.replace(item, '_')
        return word

    def save_categories(self):
        categories_list = {}
        categories = self.get_all_categories()
        for category in categories:
            category_url = 'https://health-diet.ru' + category.get('href')
            category_name = self.clear_word(category.text)
            categories_list[f'{category_name}'] = category_url
        self.save_as_json(categories_list, 'categories.json')

    def main(self):
        print('i do nothing')
        with open('categories.json') as file:
            categories = json.load(file)
        for category_name, category_href in categories.items():
            req = requests.get(url=category_href, headers=headers)

            with open(f'data/{self.counter}_{category_name}.html', 'w') as file:
                file.write(req.text)

            with open(f'data/{self.counter}_{category_name}.html') as file:
                src = file.read()

            self.counter += 1
            if self.counter == 1:
                break

            soup = BeautifulSoup(src, 'lxml')
            table_head = soup.find(class_='mzr-tc-group-table')
            print(table_head)


parser = WebParser()

# with open('categories.json') as file:
#     categories = json.load(file)
# for category_name, category_href in categories.items():
#     req = requests.get(url=category_href, headers=headers)
#
#     with open(f'data/{parser.counter}_{category_name}.html', 'w') as file:
#         file.write(req.text)
#
#     with open(f'data/{parser.counter}_{category_name}.html') as file:
#         src = file.read()
#
#     parser.counter += 1
#     if parser.counter == 1:
#         break
#
#     soup = BeautifulSoup(src, 'lxml')
#     table_head = soup.find(class_='mzr-tc-group-table')
#     print(table_head)
