temp = 5
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")
else:
    print("The weather is moderate")
