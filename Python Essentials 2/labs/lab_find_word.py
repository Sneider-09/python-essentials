str_1 = input("Primera cadena: ").lower().replace(' ', '')
str_2 = input("Segunda cadena: ").lower().replace(' ', '')

for ch in str_1:
    if str_2.find(ch) != -1:
        str_2 = str_2.replace(ch, '', 1)
    else:
        print("No")
        break
else:
    print("Si")