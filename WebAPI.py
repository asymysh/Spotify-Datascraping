import requests
import json
from unidecode import unidecode
from DBHelper import SpotifyActivityDB


def get_web_access_token(cookie):
    url = "https://open.spotify.com/get_access_token?reason=transport&productType=web_player"
    headers = {"Cookie": f"sp_dc={cookie}"}
    response = requests.get(url, headers=headers)
    print(response) #DEBUG
    data = response.json()
    return data

def get_friend_activity(web_access_token):
    access_token = web_access_token["accessToken"]
    url = "https://guc-spclient.spotify.com/presence-view/v1/buddylist"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data


def get_cookie(n):
    with open('token','r') as file:
        tok = file.readlines()
    try:
        return tok[n-1].strip(" \"\n")
    except:
        return None

def write_to_database(db, friends_activity):
    for data in friends_activity['friends']:
        # Extract relevant information from the JSON data
        timestamp = data['timestamp']
        spotify_user_uri = unidecode(data['user']['uri'].split(':')[-1])
        spotify_track_uri = data['track']['uri'].split(':')[-1]
        spotify_context_uri = data['track']['context']['uri'].split(':')[-1]
        
        datapoint = (spotify_user_uri,spotify_track_uri,spotify_context_uri,timestamp)
        db.insert_datapoint(datapoint)
    db.commit()


if __name__ == "__main__":

    cookie = get_cookie(1)
    web_access_token = get_web_access_token(cookie)
    friends_activity = get_friend_activity(web_access_token)
    db = SpotifyActivityDB()
    write_to_database(db, friends_activity)
    