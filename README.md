# Spotify Datascraping Project






# Inspiration

Scrolling through the people that follow me on Spotify, I came across these accounts with seemingly the same username; all of who follow more than 100k users each. It didn't take me long to realise these may be data scraping bots that utilize the spotify data for their own projects.

![image](https://github.com/asymysh/Spotify-Datascraping/assets/33717548/442814a7-8b2f-476a-9896-ad052d5c8f9c)

# Usage

To use this API, you need to get a web player access token, not a regular API access token, so you can't use the official API way of logging in, getting and refreshing tokens.
The good news is that if you don't mind logging in on the web player and refreshing a value in your code once a year, it's actually quite easier than the official OAuth way. 


## sp_dc Cookie
This is the only value that you need for this to work. After you login on the web player(https://open.spotify.com/), you get a bunch of cookies, including one named sp_dc.
Seems like it's valid for one year, and with just that value you can call anytime an endpoint that gives you a refreshed, elevated API access token, that, unlike the official API ones, will let you query the undocumented endpoint that retrieves the friend activity.

Should your script run more than the token response's accessTokenExpirationTimestampMs (currently an hour), I would suggest implementing token refresh logic which is just calling getWebAccessToken and setAccessToken again like above. 
In my code, I get a new web access token every iteration so it becomes quite unneccesary to look for edge cases.


### 1. Fetching the cookie
You'll need to grab your sp_dc cookie from Spotify. This is a requirement because Spotify doesn't allow third-party apps to get the friend activity feed, so this cookie allows us to pretend that we're the Spotify app itself to get access to that data.
For that, login on the web player(https://open.spotify.com/) and open your browser's web developer tools. It's usually in "settings", "more tools", "developer tools". In that pane, go in "application", "storage", "cookies", https://open.spotify.com (or something close to that depending on your browser).

You'll find a cookie named sp_dc. Copy its value.


### 2. Insert the cookie in a file named token 

### 3. Run the script
