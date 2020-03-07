from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


def get_team_schedule(team):
    url = f"https://www.basketball-reference.com/teams/{team}/2020_games.html"
    html = urlopen(url)
    team_schedule_soup = BeautifulSoup(html, "html5lib")

    headers_result_set = team_schedule_soup.find("tr").find_all("th")
    headers = [th.text for th in headers_result_set][1:]
    headers[4], headers[6] = "Location", "Result"

    data_rows = team_schedule_soup.find_all("tr")
    data_result_set = [td.find_all("td") for td in data_rows]
    data = [[feature.text for feature in record] for record in data_result_set]

    df = pd.DataFrame(data, columns=headers)
    df = df.drop(df.columns[[2, 3, 7, 13]], axis=1).reset_index(drop=True)
    df['Result'].replace('', np.nan, inplace=True)
    df = df.dropna(subset=['Result']).reset_index(drop=True)

    return df
