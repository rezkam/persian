# Persian

A simple Python library for Persian language localization.

[![Tests](https://github.com/rezakamalifard/Persian/workflows/tests/badge.svg)](https://github.com/rezakamalifard/Persian/actions)

Python implementation of [Persian.js](https://github.com/usablica/persian.js)

## Installation

```bash
pip install persian
```

## Functions

### Convert to Persian characters

Used for converting Arabic characters to Persian.

Example:

```python
persian.convert_ar_characters("علي")  # returns: علی
```

### Convert to English numbers from Persian Number

Used for converting Persian numbers to English.

Example:

```python
persian.convert_fa_numbers("۱۳۷۱")  # returns: 1371
```

### Convert to Persian numbers from Arabic Number

Used for converting Arabic numbers to Persian.

Example:

```python
persian.convert_ar_numbers("٣٤٥")  #returns: ۳۴۵
```

### Convert to Persian numbers from English Number

Used for converting English numbers to Persian.

Example:

```python
persian.convert_en_numbers("345")  #returns: ۳۴۵
```

### Change keyboard layout

Converting Persian char to English char by switching the keyboard layout

Example:

```python
persian.convert_en_characters("sghl")  # returns: سلام
```

### Zero-width non-joiner correction

Example:

```python
persian.convert_en_characters("آمده ای ولی من رفته ام و می آییم")  #returns: آمده‌ای ولی من رفته‌ام و می‌آییم
```

### Decode Percent-encoding Characters in URLs

Example:

```python
persian.decode_url(
    "https://fa.wikipedia.org/wiki/%D8%B5%D9%81%D8%AD%D9%87%D9%94_%D8%A7%D8%B5%D9%84%DB%8C")  #returns: https://fa.wikipedia.org/wiki/صفحهٔ_اصلی
```

### Encode non-ASCII Characters in URLs

Example:

```python
persian.encode_url("https://fa.wikipedia.org/wiki/۱۹۸۴_(رمان)")  
# returns: https://fa.wikipedia.org/wiki/%DB%B1%DB%B9%DB%B8%DB%B4_%28%D8%B1%D9%85%D8%A7%D9%86%29
```

## Contributors

- [Reza Kamlifard](https://github.com/rezakamalifard/)
- [Keyvan Hedayati](https://github.com/k1-hedayati)
- [Bahram Aghaei](https://github.com/GreatBahram)
- [Hasan Ramezani](https://github.com/hramezani)
- [Farhad Mortezapour](https://github.com/farhadmpr)

## Contributing

This is a open-source project. Fork the project, complete the code and send pull request.
