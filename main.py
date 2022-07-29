import instaloader

L = instaloader.Instaloader(download_video_thumbnails=False, request_timeout=30, download_pictures=False) 

# Show me public ip to see if tor works correctly 
headers = { 'User-Agent': 'curl/7.64.1' }
x = L.context._session.get("http://ifconfig.me",headers=headers)
print(f"STARTIN UP MyIP {x.content}")

# Instagram login
L.login("-----------------", "-----------------")    

# Target
user = "snoopdogg"

# Followers (True) or following(False)
followers = True
#followers = False

# Obtain profile metadata 
profile = instaloader.Profile.from_username(L.context, user) 
 
if followers:
    # Print list of followers
    with open(f'/data/{user}_followers.txt', 'a') as f:
        for followee in profile.get_followers(): 
            username = followee.username 
            print(username)
            f.write(f"{username}\n")
else:
    with open(f'/data/{user}_following.txt', 'a') as f: 
        for followee in profile.get_followees(): 
            username = followee.username 
            print(username)
            f.write(f"{username}\n")