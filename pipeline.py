import pandas as pd
from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load

df = extract()
df = transform(df)
load(df)