# Foo Package

Python package that parameterizes Foo et al physics calculations.

## Prerequisites

- Python3
- pip3
- git
  
Refer to [this documentation](https://packaging.python.org/en/latest/tutorials/installing-packages/) on how to install pip and python. Git can be downloaded [here](https://git-scm.com/downloads).

## Usage

From the command line, run:

1. clone repo
2. from ```/Foo/foo_package``` directory run:
  ``` pip3 install . ``` which builds the package.
3. See the section below for use cases.

### Interactive Script and Example Usage

See the ./scripts folder for examples how the package's functions can be imported and called upon.

One script provided  is an interactive foo calculator can be ran command line.
To use this interactive calculator script, from the /Foo directory of this repo, run:
``` python3 .\scripts\ineteractive_foo_calc.py ```

## IMPORTANT *Note on usage*

The ./scripts and the ./tests files have lines of code at the top for the file that say:

```python
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
```

which are there to mimick the behavior of when script is being run in the proper package context. Those lines  ensure that the script can locate the parent package directory to import the modules correctly.

To use foo package in a proper package context, you would need to modify the sys.path to be similar to above by doing:

```python
import sys
import os

# add the ABSOLUTE path of the package to the package directory in sys.path
sys.path.append("/path/to/foo_package")

# now you can use the foo package modules like so
from foo import sphereVolume
```

OR another way to quickly use the functions is to add the foo package directory to your PYTHONPATH. If using Windows, add/edit the System Variable PYTHONPATH from the Windows GUI (My Computer > Properties > Advanced System Settings > Environment Variables) and set it to your path to foo_package. If using Linux, use the bash command:

```bash
PYTHONPATH=/path/to/foo_package:$PYTHONPATH
```

Once it's added, you can call from the Python shell like so:

```bash
> python3
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import foo
>>> foo.sphereVolume(2)
33.510321638291124
>>>
```

See [this article](https://stackoverflow.com/questions/16981921/relative-imports-in-python-3) for more info on the relative pathing.

## Testing and further work

Further additions to the foo physics parameterization can be expanded in the calc_functions.py file or by adding new files. Be sure to add anymore new functions to the import in the \_\_init\_\_.py file so they get initialized.

For testing these functions, the ./tests folder contains unit tests for the functions. More tests can be added as more Foo physics additions are made.

To run unit tests for the sphere functions, from the /Foo dir, run:
```python3 .\tests\test_sphere_calc_unittest.py```

If all tests ran correctly, the expected result should show "OK".

## References

As a refresher for how python packages are built, [this tutorial link](https://www.tutorialspoint.com/python/python_packages.htm) was used and can be used whenever developers want to add new science features.

For the interactive calculaor script, [this article](https://www.geeksforgeeks.org/make-simple-calculator-using-python/) was used for inspiration.

The unit testing reference used for the basics was [here](https://realpython.com/python-testing/).

[This post](https://stackoverflow.com/questions/16981921/relative-imports-in-python-3) about relative paths for referencing the package in scripts was helpful for understanding why you can't just import from scripts within the package.
