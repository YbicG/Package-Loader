import os
from importlib.machinery import SourceFileLoader

PACKAGE_DIRECTORY = "C:\\Users\\djcoo\\Documents\\Main Documents\\Code\\Packages\\Python"
"""
### The package directory has to have folders layed out like this:

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

`testing_packge` and `testing_package_2` are the names of the packages, and `__init__.py` is what will be loaded when imported.
"""

package_dict = {}

for folder_name in os.listdir(PACKAGE_DIRECTORY):
    folder_path = os.path.join(PACKAGE_DIRECTORY, folder_name)

    if os.path.isdir(folder_path):

        for sub_folder_name in os.listdir(folder_path):
            sub_folder_path = os.path.join(folder_path, sub_folder_name)
            
            if os.path.isdir(sub_folder_path) and "__init__.py" in os.listdir(sub_folder_path):
                package_dict[sub_folder_name] = os.path.join(sub_folder_path, "__init__.py")
                
def import_(package_name: str):
    if package_name.lower() in package_dict:
        package_path = package_dict[package_name]
        loc = {}
        
        exec(f"""{package_name} = SourceFileLoader("{package_name}", r"{package_path}").load_module()""", globals(), loc)
        
        return loc[package_name]

def get_package_list():
    print("\n\n")
    index = 0
    for key in package_dict.keys():
        index += 1
        print(f"{str(index)}) {key.title()} - {package_dict[key]}")