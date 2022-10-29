# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
#
# Пример
# 	а) AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE => 6A1F2D7C1A17E

data = open('codingText.txt', 'w+')
data.write('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEEN')
data.close()


def Coding(text):
    count = 1
    cod = ''
    lenText = len(text)
    for i in range(lenText - 1):
        if text[i] == text[i + 1]:
            count += 1
            if i + 2 == lenText:
                cod = cod + str(count) + text[i]
        else:
            cod = cod + str(count) + text[i]
            count = 1
    if text[lenText - 2] != text[lenText - 1]:
        cod = cod + str(count) + text[lenText-1]
    return cod


def Decoding(cod):
    num = ''
    text = ''
    i = 0
    while i < len(cod):
        while True:
            num = num + cod[i]
            try:
                a = int(num)
                i += 1
            except:
                for j in range(a):
                    text = text + cod[i]
                i += 1
                num = ''
                break
    return text


fileText = open('codingText.txt', "r")
text = fileText.readline()
print('текст в файле:', text)
cod = Coding(text)
decodingText = Decoding(cod)
print('после сжатия:', cod)
# print(text)
print(f"Текст после расшифровки: {decodingText}")
