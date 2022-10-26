# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'мы старались удалитьабв в любом месте где естьабв'
print(text)
findText = 'абв'
textNew = ''
for i in text.split():
    if findText not in i:
        textNew = textNew + i+' '
print(textNew)
