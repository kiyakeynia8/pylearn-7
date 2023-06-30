import instaloader
import getpass

f = open("followers list.txt", "r")
old_followers = []
for line in f:
    old_followers.append(line)
f.close()

l = instaloader.Instaloader()

user_name = input("enter user nsme: ")
print("OK")

password = getpass.getpass("enter password: ")
print("OK")

l.login(user_name, password)
pritn("you logged in")

profile = instaloader.Profile.from_username(l.context, "kia13keynia")

followers = []
for follower in profile.get_followers():
    followers.append(follower)

f = open("new followers.txt","w")
for follower in followers:
    if follower not in old_followers:
        f.write(follower + "\n")

n.close()