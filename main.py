import instaloader

L = instaloader.Instaloader(download_video_thumbnails=False, request_timeout=30, download_pictures=False) 
 

headers = {
        'User-Agent': 'curl/7.64.1'
    }

x = L.context._session.get("http://ifconfig.me",headers=headers)

print(f"STARTIN UP MyIP {x.content}")

L.login("login", "pass")  

user = "snoopdogg"

# Obtain profile metadata 
profile = instaloader.Profile.from_username(L.context, user) 
 
# Print list of followers
with open(f'./data/{user}_followers.txt', 'a') as f:
     for followee in profile.get_followers(): 
     #for followee in profile.get_followees(): 
          username = followee.username 
          print(username)
          f.write(f"{username}\n")