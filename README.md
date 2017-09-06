Persian.py
==========

A simple Python library for Persian language localization.

Python package like [Persian.js](https://github.com/usablica/persian.js)

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
persian.convert_ar_characters("علي")  #returns: علی
```

####Convert to Persian numbers from Arabic Number

Converting Arabic numbers to Persian.

Example:

```
persian.convert_ar_numbers("٣٤٥")  #returns: ۳۴۵
```


####Convert to Persian numbers from English Number
Converting English numbers to Persian.

Example:

```
persian.convert_en_numbers("345")  #returns: ۳۴۵
```



#### Change keyboard layout
Converting Persian char to English char.

Example:

```
persian.convert_en_characters("sghl")   #returns: سلام
```



###Contributors

- [Mohammad reza Kamlifard](http://kamalifard.ir/)
- [Keyvan Hedayati](https://github.com/k1-hedayati)

###Contributing

This is a open-source project. Fork the project, complete the code and send pull request.
