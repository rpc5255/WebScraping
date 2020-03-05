from urllib.request import urlopen
from bs4 import BeautifulSoup, Comment
import pandas as pd
import re

def get_team_stats_soup():
    url = "https://www.basketball-reference.com/leagues/NBA_2020.html"
    html = urlopen(url)
    soup = BeautifulSoup(html, "html5lib")
    team_stats_tables = "".join(soup.find_all(string=lambda text: isinstance(text, Comment)))
    return BeautifulSoup(team_stats_tables, "html5lib")


def get_stats_df(team_stats_soup, id):
    id_table = team_stats_soup.find_all("table", id=id)

    headers_result_set = id_table[0].find_all("th", {"aria-label": True, "class": re.compile('.*poptip.*')})
    headers = [th.text for th in headers_result_set][1:]

    data_rows = id_table[0].find_all("tr")[1:]
    data_result_set = [td.find_all("td") for td in data_rows]
    data = [[feature.text.replace("*", "") for feature in record] for record in data_result_set]
    return pd.DataFrame(data, columns=headers).dropna().reset_index(drop=True)


def get_team_stats_per_game(team_stats_soup):
    return get_stats_df(team_stats_soup, "team-stats-per_game")


def get_opponent_stats_per_game(team_stats_soup):
    return get_stats_df(team_stats_soup, "opponent-stats-per_game")


def get_season_team_stats(team_stats_soup):
    return get_stats_df(team_stats_soup, "team-stats-base")


def get_season_opponent_stats(team_stats_soup):
    return get_stats_df(team_stats_soup, "opponent-stats-base")


def get_team_stats_per_100_poss(team_stats_soup):
    return get_stats_df(team_stats_soup, "team-stats-per_poss")


def get_opponent_stats_per_100_poss(team_stats_soup):
    return get_stats_df(team_stats_soup, "opponent-stats-per_poss")


def get_miscellaneous_stats(team_stats_soup):
    return get_stats_df(team_stats_soup, "misc_stats")


def get_team_shooting_stats(team_stats_soup):
    return get_stats_df(team_stats_soup, "team_shooting")


def get_opponent_shooting_stats(team_stats_soup):
    return get_stats_df(team_stats_soup, "opponent_shooting")
