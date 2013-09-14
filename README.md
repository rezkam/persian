persian.py
==========

A simple Python library for Persian language localization.

##How to use
Simply import 'persian.py' and use the functions.

##Functions

###1) Convert to Persian characters
----------
Used for converting Arabic characters to Persian.

Example:

```python
arToPersianChar("علي")  #returns: علی
````

###2) Convert to Persian numbers from Arabic Number
----------
Used for converting Arabic numbers to Persian.

Example:

```python
arToPersianNumb("٣٤٥")  #returns: ۳۴۵
````
###3) Convert to Persian numbers from English Number
----------
Used for converting English numbers to Persian.

Example:

```python
enToPersianNumb("345")  #returns: ۳۴۵
````

###4) Change keyboard layout
----------
Used for converting Persian char to English char.

Example:

```python

enToPersianchar("لخخلمث")   #returns: google
````
##Contributors

- [Mohammad reza Kamlifard](http://kamalifard.ir/)

##Contributing

This is a open-source project. Fork the project, complete the code and send pull request.

##License

The MIT License (MIT)

Copyright (c) 2013 Mohammad reza Kamalifard

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
