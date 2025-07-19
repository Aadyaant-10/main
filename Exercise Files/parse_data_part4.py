import xml.etree.ElementTree as ET

file_path = "groceries.xml"

tree = ET.parse(file_path)
root = tree.getroot()

item_over_6 = []

for item in root.findall("grocery_item"):
    name = item.find("name").text
    price = item.find("price").text
    if float(price) > 6:
        item_over_6.append(name)
    print(name, price)

print("Items with price over 6:", item_over_6)