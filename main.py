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
    """Returns the HP index score i.e. the number of countries with visa-free access for a given country code."""
    try:
        res = requests.get(f'{base}/api/passports/{code}/countries')
        countries_data = res.json()['default']
        visa_free_count = sum(1 for country in countries_data if country.get('pivot', {}).get('is_visa_free') == 1)
        return visa_free_count
    except Exception as e:
        print(f"Error getting visa-free count for {code}: {e}")
        return 0

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
        hp_index = henley_passport_index(passport['code'], base)
        df_data.append({
            'country_name': passport['name'],
            'country_code': passport['code'],
            'hp_index': hp_index
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


df = hp_index_df()
df_with_strength = add_strength_columns(df)
print("\nPassport Power Rankings:")
print(df_with_strength.head().to_string(index=False))


