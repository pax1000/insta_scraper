import json
from create_email import wait_for_messages
import re
import logging
from camoufox.sync_api import Camoufox




def create_instagram_account():
    # Load email address from JSON file
    try:
        with open('email_hash.json', 'r') as f:
            data = json.load(f)
    
        with Camoufox(geoip=True) as browser:
                context = browser.new_context(
                    locale="en-US",
                    extra_http_headers={"Accept-Language": "en-US,en;q=0.9"},
                    record_video_dir='videos/',
                    record_video_size={"width": 1280, "height": 720}
                )
                page = context.new_page()
                page.goto("https://www.instagram.com/accounts/emailsignup/")
        
                # Fill in sign-up form
                page.get_by_label('Mobile Number or Email').type(data['email'],delay=100)
                page.get_by_label('Password').type('G7p#kV2!eR')
                names = data['email'].split('@')[0]
                page.get_by_label('Full Name').type(names,delay=100)
                page.get_by_label('Username').type(names,delay=100)
        
                # Wait 2 seconds before continuing
                page.wait_for_timeout(2000)
        
                # Click "Sign up" button
                page.get_by_role("button", name="Sign up").click()
        
                # Select birth year (2001)
                page.locator('select[title="Year:"]').select_option("2001")
        
                # Wait 3 seconds before clicking "Next"
                page.wait_for_timeout(3000)
                page.get_by_role('button', name="Next").click()
        
                # Wait for email with confirmation code
                email_message = wait_for_messages()
        
                # Extract 6-digit confirmation code, strip RTL marks (U+200F)
                pattern = r'[\u200F]*\d{6}[\u200F]*'
                Confirmation_Code = re.search(pattern, email_message).group().replace('\u200f', '')  # type: ignore
        
                # Wait 15 seconds to ensure the page is ready for input
                page.wait_for_timeout(15000)
        
                # Enter confirmation code
                page.get_by_role("textbox", name="Confirmation Code").type(Confirmation_Code,delay=100)
        
                # Wait 2 seconds before clicking "Next"
                page.wait_for_timeout(2000)
                page.get_by_text('Next').click()
        
                # Wait for final redirect to Instagram homepage
                page.wait_for_url('https://www.instagram.com/', timeout=40000)
        
                # Extract session ID from cookies
                cookies = page.context.cookies()
                for cookie in cookies:
                    if cookie['name'] == 'sessionid':  # type: ignore
                        with open('account_session_id.json', 'w') as f:
                            json.dump({
                                'Session_ID': cookie['value']  # type: ignore
                            }, f, indent=4)
                        break
                else:
                    print("Session ID not found.")
        
                page.close()
    except Exception as e:
        logging.error(f'there was an error as {e}')



