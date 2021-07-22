# Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.


string_a = 'Meet my family There are five of us  my parents my elder brother my baby sister and me'
string_a = string_a.split()
print(max(string_a, key=len))

for el in string_a:
    count = string_a.count(el)
    if count > 1:
        print(el)
