import datetime
import json
import re

import os
import requests
import wget
from bs4 import BeautifulSoup as soup
from pprint import pprint
import xml.etree.ElementTree as et
import time
from concurrent.futures import ThreadPoolExecutor

for i in range(0,4,2):
    print(i)