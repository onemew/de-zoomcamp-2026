import pandas as pd
from sqlalchemy import create_engine


ZONES_DATA = "taxi_zone_lookup.csv"

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
df_zones = pd.read_csv(ZONES_DATA)
df_zones.to_sql(name='zones', con=engine, if_exists='replace')
