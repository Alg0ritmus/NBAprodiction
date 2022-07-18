import json 
import http.client
import gzip

cookies='ak_bmsc=DB38F9E9A3DBFFBCD22CA3071CBF2D15~000000000000000000000000000000~YAAQn3EGFyBjBfuAAQAAYazeDw+S1GevK2IRU2TyQQt36zjESsEdxRdjElKMJqa9w67m/mOKNsUoxYChBPjwsdb2F7HfiwC1dvdfh8VI7AxbYX0JUldj1lNKQFEEiR8SXarDlGzXpiDI+gDL2ib5349bEQ8+T8/aqJOMZgCj3O4khKoT6YwVO/nbFSTEQIbTsE8dlluNJDAdGYrSb2yD9RxMMh//vXDRxRQigoP8ysRFm23lCyPLlkF3eLDRTGE+xZNTHMCEjR3pxrAO41OcZAQQeGD3whvX5Q/XD9v2bDBMY4EmRVucjyPDYH3ZrBitl+iqwGoUAqOViZ/Nymqzih3KiWJZx3TM++hIW2UwDVrNq1qjYqSRwkWgOg=='

def getBasicTeamData(my_Season="2020-21",my_TeamID="1610612737"):
    conn = http.client.HTTPSConnection("stats.nba.com")
    payload = ''
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'sk',
        'Connection': 'keep-alive',
        'Host': 'stats.nba.com',
        'Origin': 'https://www.nba.com',
        'Referer': 'https://www.nba.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-nba-stats-origin': 'stats',
        'x-nba-stats-token': 'true'
    }
    conn.request("GET", "/stats/teamdashboardbygeneralsplits?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlusMinus=N&Rank=N&Season="+my_Season+"&SeasonSegment=&SeasonType=Playoffs&ShotClockRange=&Split=general&TeamID="+my_TeamID+"&VsConference=&VsDivision=", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data= gzip.decompress(data)
    print(data,"NBA_STATS")
    return(json.loads(json.dumps(data.decode("utf-8"))))



def getBasicTeamVsTeamData(my_Season="2020-21",my_TeamID="1610612737",my_opponent_TeamID="1610612766"):
    conn = http.client.HTTPSConnection("stats.nba.com")
    payload = ''
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'sk',
        'Connection': 'keep-alive',
        'Host': 'stats.nba.com',
        'Origin': 'https://www.nba.com',
        'Referer': 'https://www.nba.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-nba-stats-origin': 'stats',
        'x-nba-stats-token': 'true'
    }
    conn.request("GET", "/stats/teamdashboardbygeneralsplits?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID="+my_opponent_TeamID+"&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlusMinus=N&Rank=N&Season="+my_Season+"&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&Split=general&TeamID="+my_TeamID+"&VsConference=&VsDivision=", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data= gzip.decompress(data)
    print(data,"NBA_STATS")
    return(json.loads(json.dumps(data.decode("utf-8"))))


def getPlayerStats(playerID='1630173'):
    conn = http.client.HTTPSConnection("stats.nba.com")
    payload = ''
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'sk',
        'Connection': 'keep-alive',
        'Host': 'stats.nba.com',
        'Origin': 'https://www.nba.com',
        'Referer': 'https://www.nba.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-nba-stats-origin': 'stats',
        'x-nba-stats-token': 'true'
    }
    conn.request("GET", "/stats/playerdashboardbyyearoveryearcombined?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID="+playerID+"&PlusMinus=N&Rank=N&Season=2021-22&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&VsConference=&VsDivision=", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data= gzip.decompress(data)
    print(data,"NBA_STATS")
    return(json.loads(json.dumps(data.decode("utf-8"))))
