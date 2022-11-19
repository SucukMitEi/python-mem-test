# mem

mem is a Python package for memory editing with Python on Linux.

## Installation instructions

1. 
2.

## Usage

```python
from mem import MEM

# open a process
mem = MEM(12345) # by PID
# or
mem = MEM.fromName("konsole") # by name

value = mem.readInt(0x7fffffff)
print(value)
```

## Contributing

You can make a pull request if you want to change something or add something.

## License

[MIT](https://choosealicense.com/licenses/mit/)
