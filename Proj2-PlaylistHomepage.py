from typing import List
from random import randint
# My name: Naomi Ross
# My partner's name: Cameron Mccaster

# User Information
USERNAME = "MusicFan'03"
PASSWORD = "hunter1"
users_playlists = [2019386, 5343409, 9082438]
subscriber_count = 10

# Site Policies
MAX_PASSWORD_ATTEMPTS_ALLOWED = 3
MAX_VIDEOS_OUTPUTTED_AT_ONCE = 5

# Playlists (in the form of lists of video IDs)
top_hits_playlist = [5390161, 7736243, 8267507, 4922599, 4559658, 9897626, 1461025, 7434914, 6093037, 6438692, 8117542, 
5746821, 9566779, 5718817, 2459304, 5610524, 6980497, 4547223, 9086699]
top_2010s_playlist = [3720918, 6382983, 1012930, 1109274, 2981023, 7394792]
my_mix = [6382983, 2981023, 9086699]

# Dictionaries
playlist_id_to_video_list = {2019386 : top_hits_playlist, 5343409: top_2010s_playlist, 9082438: my_mix}
playlist_id_to_title = {2019386 : "Top Hits", 5343409: "Top 2010s", 9082438: "My Mix"}
playlist_title_to_id = {"Top Hits": 2019386, "Top 2010s": 5343409, "My Mix": 9082438}

# Videos (key = Video ID, value = Video Title)
video_id_to_title = {
5390161 : "Who Want Smoke",
7736243 : "INDUSTRY BABY",
8267507 : "STAY",
1012930 : "Style",
1109274 : "bad guy",
2981023 : "Blank Space",
4922599 : "Love Nwantiti Remix",
4559658 : "Essence (Official Video)",
9897626 : "Pepas",
5610524 : "Outside (Better Days)",
6980497 : "Lo Siento BB:/",
4547223 : "Face Off",
9086699 : "Heat Waves",
3720918 : "Despacito",
9086691 : "Royals",
1461025 : "Fancy Like",
7434914 : "Way 2 Sexy",
6093037 : "Corta Venas",
6438692 : "Need to Know",
8117542 : "MONEY",
5746821 : "Wild Side ",
9566779 : "Knife Talk",
1683724 : "Life Support",
5718817 : "Save Your Tears",
2459304 : "Ghost",
6382983 : "Love Yourself",
7394792 : "7 rings",
}

# Tip: Take in a playlist (its list of videos) are return a new, shuffled playlist.
# Create a new list (shuffled_playlist) to put video IDs into.
# Create an empty set to store taken positions (ints).
# While the set is smaller than the original playlist (in terms of length), get a random int (which can be a position/index),
# and if the int is not already taken (i.e. in the set of taken positions),
# append the video at that position in the original list to the end of the new list. Be sure to update the set.
# Remember, we can only rely on sets for group membership.
def get_shuffled_playlist(video_list: List[int]) -> List[int]:
    shuffled_playlist = []
    playlist_length = len(video_list)
    used_indexes = set()
    while len(used_indexes) < playlist_length:
        random_index = randint(0,playlist_length-1)
        if random_index not in used_indexes:
            used_indexes.add(random_index)
            random_video = video_list[random_index]
            shuffled_playlist.append(random_video)
    return shuffled_playlist

# This prints out the playlist and its videos, 
# but only up to 5 video titles at a time (before asking for user input).
# Tip: In a loop, keep track of how many video titles have been printed as you print them, and
# after each 5, ask for user input. If the user says "no", break out of the loop.

def display_full_playlist(playlist_id: int) -> None:
    want_to_see_more = ""
    num_songs = 0
    total_songs = 0   
    songs = playlist_id_to_video_list[playlist_id]
    while want_to_see_more != "no" and num_songs != MAX_VIDEOS_OUTPUTTED_AT_ONCE:
            for index in songs:
                video_title = video_id_to_title.get(index)
                print(video_title)
                num_songs += 1
                total_songs += 1
                if total_songs == len(songs):
                    want_to_see_more = "no"
                    continue
                elif num_songs >= MAX_VIDEOS_OUTPUTTED_AT_ONCE:
                    want_to_see_more = input("...Do you want to see more? ")
                    if want_to_see_more == "yes":
                        num_songs = 0
                    else:
                        break
# This prints out a playlist title and video count.
def display_playlist_preview(playlist_id: int) -> None:
    print(playlist_id_to_title.get(playlist_id))
    print(len(playlist_id_to_video_list.get(playlist_id)), "videos")
    print("")

# Tip: Call display_playlist_preview from this, for each playlist.
def display_personal_homepage() -> None:
    print("*" * len(USERNAME))
    print(USERNAME)
    print("{} subscribers".format(subscriber_count))
    print("")
    display_playlist_preview(2019386) #for playlist id in dict print whatever
    display_playlist_preview(5343409)
    display_playlist_preview(9082438)
# Tip: If the user wants to shuffle a playlist, make sure the playlist_id_to_video_list dict
# is updated with the new, shuffled playlist from get_shuffled_playlist.
# If the user wants to shorten a playlist and then it becomes empty, make sure to delete
# it from any relevant dicts.
def do_playlist_action(playlist_id: int, choice: int) -> None:
    if choice == 1:
        video_list = playlist_id_to_video_list[playlist_id]
        shuffled_playlist = get_shuffled_playlist(video_list)
        playlist_id_to_video_list[playlist_id] = shuffled_playlist
    elif choice == 2:
        video_list = playlist_id_to_video_list[playlist_id]
        del video_list[0]
        if len(video_list) > 0:
            playlist_id_to_video_list[playlist_id] = video_list
        else:
            del playlist_id_to_video_list[playlist_id] #deletemore.
            video_title = playlist_id_to_title[playlist_id]
            del playlist_title_to_id[video_title]
            del playlist_id_to_title[playlist_id]
    elif choice == 4:
        pass
    else:
        print("Error.")

# Tip: Use a while loop in here that keeps going until the user choice equals 4 (for exit).
# In the while loop, you can ask which playlist the user wants to see, and then offer further playlist actions on that playlist.
# You should make calls to display_full_playlist and do_playlist_action.
def main_playlist_interface() -> None:
    choice = 0
    while choice != 4:
        playlist_pick = input("What playlist do you want to see? ")
        if playlist_pick in playlist_title_to_id:
            playlist_id = playlist_title_to_id.get(playlist_pick)
            display_full_playlist(playlist_id)
            choice = int(input("Actions: 1 for shuffle, 2 for shorten, 4 for exit. "))
            do_playlist_action(playlist_id, choice)
        else:
            print("Error.")
            continue
# This asks the user for their username and password, and returns whether the login is successful.
def user_login() -> bool:    
    username_input = input("Username: ")
    password_input = input("Password: ")

    if username_input == USERNAME and password_input == PASSWORD:
        return True
    else:
        return False

#####################################################
print("> YouTube")
successful_login = False
successful_login = user_login()
##log in loop is outside, inside only returns true or
user_login_attempts = 1
while successful_login != True and user_login_attempts < MAX_PASSWORD_ATTEMPTS_ALLOWED:
    if successful_login == False:
        print("Try again.")
    user_login_attempts += 1
    successful_login = user_login()
if user_login_attempts == MAX_PASSWORD_ATTEMPTS_ALLOWED:
    print("Access Denied.")

#############
if successful_login:
    display_personal_homepage()
    main_playlist_interface()

