Persian.py
==========

A simple Python library for Persian language localization.
Python Version of [Persian.js](https://github.com/itmard/persian.js)

###Install Package
```
pip install persian
```
###How to use
```
import persian
```
###Functions

#### Convert to Persian characters
Converting Arabic characters to Persian.

Example:
```
persian.arToPersianChar("علي")  #returns: علی
```

####Convert to Persian numbers from Arabic Number

Converting Arabic numbers to Persian.

Example:

```
persian.arToPersianNumb("٣٤٥")  #returns: ۳۴۵
```


####Convert to Persian numbers from English Number
Converting English numbers to Persian.

Example:

```
persian.enToPersianNumb("345")  #returns: ۳۴۵
```



#### Change keyboard layout
Converting Persian char to English char.

Example:

```
persian.enToPersianchar("sghl")   #returns: سلام
```

#### Simple letter substitution cipher
Replaces a letter with the letter 16 letters after it in the alphabet.

Example:

```
persian.rot16('صذچضص')  # returns: 'الفبا'

```
And `rot5()` also replace digits.
Finally `rot21()` replace both.

By: [MohammadSadegh Yazdani](http://pypro.blog.ir)

###Contributors

- [Mohammad reza Kamlifard](http://kamalifard.ir/)
- [Keyvan Hedayati](https://github.com/k1-hedayati)

###Contributing

This is a open-source project. Fork the project, complete the code and send pull request.

###License

The MIT License (MIT)

Copyright (c) 2013 Mohammad reza Kamalifard

    
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
    documentation files (the "Software"), to deal in the Software without restriction, including without limitation 
    the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
    and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in all copies or substantial portions 
    of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED 
    TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
    CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
    IN THE SOFTWARE.
