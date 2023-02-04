#import sys

#locate_python = sys.exec_prefix
#print(locate_python)

import os

# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))