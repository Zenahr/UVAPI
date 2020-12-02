from bs4 import BeautifulSoup

class Retriever:
    """Metadata Retriever for vault items.
    """

    def __init__(self):
        pass

    def retrieve(self, source):
        """Retrieves data of all vault items on the page

        Args:
            source (HTML_string): HTML source string

        Returns:
            [{}]: List of all Vault Items found on the page
        """
        soup = BeautifulSoup(source, features='html.parser')
        vault_items = []
        container = soup.find('div', class_='category-container vault-page')
        if (not container):
            print('Retriever: container div element not detected')
            return 1
        items = container.find_all('div', class_='asset-container')
        if(items):
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
        else:
            print('Retriever: No Vault Items Detected.')


Retriever()