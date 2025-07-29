import requests
import hashlib
import random
import string
import time
import json
from dotenv import find_dotenv, load_dotenv
import os
import logging

# Load environment variables from .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Get API key from environment variables
API_KEY = os.getenv("RAPIDAPI_KEY")

# Set headers for the API requests
headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "privatix-temp-mail-v1.p.rapidapi.com"
}

def creat_new_email():
    try:
        url = f"https://privatix-temp-mail-v1.p.rapidapi.com/request/"
        
        # Get list of available domains
        response = requests.get(url + 'domains/', headers=headers)
        domains = response.json()
        domain = domains[0]  # Use the first domain
        
        # Generate a random 10-letter username and append the domain
        letters = string.ascii_lowercase
        email = ''.join(random.choices(letters, k=10)) + domain
        
        logging.info('creating new email')
        
        # Create MD5 hash of the email to get its ID on the API
        email_hash = hashlib.md5(email.encode()).hexdigest()
        
        # Store email and hash in a JSON file
        data = {
            "email": email,
            "email_hash": email_hash   
        }
        with open('email_hash.json', "w") as f:
            json.dump(data, f, indent=4)
    
    except Exception as e:
        logging.error(f'there was an error as {e}')

def wait_for_messages():
    # Load the email hash from the JSON file
    with open('email_hash.json', 'r') as f:
        email_hash = json.load(f)['email_hash']
    
    # Try up to 30 times (with 2s delay) to get email messages
    for i in range(30):
        emails_url = f"https://privatix-temp-mail-v1.p.rapidapi.com/request/mail/id/{email_hash}/"
        response = requests.get(emails_url, headers=headers)
        emails = response.json()
        
        # If there's at least one email, return the latest message text
        if isinstance(emails, list) and emails:
            logging.info('confirmation code recived')
            return emails[-1]['mail_text']
        else:
            logging.info("waiting for confirmation code...")
        
        # If this is the last attempt and still no email
        if i == 29:
            logging.info('no code was sent')
        
        time.sleep(2)
