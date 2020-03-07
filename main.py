import basketball_reference_scraper


def main():
    team_stats_soup = basketball_reference_scraper.get_team_stats_soup()
    basketball_reference_scraper.get_team_stats_per_game(team_stats_soup)
    basketball_reference_scraper.get_opponent_stats_per_game(team_stats_soup)
    basketball_reference_scraper.get_team_stats_per_100_poss(team_stats_soup)
    basketball_reference_scraper.get_opponent_stats_per_100_poss(team_stats_soup)
    basketball_reference_scraper.get_miscellaneous_stats(team_stats_soup)
    basketball_reference_scraper.get_team_shooting_stats(team_stats_soup)
    basketball_reference_scraper.get_opponent_shooting_stats(team_stats_soup)

client = pymongo.MongoClient("mongodb+srv://David:david123@cluster0-lu6oi.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


if __name__ == "__main__":
    main()
