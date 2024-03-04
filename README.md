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
