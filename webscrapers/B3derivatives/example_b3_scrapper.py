import pandas as pd
from webscrapers import ScraperB3

b3 = ScraperB3()

df = b3.scrape('DI1', pd.to_datetime('2018-08-01'), pd.to_datetime('2018-08-10'))

print(df)
