# Foo Package

Python package for Foo et al physics calculations.

## Prerequisites

- Python3
- pip3

Refer to [this documentation](https://packaging.python.org/en/latest/tutorials/installing-packages/) on how to install them.

## Usage

From the command line, run:

1. clone repo
2. from /Foo run:
  ``` pip install . ```
  This builds the package on your machine
3. In a new terminal window, run:

```bash
>>> python
>>> foo.sphereVolume(<test radius integer>)
<output volume value>
>>> foo.sphereSA(<test radius integer>)
<output Surface Area value>
```

The test.py file can be used to see how the package's functions can be imported and called upon.

To run the test file on the command line, from the /Foo root directory, run:
``` python .\test.py ```

## References

As a refresher for how python packages are built, [this tutorial link](https://www.tutorialspoint.com/python/python_packages.htm) was used and can be used whenever developers want to add new science features.
