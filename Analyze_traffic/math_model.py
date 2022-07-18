# P.Z. (PTS + 3P% + FT% + REB + AST + BLK + +/-) : (MIN . GP)
# check right values by headers
# headers[27],headers[13],headers[16],headers[19],headers[20],headers[23],headers[28],"/",headers[7],headers[3]
import json
import nba_stats as stats



#TO DO add Win/Lose ratio to Team stats

# TEAM STATS
def getTeamStats(my_Season,my_TeamID):
    print("mathmode - fetch data")
    data = json.loads(stats.getBasicTeamData(my_Season,my_TeamID))
    print("mathmode - got data")
    headers= data["resultSets"][0]["headers"]
    values= data["resultSets"][0]["rowSet"]
    if values == []:
        return 0
    #print just for check if there is update in nba.com backend
    #print(headers[27],headers[13],headers[16],headers[19],headers[20],headers[23],headers[28],"/",headers[7],headers[3])
    OVERALL_STATS = ((values[0][27]+values[0][13]+values[0][16]+values[0][19]+values[0][20]+values[0][23]+values[0][28])/(values[0][7]*values[0][3]))
    return OVERALL_STATS

# TEAM VS TEAM STATS
def getTeamVsTeamStats(my_Season,my_TeamID,my_opponent_TeamID):
    print("mathmode - fetch data")
    data = json.loads(stats.getBasicTeamVsTeamData(my_Season,my_TeamID,my_opponent_TeamID))
    print("mathmode - got data")
    headers= data["resultSets"][0]["headers"]
    values= data["resultSets"][0]["rowSet"]
    if values == []:
        return 0
    #print just for check if there is update in nba.com backend
    #print(headers[27],headers[13],headers[16],headers[19],headers[20],headers[23],headers[28],"/",headers[7],headers[3])
    OVERALL_TEAM_VS_TEAM_STATS = ((values[0][27]+values[0][13]+values[0][16]+values[0][19]+values[0][20]+values[0][23]+values[0][28])/(values[0][7]*values[0][3]))
    return OVERALL_TEAM_VS_TEAM_STATS


# PLAYER STATS
def getPlayerStats_for_math(playerID):
    print("mathmode - fetch data")
    data = json.loads(stats.getPlayerStats(playerID))
    print("mathmode - got data")
    headers= data["resultSets"][0]["headers"]
    values= data["resultSets"][0]["rowSet"]
    if values == []:
        return 0
    #print just for check if there is update in nba.com backend
    #print(headers[29],headers[15],headers[18],headers[21],headers[22],headers[25],headers[30],"/",headers[9],headers[5])
    OVERALL_PLAYER_STATS = ((values[0][29]+values[0][15]+values[0][18]+values[0][21]+values[0][22]+values[0][25]+values[0][30])/(values[0][9]*values[0][5]))
    return OVERALL_PLAYER_STATS

# CHECK STRUCTURE
#for i in range(len(headers)):
#    print("{} {:20} = {:4}".format(i,headers[i],values[0][i]))
#




