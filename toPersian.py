# encoding: utf-8

def enToPersianNumb(number):
    numPersian = ['۰','۱','۲','۳','۴','۵','۶','۷','۸','۹','.']
    numEnglish = ['0','1','2','3','4','5','6','7','8','9','.']
    return replaceing(numEnglish, numPersian, number)

def enToPersianchar(userInput):
    charPersian = [ 'ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'چ', 'ش', 'س', 'ی', 'ب', 'ل', 'ا', 'ت', 'ن', 'م', 'ک', 'گ', 'ظ', 'ط', 'ز', 'ر', 'ذ', 'د', 'پ', 'و','؟' ]
    charEnglish = [ 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',','?' ]
    return replaceing(charEnglish, charPersian, userInput)

def arToPersianNumb(number):
    numArabic = ['١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩', '٠']
    numPersian = ['۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', '۰']
    return replaceing(numArabic, numPersian, number)

def arToPersianChar(userInput):
    charArabic = ['ي', 'ك', '‍', 'دِ', 'بِ', 'زِ', 'ذِ', 'ِشِ', 'ِسِ', '‌', 'ى']
    charPersian = ['ی', 'ک', '', 'د', 'ب', 'ز', 'ذ', 'ش', 'س', '', 'ی']
    return replaceing(charArabic, charPersian, userInput)
    
#list 1 is or  not ok host
#list 2 is or ok dest

def replaceing(host, dest, input):
    
    returnList = list()

    for i in list(unicode(input)):
        if i in host:
            returnList.append(dest[host.index(i)])
        else:
            returnList.append(i)
    
    return ''.join(returnList)
 

print enToPersianNumb('شماره کلاس 312')
print enToPersianNumb(3123123.9012)
print enToPersianNumb(123)
print enToPersianchar('sghl ]i ofv')
print arToPersianNumb('٣٤٥٦')
print arToPersianChar(' ك جمهوري اسلامي ايران')




