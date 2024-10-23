import os

from dotenv import load_dotenv
load_dotenv()

ZIPFILEPATH = os.getenv("ZIPFILEPATH") if os.getenv("ZIPFILEPATH") else ''