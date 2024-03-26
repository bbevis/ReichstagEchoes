
import pandas as pd
import translators as ts
import json
from bertopic import BERTopic
from bertopic.representation import KeyBERTInspired

import os
print(os.getcwd())
# Load JSON data
with open('german_reichstag_sample_30.json', 'r') as file:
    df = pd.DataFrame(json.load(file))
    

print(df.shape)
text_eng = df['text'].apply(lambda x: ts.translate_text(x, translator='google', to_language='en'))

# Print translated DataFrame
# print(df)