from models.item import Item


url = "https://www.johnlewis.com/2019-apple-ipad-mini-apple-a12-ios-7-9-inch-wi-fi-64gb/space-grey/p4067399"
tag_name = "p"
query = {"class": "price price--large"}

item= Item(url,tag_name,query)
print(item.load_price())




#añadiendo algo




















