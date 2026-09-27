#numbers = (10 , 20 ,30 ,40)
#numbers[0] = 5
#print(numbers[0])

# numbers = {1,2,3,2,3,2,1,} #set
# print(numbers)

# user = {
#     "name": "Сергей",
#     "age": 13,
#     "country": "Switzerland"
# }
# user ["age"]= 13
# user ["email"] = "kosterin4523"
# del user ["country"]

# # print(user.keys())
# # print(user.valus())
# # print(user.items())


# for key, value in user.items():
#     print(key, ":" , value)













text = input("Введите текст:")

words = text.split()

print("всего слов:",len(words))

unique = set(words)
print("Уникальных Слов:",len(unique))

fra = {}

for word in words:
    if word not in fra:
        fra[word] = 1
    else:
        fra[word] += 1


max_word = ""
max_count = 0

for word,count in fra.items():
    if count > max_count:
        max_word = word
        max_count = count

print("Самое частое Число:",max_word)
print("Встречается раз:",max_count)