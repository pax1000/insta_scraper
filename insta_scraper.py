# Import required modules
import requests
import time
import random
import json
from create_email import creat_new_email
from insta_acount_creation import create_instagram_account
import logging

logging.basicConfig(level=logging.INFO)

# get SESSIONID

def get_current_headers():
    with open('account_session_id.json','r') as f:
        session_id = json.load(f)["Session_ID"]
    
    return {
        "User-Agent": "Instagram 219.0.0.12.117 Android",
        "Cookie": f"sessionid={session_id};",
    }


# Example list of accounts to scrape 
example_accounts_to_scrape = [
    "natgeo",       
]



# Function to get followers or following list for a given user_id
def get_accounts(user_id, type):
    seen_ids = set()  # To avoid duplicates
    accounts = []     # List to store account data
    next_max_id = ""  # Used for pagination
    while True:
        try:
            # Instagram API endpoint for followers/following
            url = f"https://i.instagram.com/api/v1/friendships/{user_id}/{type}/?count=200&max_id={next_max_id}"
            r = requests.get(url, headers=get_current_headers())
            data = r.json()
            
            time.sleep(random.randint(1,5))  # Random delay to avoid rate-limiting
            print(f'patch size was {len(data["users"])}')

            # Loop through returned users and add them if not already seen
            for user in data['users']:
                if user['id'] not in seen_ids:
                    accounts.append({
                        'id': user['id'],
                        'username': user['username'],
                        "full_name": user['full_name'],
                        "profile_pic_url": user['profile_pic_url'],
                        "is_private": user['is_private'],
                        "is_verified": user['is_verified'] 
                    })
                    seen_ids.add(user['id'])
            
            # Break if no more pages
            if "next_max_id" not in data:
                break
            next_max_id = data["next_max_id"] 
        except Exception as e:
            raise
    return accounts

# Function to get user info + followers and following lists

numb_of_retires = 3
tried_count = 0

def get_user_info(username, tried_count=0):
    
    try:    
        url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
        r = requests.get(url, headers=get_current_headers())
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
            "followers_accounts": get_accounts(user_id, "followers"),
            "following_accounts": get_accounts(user_id, "following"),
        }
        return data
    except Exception as e:
        if tried_count < numb_of_retires:
            logging.info(f'Error occurred, retries left: {numb_of_retires - tried_count - 1}')
            creat_new_email()
            create_instagram_account()
            return get_user_info(username, tried_count + 1)  # Return the result
        else:
            logging.error(f'All {numb_of_retires} retries exhausted')
            raise e  # Re-raise the last exception

        

# Loop through example accounts, get their data, and save as .json files
for account in example_accounts_to_scrape:
    data = get_user_info(account)
    with open(f'{account}.json','w') as f:
        json.dump(data, f, indent=4)
