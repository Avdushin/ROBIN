# words = ["Авто", "Велосипед", "Самолет"]

# str = "Быстрый авто"

# print(any(word.lower() in str.lower() for word in words))

def is_part_in_list(str_, words):
    for word in words:
        if word.lower() in str_.lower():
            return 'Ответ'
    return ''

words = ["Авто", "Велосипед", "Самолет"]
str_ = "Быстрый втомобиль"
print(is_part_in_list(str_, words))