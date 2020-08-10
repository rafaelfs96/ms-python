# import a module as namespace
import helpers
helpers.display(message='This is a message')

# import all into current namespace
from helpers import *
display(message='This is another message')

# import specific items into current namespace
from helpers import display
display(message='This is yet another message', is_warning=True)


# To install an individual package
# pip install package_name

# To install from a list of packages
# pip install -r requirements.txt