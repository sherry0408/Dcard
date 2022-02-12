import re

# #五個字母組成一個單字
# wwwwwRegex = re.compile(r'\D\D\D\D\D')
# #r，代表原始字串 raw。
# word = wwwwwRegex.search('EW*QRW') #找前五個非數字
# print(word.group())

#五個字母組成一個單字
wwwwwRegex = re.compile(r'[A-Z][A-Z][A-Z][A-Z][A-Z]')
#r，代表原始字串 raw。

letter = input('請輸入五個字母：')
word = wwwwwRegex.search(letter) #找前五個非數字
print(word.group())