import requests
import json
import asyncio
import websockets

API_KEY = '366acba198d619b696bc0eef33081730'
BASE_URL = 'https://v3.football.api-sports.io'

HEADERS = {
    'x-apisports-key': API_KEY
}

def fetch_league_standings(league_id, season):
    url = f"{BASE_URL}/standings?league={league_id}&season={season}"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve league data. Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return None

def display_standings(standings_data):
    if standings_data and 'response' in standings_data:
        league_standings = standings_data['response'][0]['league']['standings'][0]
        print(f"{'Position':<10}{'Team':<30}{'Points':<10}{'Wins':<10}{'Losses':<10}")
        print("-" * 70)
        for team in league_standings:
            position = team['rank']
            name = team['team']['name']
            points = team['points']
            wins = team['all']['win']
            losses = team['all']['lose']
            print(f"{position:<10}{name:<30}{points:<10}{wins:<10}{losses:<10}")

def main():
    while True:
        print("---------------------------------------------------------")
        print("Welcome! Please select an option:")
        print("A. Leagues Standing")
        print("B. Exit")
        user_input = input("Please Choose an option (A/B): ").strip().upper()

        if user_input == "B":
            print("Program Closed! Have a Nice Day!")
            exit()

        elif user_input == "A":
            print("Select a League:")
            print("1. La Liga")
            print("2. Premier League")
            print("3. Bundesliga")
            print("4. Serie A")
            league_choice = input("Enter your choice (1-4): ").strip()

            league_ids = {
                '1': {'id': 140, 'name': 'La Liga', 'season': 2023},
                '2': {'id': 39, 'name': 'Premier League', 'season': 2023},
                '3': {'id': 78, 'name': 'Bundesliga', 'season': 2023},
                '4': {'id': 135, 'name': 'Serie A', 'season': 2023}
            }

            league_info = league_ids.get(league_choice)

            if league_info:
                league_data = fetch_league_standings(league_info['id'], league_info['season'])
                display_standings(league_data)
            else:
                print("Invalid choice. Please try again.")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()