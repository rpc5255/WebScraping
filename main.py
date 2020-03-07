import pymongo
import basketball_reference_scraper
import team_schedule_scraper


def main():

    season_stats_table_ids = ["team-stats-per_game", "opponent-stats-per_game", "team-stats-base",
                              "opponent-stats-base", "team-stats-per_poss", "opponent-stats-per_poss", "misc_stats",
                              "team_shooting", "opponent_shooting"]

    team_abbreviations = {"ATL": "Atlanta Hawks", "BKN": "Brooklyn Nets", "BOS": "Boston Celtics",
                          "CHA": "Charlotte Hornets", "CHI": "Chicago Bulls", "CLE": "Cleveland Cavaliers",
                          "DAL": "Dallas Mavericks", "DEN": "Denver Nuggets", "DET": "Detroit Pistons",
                          "GSW": "Golden State Warriors", "HOU": "Houston Rockets", "IND": "Indiana Pacers",
                          "LAC": "Los Angeles Clippers", "LAL": "Los Angeles Lakers", "MEM": "Memphis Grizzlies",
                          "MIA": "Miami Heat", "MIL": "Milwaukee Bucks", "MIN": "Minnesota Timberwolves",
                          "NOP": "New Orleans Pelicans", "NYK": "New York Knicks", "OKC": "Oklahoma City Thunder",
                          "ORL": "Orlando Magic", "PHI": "Philadelphia 76ers", "PHX": "Phoenix Suns",
                          "POR": "Portland Trail Blazers", "SAC": "Sacramento Kings", "SAS": "San Antonio Spurs",
                          "TOR": "Toronto Raptors", "UTA": "Utah Jazz", "WAS": "Washington Wizards"}

    client = pymongo.MongoClient("mongodb+srv://David:david123@cluster0-lu6oi.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test


if __name__ == "__main__":
    main()
