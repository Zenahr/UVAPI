from bs4 import BeautifulSoup
soup = BeautifulSoup(open('dump.html', 'r'))
vault_items = []
# container = soup.find('div', class_='category-container vault-page')
item = soup.find('div', class_='asset-container')
name = item.find('a', class_='mock-ellipsis-item mock-ellipsis-item-helper ellipsis-text').get_text()
link = 'https://www.unrealengine.com' + item.find('a', class_='mock-ellipsis-item mock-ellipsis-item-helper ellipsis-text')['href']
publisher = item.find('div', class_='creator ellipsis').get_text()
amount_of_ratings = item.find('span', class_='rating-board__count').get_text()
img_src = item.find('img')['src']
print(name)
print(publisher)
print(link)
print(img_src)
print(amount_of_ratings)
# for vault_item_content in vault_items:
#     item_name = vault_item_content.find('div', class_='mock-ellipsis-item mock-ellipsis-item-helper ellipsis-text')
#     # review = review.strip()
#     vault_items.append(item_name)
# print(vault_items)