'''
a) Create file with some content. As example you can take this one
b) Create second file and copy content of the first file to the second file in upper case.
'''

text_1 = """Тому що ніколи тебе не вирвеш,
ніколи не забереш,
тому що вся твоя свобода
складається з меж,
тому що в тебе немає
жодного вантажу,
тому що ти ніколи не слухаєш,
оскільки знаєш і так,
що я скажу,"""

with open('lower_text.txt', 'w') as lower:
    lower.write(text_1)
text_2 = text_1.upper()
with open('upper_text.txt', 'w') as upper:
    upper.write(text_2)
