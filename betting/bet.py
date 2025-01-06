import requests
from bs4 import BeautifulSoup
from colorama import Fore,init
import os

init(autoreset=True)


def pull_team_information(team):
    clear_screen()

    url = f"https://www.sporx.com/{team}-fiksturu-ve-mac-sonuclari"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table containing team information
    matches = soup.find_all("tr")
    winner_count = 0
    total_goals = 0
    last_match_score = None
    for match in matches:
        score_element = match.find("a",class_="d-block rounded bg-sporx text-white fw-bolder py-1 px-1 text-nowrap")
        if score_element:
            score = score_element.get_text(strip=True)
            goals_count = score.split("-")
            if len(goals_count) == 2 and goals_count[0].strip() and goals_count[1].strip():
                try:
                    goal_scored = int(goals_count[0].strip())
                    number_goal2 = int(goals_count[1].strip())
                except ValueError:
                    goal_scored = None
                    number_goal2 = None
                if goal_scored is not None and number_goal2 is not None:
                    home = match.find("td",class_ = "text-start w-25").find("a").get_text(strip=True)
                    away = match.find("td",class_ = "text-end w-25").find("a").get_text(strip=True)
                    if team.lower() == turkish_characters_change(home.lower()):
                        total_goals += goal_scored
                        if goal_scored > number_goal2:
                            winner_count += 1
                        last_match_score = f"Last Match: {home} {score} "
                    elif team.lower() == turkish_characters_change(away.lower()):
                        total_goals += number_goal2
                        if goal_scored < number_goal2:
                            winner_count += 1
                        last_match_score = f"Last Match: {home} {score} {away}"
    if winner_count == 0:
        print(Fore.RED + team.capitalize())
        return None, None, None
    else:
        return winner_count,total_goals,last_match_score


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def turkish_characters_change(team_name):
    team_name = team_name.replace("ı","i")
    team_name = team_name.replace("ç","c")
    team_name = team_name.replace("ş","s")
    team_name = team_name.replace("ğ","g")
    team_name = team_name.replace("ü","u")
    return team_name


def last_match_information_pull(team):
     url = f"https://www.sporx.com/{team}-fiksturu-ve-mac-sonuclari"
     response = requests.get(url)
     soup = BeautifulSoup(response.content,"html.parser")
     matches = soup.find_all("tr")
     last_10_match_goal_count = []
     match_sayac = 0

     for match in matches:
         score_element = match.find("a", class_="d-block rounded bg-sporx text-white fw-bolder py-1 px-1 text-nowrap")
         if score_element:
             score = score_element.get_text(strip=True)
             goals_count = score.split("-")
             if len(goals_count) == 2 and goals_count[0].strip() and goals_count[1].strip():
                        try:
                            gol_sayisi_g1 = int(goals_count[0])
                            gol_sayisi_g2 = int(goals_count[1])
                            last_10_match_goal_count.append(gol_sayisi_g1)
                            last_10_match_goal_count.append(gol_sayisi_g2)
                            match_sayac +=1
                        except ValueError:
                              continue
                        if match_sayac >= 7:     
                              break
                        return last_10_match_goal_count    

def two_team_analytic(team1,team2):
    clear_screen()

    conclusion = f"{team1.capitalize()} vs {team2.capitalize()}"
    conclusion = f"--------------------------------------------\n"

    #team1 information
    team1_information_pull = pull_team_information(team1)
    if team1_information_pull is None:
        return 
    winner_count_g1, goal_count_g1, last_match_g1 = team1_information_pull


    #team2 information
    team2_information_pull = pull_team_information(team2)
    if team2_information_pull is None:
        return 
    winner_count_g2, goal_count_g2, last_match_g2 = team2_information_pull

    conclusion += f"{team1}\nWinner Count : {winner_count_g1}\n Goal Count : {goal_count_g1}\n Last Match : {last_match_g1}"

    conclusion += f"{team2}\nWinner Count : {winner_count_g2}\n Goal Count : {goal_count_g2}\n Last Match : {last_match_g2}"

    if winner_count_g1 is not None and winner_count_g2 is not None:
        if winner_count_g1 > winner_count_g2:
            conclusion += f"{Fore.GREEN} {team1.capitalize()} is the winner!"
        elif winner_count_g1 < winner_count_g2:
            conclusion += f"{Fore.GREEN} {team2.capitalize()} is the winner!"
        else:
            conclusion += f"{Fore.YELLOW} Both teams have same winning count!"
    else:
        conclusion += f"{Fore.RED} Not enough data to compare teams!"
    
    if winner_count_g1 is not None and winner_count_g2 is not None:
        team1_last_match_5 = last_match_information_pull(team1)
        team2_last_match_5 = last_match_information_pull(team2)

        if len(team1_last_match_5) < 7 or len(team2_last_match_5) < 7:
            print(Fore.RED + "data is not found !!")
        
        average_goals_team1 = sum(team1_last_match_5) / len(team1_last_match_5)
        average_goals_team2 = sum(team2_last_match_5) / len(team2_last_match_5)


        average_goal = (average_goals_team1+average_goals_team2)/2
        goal_guess = average_goal + 0.25 if team1_last_match_5[-1] > team2_last_match_5[-1] else average_goal

        conclusion += f"{Fore.GREEN} Average Goals : {average_goal:.2f}\nExpected Goals : {goal_guess:.2f}"
    
        
    print(conclusion)
    print("--------------------------------------------")



while True:
    team1 = input("Enter the first team name: ")
    team2 = input("Enter the second team name: ")
    two_team_analytic(team1, team2)
    continues = input("continue")
    if continues.lower() != "y":
        break