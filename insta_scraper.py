# Import required modules
import requests
import time
import random
import json
import os
from dotenv import find_dotenv,load_dotenv



# Load environment variables from .env file to get SESSIONID
dovent_path = find_dotenv()
load_dotenv(dovent_path)
SESSIONID = os.getenv('SESSIONID')

# Define headers for Instagram API requests with session cookie for authentication
HEADERS = {
    "User-Agent": "Instagram 219.0.0.12.117 Android",
    "Cookie": f"sessionid={SESSIONID};",
}

# Example list of accounts to scrape (only 'nike' is active here)
example_accounts_to_scrape = [
    "bahaa__beh__",
    # "starbucks",
    # "natgeo",       
    # "therock",
    # "instagram",
    # "nasa",
    # "cristiano",
    # "leomessi",
    # "khaby00",
    # "9gag",
]

# # Function to get followers or following list for a given user_id
# def get_accounts(user_id, type):
#     seen_ids = set()  # To avoid duplicates
#     accounts = []     # List to store account data
#     next_max_id = ""  # Used for pagination

#     while True:
#         try:
#             # Instagram API endpoint for followers/following
#             url = f"https://i.instagram.com/api/v1/friendships/{user_id}/{type}/?count=200&max_id={next_max_id}"
#             r = requests.get(url, headers=HEADERS)
#             data = r.json()
            
#             time.sleep(random.randint(1,3))  # Random delay to avoid rate-limiting
#             print(f'patch size was {len(data["users"])}')

#             # Loop through returned users and add them if not already seen
#             for user in data['users']:
#                 if user['id'] not in seen_ids:
#                     accounts.append({
#                         'id': user['id'],
#                         'username': user['username'],
#                         "full_name": user['full_name'],
#                         "profile_pic_url": user['profile_pic_url'],
#                         "is_private": user['is_private'],
#                         "is_verified": user['is_verified'] 
#                     })
#                     seen_ids.add(user['id'])
            
#             # Break if no more pages
#             if "next_max_id" not in data:
#                 break
#             next_max_id = data["next_max_id"] 
#         except Exception as e:
#             print(f'there was an error: {e}')
#             break
#     return accounts

# Function to get user info + followers and following lists
def get_user_info(username):
    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
    try:
        r = requests.get(url, headers=HEADERS)
        r.raise_for_status()
        user = r.json()['data']['user']
        
        # Extract main user info
        user_id = user['id']
        user_biography = user['biography']
        user_bio_links = [link['url'] for link in user['bio_links']] 
        user_posts_count = user['edge_owner_to_timeline_media']['count']
        user_followers_count = user['edge_followed_by']['count']
        user_following_count = user['edge_follow']['count']
        
        # Combine all data into a single dict
        data = {
            "user_id": user_id,
            "user_full_name": user['full_name'],
            "user_biography": user_biography,
            "user_bio_links": user_bio_links,
            "user_posts_count": user_posts_count,
            "user_followers_count": user_followers_count,
            "user_following_count": user_following_count,
            # "followers_accounts": get_accounts(user_id, "followers"),
            # "following_accounts": get_accounts(user_id, "following"),
        }
        print(user)
        return data
    except Exception as e:
        print(f"[!] Failed to get user info: {e}")
        return None

# Loop through example accounts, get their data, and save as .json files
for account in example_accounts_to_scrape:
    data = get_user_info(account)
    with open(f'{account}.json','w') as f:
        json.dump(data, f, indent=4)
