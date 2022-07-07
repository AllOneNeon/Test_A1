phones = ["Xiaomi Redmi Note 10S", "Смартфон Xiaomi Redmi Note 10 Pro",
         "Apple iPhone 13", "Apple iPhone 11",
          "Huawei nova Y70", "Смартфон Apple iPhone 13 Pro"]

value = "Apple"
value_apple = []

for i in phones:
    if value.lower() in i.lower():
        value_apple.append(i)

print(value_apple)




