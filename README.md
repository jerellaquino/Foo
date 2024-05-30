# Foo Package

Python package for Foo et al physics calculations.

## Prerequisites

- Python3
- pip3
- git
  
Refer to [this documentation](https://packaging.python.org/en/latest/tutorials/installing-packages/) on how to install pip and python. Git can be downloaded [here](https://git-scm.com/downloads).

## Usage

From the command line, run:

1. clone repo
2. from /Foo run:
  ``` pip install . ```
  This builds the package into your Python environment
3. for basic python shell use, in a new terminal window, run:

```bash
>>> python
>>> foo.sphereVolume(<test radius integer>)
<output volume value>
>>> foo.sphereSA(<test radius integer>)
<output Surface Area value>
```

 See the section below for other uses.

### Interactive Script and Example Usage

See the ./scripts folder for examples how the package's functions can be imported and called upon.

An interactive foo calculator can be ran command line.
To use this interactive calculator script, from the /Foo directory of this repo, run:
``` python .\scripts\ineteractive_foo_calc.py ```

## Testing and further work

Further additions to the foo physics parameterization can be expanded in the calc_functions.py file or by adding new files.
Be sure to add anymore new functions to the __init__.py file.

For testing these functions, the ./tests folder contains unit tests for the functions.

To run unit tests for the sphere functions, from the /Foo dir, run:
```python .\tests\test_sphere_calc_unittest.py```

If all tests ran correctly, the expected result should show "OK".

More tests can be added as more Foo physics additions are made.

## References

As a refresher for how python packages are built, [this tutorial link](https://www.tutorialspoint.com/python/python_packages.htm) was used and can be used whenever developers want to add new science features.

For the interactive calculaor script, [this article](https://www.geeksforgeeks.org/make-simple-calculator-using-python/) was used for inspiration.
