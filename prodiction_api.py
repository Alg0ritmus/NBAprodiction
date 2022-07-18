from timeit import default_timer as timer
import sys
import os
import json



# pridaj cestu na uspesny import medzi-suborov 
sys.path.append(os.path.join(os.path.dirname(__file__), "Analyze_traffic"))

from Analyze_traffic.math_model import *



#SEASONS = ["2021-22","2020-21","2019-20"]
SEASONS = ["2020-21","2020-21","2020-21"]

# FILL CONST.
#with open("./static_data/playersInTeam.json","r") as f:
#    data = f.read()
#
#data = json.loads(data)
#
#for i in data:
#    print(i["players"])


# write down Teams with abbr
def getTeamList():
    with open("./static_data/teams.json","r") as f:
        data = f.read()
    data = json.loads(data)

    for i in data:
        print("Abbr: {} | Name: {}".format(i["abbreviation"],i["teamName"]))

# get teamID from abbr
def getTeamId(abbr):
    with open("./static_data/teams.json","r") as f:
        data = f.read()
    data = json.loads(data)
    for team in data:
        if team["abbreviation"] == abbr:
            return team["teamId"]

# get All players from Team
def getTeamWithPlayers(TeamID):
    with open("./static_data/playersInTeam.json","r") as f:
        data = f. read()
    data = json.loads(data)
    team_and_players = data

    for team_and_players_info in team_and_players:
        if team_and_players_info["teamId"] == TeamID:
            return(team_and_players_info["players"])



def TeamVsTeam(TEAM_1, TEAM_2):
    TEAM_1_ID = getTeamId(TEAM_1)
    TEAM_2_ID = getTeamId(TEAM_2)

    # GET TEAM GENERAL STATS FOR 3 PREV SEASONS
    print("TEAM_1_Stats")
    start1 = timer()
    TEAM_1_Stats = (getTeamStats(my_Season=SEASONS[0],my_TeamID=str(TEAM_1_ID))+getTeamStats(my_Season=SEASONS[1],my_TeamID=str(TEAM_1_ID))+getTeamStats(my_Season=SEASONS[2],my_TeamID=str(TEAM_1_ID)))/3
    end1 = timer()
    print(end1-start1)

    print("TEAM_2_Stats")
    start2 = timer()
    TEAM_2_Stats = (getTeamStats(my_Season=SEASONS[0],my_TeamID=str(TEAM_2_ID))+getTeamStats(my_Season=SEASONS[1],my_TeamID=str(TEAM_2_ID))+getTeamStats(my_Season=SEASONS[2],my_TeamID=str(TEAM_2_ID)))/3
    end2 = timer()
    print(end2-start2)

    TEAM_1_Players_Stats = 0
    TEAM_2_Players_Stats = 0

    # GET PLAYERS GENERAL STATS FOR SEASONS 2021-22 (UNFINNISHED - do for all 3 seasons)
    print("TEAM_1_Players_Stats")
    start3 = timer()
    for player in getTeamWithPlayers(TEAM_1_ID):
        print("playerIn1")
        TEAM_1_Players_Stats = getPlayerStats_for_math(str(player))
    end3 = timer()
    print(end3-start3)
    print("TEAM_2_Players_Stats")
    start4 = timer()
    for player in getTeamWithPlayers(TEAM_2_ID):
        print("playerIn2")
        TEAM_2_Players_Stats = getPlayerStats_for_math(str(player))
    end4 = timer()
    print(end4-start4)
    # GET TEAM VS TEAM GENERAL STATS FOR 3 PREV SEASONS
    print("TEAM_VS_TEAM")
    start5 =timer()
    TEAM_VS_TEAM = (getTeamVsTeamStats(my_Season=str(SEASONS[0]),my_TeamID=str(TEAM_1_ID),my_opponent_TeamID=str(TEAM_2_ID))+getTeamVsTeamStats(my_Season=str(SEASONS[1]),my_TeamID=str(TEAM_1_ID),my_opponent_TeamID=str(TEAM_2_ID))+getTeamVsTeamStats(my_Season=str(SEASONS[2]),my_TeamID=str(TEAM_1_ID),my_opponent_TeamID=str(TEAM_2_ID)))/3
    end5 =timer()
    print(end5-start5)
    RESULTS = (TEAM_1_Stats+TEAM_1_Players_Stats+TEAM_VS_TEAM)/(TEAM_2_Stats+TEAM_2_Players_Stats+(1/TEAM_VS_TEAM))
    return RESULTS

getTeamList()
TEAM1ABBR = input("Pass Team 1 abbr: ")
TEAM2ABBR = input("Pass op. Team 1 abbr: ")
print(TeamVsTeam(TEAM1ABBR,TEAM2ABBR))


#sys.argv
