from bs4 import BeautifulSoup

class Retriever:

    def __init__(self):
        pass

    def retrieve(self, source):
        soup = BeautifulSoup(source)
        vault_items = []
        container = soup.find('div', class_='category-container vault-page')
        items = soup.find_all('div', class_='asset-container')
        for item in items:
            try:
                item_data = {
                'name' : item.find('a', class_='mock-ellipsis-item mock-ellipsis-item-helper ellipsis-text').get_text(),
                'link' : 'https://www.unrealengine.com' + item.find('a', class_='mock-ellipsis-item mock-ellipsis-item-helper ellipsis-text')['href'],
                'publisher' : item.find('div', class_='creator ellipsis').get_text(),
                'amount_of_ratings' : item.find('span', class_='rating-board__count').get_text(),
                'img_src' : item.find('img')['src'],
                }
                vault_items.append(item_data)
            except:
                pass
        return vault_items

Retriever()