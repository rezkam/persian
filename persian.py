# encoding: utf-8
'''
persian.py
A simple library for Persian language localization in Python
Copyright (C) 2013 Mohammad reza Kamalifard , kamalifard@datasec.ir
MIT licensed
https://github.com/itmard/persian.py 
'''
def enToPersianNumb(number):
    numPersian = ['۰','۱','۲','۳','۴','۵','۶','۷','۸','۹','.']
    numEnglish = ['0','1','2','3','4','5','6','7','8','9','.']
    dictionary = dict(zip(numEnglish),numPersian)
    return replaceing(numEnglish, numPersian, number)

def enToPersianchar(userInput):
    charPersian = [ 'ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'چ', 'ش', 'س', 'ی', 'ب', 'ل', 'ا', 'ت', 'ن', 'م', 'ک', 'گ', 'ظ', 'ط', 'ز', 'ر', 'ذ', 'د', 'پ', 'و','؟' ]
    charEnglish = [ 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',','?' ]
    dictionary = dict(zip(char(charEnglish),charPersian)
    return replaceing(charEnglish, charPersian, userInput)

def arToPersianNumb(number):
    numArabic = ['١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩', '٠']
    numPersian = ['۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', '۰']
    dictionary = dict(zip(nupArabic),NumPersian)
    return replaceing(numArabic, numPersian, number)

def arToPersianChar(userInput):
    charArabic = ['ي', 'ك', '‍', 'دِ', 'بِ', 'زِ', 'ذِ', 'ِشِ', 'ِسِ', '‌', 'ى']
    charPersian = ['ی', 'ک', '', 'د', 'ب', 'ز', 'ذ', 'ش', 'س', '', 'ی']
    dictionary = dict(zip(charArabic),charPersian)
    return replaceing(charArabic, charPersian, userInput)
    
#list 1 is or  not ok host
#list 2 is or ok dest

def replaceing(input,dictionary):
    
    for i in dictionary:
        transed = input.replace(i,dictionary[i])
        input = transed
    return input
