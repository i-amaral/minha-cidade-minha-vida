"""Get data from IBGE API"""

import requests
import pandas as pd

def get_data(resource_url: str) -> pd.DataFrame:
    """Get data from API converted to pandas dataframe"""
    response = requests.get(resource_url, timeout=10)
    response.raise_for_status()
    return pd.json_normalize(response.json())
