
# myFile = open('text_doc.txt')
# for line in myFile:
#     print(line)
#     print(len(line))
#
# myFile = open('namefile.txt', 'w')
# myFile.write('tttt')
# print('zzzz', file = myFile)

# with open('text_doc.txt') as myFile:
#     for line in myFile:
#         print(line)

alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphaUP = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
NUMBER = int(input('Введите чилсо, на которое нужно сдвинуть текст: '))

summary = ''
def changeChar(char):
    if char in alpha:
        return alpha[(alpha.index(char) + number) % len(alpha)]
    elif char in alphaUP:
        return alphaUP[(alphaUP.index(char) + number) % len(alphaUP)]
    else:
        return char

with open('text_doc.txt', encoding="utf8") as myFile:
    for line in myFile:
        for char in line:
            summary += changeChar(char)

with open('output.txt', 'w', encoding="utf8") as myFile:
    myFile.write(summary)