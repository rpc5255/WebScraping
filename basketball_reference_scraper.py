from urllib.request import urlopen
from bs4 import BeautifulSoup, Comment
import pandas as pd


def get_team_stats_soup_obj():
    url = "https://www.basketball-reference.com/leagues/NBA_2020.html"
    html = urlopen(url)
    soup = BeautifulSoup(html, "html5lib")
    team_stats_tables = "".join(soup.find_all(string=lambda text: isinstance(text, Comment)))
    return BeautifulSoup(team_stats_tables, "html5lib")


def get_team_stats_df(id):
    team_stats_table = get_team_stats_soup_obj()
    id_table = team_stats_table.find_all("table", id=id)

    headers_result_set = id_table[0].find_all("th", {"aria-label": True})
    headers = [th.text for th in headers_result_set][1:]

    data_rows = id_table[0].find_all("tr")[1:]
    data_result_set = [td.find_all("td") for td in data_rows]

    data = [[j.text.replace("*", "") for j in i] for i in data_result_set]
    return pd.DataFrame(data, columns=headers)


def get_team_stats_per_game():
    return get_team_stats_df("team-stats-per_game")
