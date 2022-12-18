import pandas as pd

def get_data(link: str) -> pd.DataFrame:
    """
    This function extract data from the link
    """
    return pd.read_csv(link)