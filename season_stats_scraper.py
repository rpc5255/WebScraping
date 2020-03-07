from urllib.request import urlopen
from bs4 import BeautifulSoup, Comment
import pandas as pd
import re


def get_season_stats_soup():
    url = "https://www.basketball-reference.com/leagues/NBA_2020.html"
    html = urlopen(url)
    soup = BeautifulSoup(html, "html5lib")
    season_stats_tables = "".join(soup.find_all(string=lambda text: isinstance(text, Comment)))
    return BeautifulSoup(season_stats_tables, "html5lib")


def get_season_stats_df(season_stats_soup, id):
    id_table = season_stats_soup.find_all("table", id=id)

    headers_result_set = id_table[0].find_all("th", {"aria-label": True, "class": re.compile('.*poptip.*')})
    headers = [th.text for th in headers_result_set][1:]

    data_rows = id_table[0].find_all("tr")[1:]
    data_result_set = [td.find_all("td") for td in data_rows]
    data = [[feature.text.replace("*", "") for feature in record] for record in data_result_set]

    df = pd.DataFrame(data, columns=headers)
    df = df.dropna().reset_index(drop=True)

    return df
