# __init__.py
# Code here runs when the package is imported
print("Initializing my_package")

# You can define package-level variables or imports
__version__ = "1.0.1"

# Import modules for easier access
from my_package.tubePack.youtube import tubePlay,tubeSearch,tubeStart
from my_package.Extractors.extract import extractnum,extractsearch,classify,ytclassify
from my_package.quotes.quote import quote_gen