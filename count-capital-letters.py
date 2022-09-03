"""
If you need to find small letters:
i.isupper() -> i.islower()
"""

with open('text_capital.txt') as file:
    count = 0
    text = file.read()
    for i in text:
        if i.isupper():
            count += 1
    print(count)


