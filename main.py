import requests
import pandas as pd
from datetime import datetime
import json
import os
from pathlib import Path
import pickle

BASE = "https://api.henleypassportindex.com/"
CACHE_FILE = "passport_data_cache.json"
DF_CACHE_FILE = "passport_df_cache.pkl"
CACHE_EXPIRY_DAYS = 7

def get_passport_data(cache_file: str = CACHE_FILE):
    """Get passport data from cache or API."""
    if not os.path.exists(cache_file):
        return None
    
    cache_time = os.path.getmtime(cache_file)
    current_time = datetime.now().timestamp()
    if (current_time - cache_time) > (CACHE_EXPIRY_DAYS * 24 * 60 * 60):
        return None
    
    try:
        with open(cache_file, 'r') as f:
            return json.load(f)
    except:
        return None

def save_passport_data(data, cache_file: str = CACHE_FILE):
    """Save passport data to cache."""
    with open(cache_file, 'w') as f:
        json.dump(data, f)

def henley_passport_index(code, base: str = BASE):
    """Returns the HP index score and list of countries with visa-free access for a given country code."""
    try:
        res = requests.get(f'{base}/api/passports/{code}/countries')
        countries_data = res.json()['default']
        countries = [country['name'] for country in countries_data if country.get('pivot', {}).get('is_visa_free') == 1]
        visa_free_count = len(countries)
        return visa_free_count, countries
    except Exception as e:
        print(f"Error getting visa-free count for {code}: {e}")
        return 0, []

def build_passport_dataframe(base: str = BASE):
    """Build and return a DataFrame containing passport power rankings."""
    data = get_passport_data(base)
    if data is None:
        res = requests.get(f'{base}/api/passports')
        data = res.json()
        save_passport_data(data)

    # First build DataFrame with just HP indices
    df_data = []
    for passport in sorted(data, key=lambda x: x['name']):
        hp_index, countries = henley_passport_index(passport['code'], base)
        df_data.append({
            'country_name': passport['name'],
            'country_code': passport['code'],
            'hp_index': hp_index,
            'countries': countries
        })
    
    df = pd.DataFrame(df_data)
    
    return df

def hp_index_df(base: str = BASE, cache_file: str = DF_CACHE_FILE) -> pd.DataFrame:
    """Get passport power rankings DataFrame from cache or build it if needed."""
    if os.path.exists(cache_file):
        cache_time = os.path.getmtime(cache_file)
        current_time = datetime.now().timestamp()
        if (current_time - cache_time) <= (CACHE_EXPIRY_DAYS * 24 * 60 * 60):
            with open(cache_file, 'rb') as f:
                return pickle.load(f)
    
    df = build_passport_dataframe(base)
    with open(cache_file, 'wb') as f:
        pickle.dump(df, f)
    return df

def add_strength_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Add strength columns for both HP and BS indices."""
    df_sorted = df.sort_values('hp_index', ascending=False)
    df_sorted['hp_strength'] = range(1, len(df_sorted) + 1)
 
    return df_sorted

def add_bsp(df: pd.DataFrame) -> pd.DataFrame:
    total_countries = len(df)
    df['bsp_weight'] = df['hp_index'] / total_countries

    country_to_weight = dict(zip(df['country_name'], df['bsp_weight']))
    df['bsp_index'] = df['countries'].apply(lambda countries: sum(country_to_weight.get(country, 0) for country in countries))

    df = df.sort_values('bsp_index', ascending=False)
    df['bsp_strength'] = range(1, len(df) + 1)

    df['bsp_strength_diff'] = df['hp_strength'] - df['bsp_strength']

    return df

df = hp_index_df()
df = add_strength_columns(df)
df = add_bsp(df)

print("\nPassport Power Rankings:")


df = df[df['bsp_strength_diff'] != 0][['country_name', 'hp_strength', 'bsp_strength', 'bsp_strength_diff']]
df = df.sort_values('bsp_strength_diff', ascending=False)
print(df.to_string(index=False))

print("\nStats on the difference in the HP and BSP index scores:")
print(df['bsp_strength_diff'].describe())

