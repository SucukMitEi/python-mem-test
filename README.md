# mem

mem is a Python package for memory editing with Python on Linux.

## Installation instructions

### Latest

1. `git clone https://github.com/SucukMitEi/python-mem-test.git`
2. `cd python-mem-test`
3. `sudo pip install .`

### Releases

1. Download a release
2. `sudo pip install <path of archive>`

## Usage

```python
from mem import MEM

# open a process
mem = MEM(12345) # by PID
# or
mem = MEM.fromName("game") # by name

value = mem.readInt(0x7fffffff)
print(value)
```

## Running

Run the file with `sudo python3 myfile.py`

## Examples

There are two examples in the examples folder.

## License

[MIT](https://choosealicense.com/licenses/mit/)
