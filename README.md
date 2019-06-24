# big-num-format

big-num-format is a package which converts very large numbers into human readable text.

### Installation

Simply type the following in a command line to install the package:

`pip install big-num-format`

### Usage

Use the format_num() function to format numbers.

e.g.

```python
>>> from big_num_format import *
>>> format_num(123456789.55)
'123 million, 456 thousnd and 789.55'
>>> format_num(1e50/3, shorten=True, precision=5, decimal_precision=10)
'33QDe 333qDe 333TDe 333DDe 333.3359375UDe'
```
