# How to install

- Go into **__init__.py** and change the PACKAGE_DIRECTORY to your directory for your local packages.

- Install package_loader by running `pip install -e <directory_of_package_loader>`

- Import packages by using it like this:

### Method 1 (Recursive Importing)
```py
import package_loader as loader

utils = loader.import_("utilities").libs.colors

print(utils.red("hi"))
```
### Method 2 (Static Importing)

```py
import package_loader as loader

utils = loader.import_("utilities")

print(utils.libs.colors.red("hi"))
```

### The package directory has to have folders layed out like this:

```
PackageDir/
|-- Testing Package 1/
|   |-- tests.py
|   |-- whatever.md
|   |-- testing_package/
|   |   |-- whatever/
|   |   |   |-- whatever.wtv
|   |   |-- __init__.py
|-- Testing Package 2/
|   |-- tests.py
|   |-- whatever.md
|   |-- testing_package_2/
|   |   |-- whatever/
|   |   |   |-- whatever.wtv
|   |   |-- __init__.py
```
`testing_packge` and `testing_package_2` are the names of the packages, and `__init__.py` is what will be loaded when imported.
