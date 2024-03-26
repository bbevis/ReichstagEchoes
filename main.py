
import pandas as pd
from googletrans import Translator
import json

import os
print(os.getcwd())
# Load JSON data
with open('..../Data/german_reichstag_sample_30.json', 'r') as file:
    data = json.load(file)