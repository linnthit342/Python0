
# ft_package

A sample Python package for counting occurrences of an item in a list.

## Installation

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
print(count_in_list(["toto", "tata", "toto"], "tutu"))
```

Expected output:

```text
2
0
```
