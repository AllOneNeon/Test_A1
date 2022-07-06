phones = ["Xiaomi Redmi Note 10S", "Смартфон Xiaomi Redmi Note 10 Pro",
         "Apple iPhone 13", "Apple iPhone 11",
          "Huawei nova Y70", "Смартфон Apple iPhone 13 Pro"]

### Первый вариант ###
value = "Apple"
value_apple = []

for i in phones:
    if value.lower() in i.lower():
        value_apple.append(i)

print(value_apple)

### Второй вариант ###
#iphones.append(phones[2:4] + phones[5:])
#print(iphones)

### Третий вариант ###
#phones.sort()
#phones.pop(-1)
#phones.pop(-3)
#phones.pop(-2)
#for i in phones:
    #iphones.append(i)
#print(iphones)


