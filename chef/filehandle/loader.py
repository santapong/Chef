import os, sys
sys.path.append("/".join(os.getcwd(),"chef"))

# Use to import file
import importlib.util
import shutil

# logging config
import logging
from logging.config import Formatter
from logging.handlers import RotatingFileHandler

# import config.py
from chef.config import ZIPFILEPATH

#TODO: This file need to load zip file form user

import shutil

# Define the source and destination paths
source_path = ZIPFILEPATH
destination_path = ''

# Move the file
shutil.move(source_path, destination_path)

print(f"File moved from {source_path} to {destination_path}")
