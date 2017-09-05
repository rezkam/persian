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



####Convert Persian numbers to english numbers
Convert Persian numbers to english numbers

Example:

```
persian.persianToEngNumb("۱۳۷۱")  #returns: 1371
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
persian.enToPersianchar("لخخلمث")   #returns: google
```



###Contributors

- [Mohammad reza Kamlifard](http://kamalifard.ir/)
- [Keyvan Hedayati](https://github.com/k1-hedayati)
- [Bahram Aghaei](https://github.com/GreatBahram)

###Contributing

This is a open-source project. Fork the project, complete the code and send pull request.
