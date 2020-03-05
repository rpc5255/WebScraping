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


if __name__ == "__main__":
    main()
