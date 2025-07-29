# Instagram Scraper

A Python-based tool for scraping Instagram user profile information including basic account details, bio, website links, post/follower counts, and complete followers/following lists. Features automatic account creation and session management with retry logic.

## Features

✅ **Full name** extraction  
✅ **Bio** text retrieval  
✅ **Website link** extraction  
✅ **Number of posts** count  
✅ **Followers count** retrieval  
✅ **Following count** retrieval  
✅ **Complete followers list** with detailed user info
✅ **Complete following list** with detailed user info
✅ **Automatic Instagram account creation** using temporary emails
✅ **Session management** with automatic renewal
✅ **Retry logic** with account recreation on failures
✅ **Rate limiting protection** with random delays

## Project Structure

```
├── insta_scraper.py          # Main scraper script
├── create_email.py           # Temporary email creation and management
├── insta_acount_creation.py  # Automated Instagram account creation
├── account_session_id.json   # Current session storage
├── email_hash.json          # Email credentials storage
├── README.md                # Project documentation
└── .env                     # Environment variables (RapidAPI key)
```

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd instagram-scraper
```

2. Install required dependencies:
```bash
pip install requests playwright python-dotenv
```

3. Install Playwright browsers:
```bash
playwright install chromium
```

4. Create a `.env` file in the project root:
```bash
touch .env
```

## Configuration

### Environment Variables

Create a `.env` file and add your RapidAPI key for the temporary email service:

```env
RAPIDAPI_KEY=your_rapidapi_key_here
```

**How to get your RapidAPI Key:**
1. Sign up at [RapidAPI](https://rapidapi.com/)
2. Subscribe to the "Privatix Temp Mail" API
3. Copy your API key from the dashboard

## Usage

### Basic Usage

Edit the `example_accounts_to_scrape` list in `insta_scraper.py` to include the usernames you want to scrape:

```python
example_accounts_to_scrape = [
    "natgeo",
    "username1", 
    "username2",
]
```

Run the scraper:

```bash
python insta_scraper.py
```

### How It Works

1. **Automatic Account Creation**: Creates temporary email addresses and Instagram accounts automatically
2. **Session Management**: Extracts and stores session IDs for API access
3. **Data Scraping**: Retrieves comprehensive user data including followers/following lists
4. **Retry Logic**: Automatically creates new accounts if sessions expire or fail
5. **Rate Limiting**: Implements delays to avoid Instagram's rate limits

### Output

The script creates individual JSON files for each scraped account containing:

```json
{
    "user_id": "123456789",
    "user_full_name": "Full Name",
    "user_biography": "Bio text here...",
    "user_bio_links": ["https://website.com"],
    "user_posts_count": 150,
    "user_followers_count": 50000,
    "user_following_count": 500,
    "followers_accounts": [
        {
            "id": "user_id",
            "username": "follower_username",
            "full_name": "Follower Name",
            "profile_pic_url": "https://...",
            "is_private": false,
            "is_verified": false
        }
    ],
    "following_accounts": [
        {
            "id": "user_id", 
            "username": "following_username",
            "full_name": "Following Name",
            "profile_pic_url": "https://...",
            "is_private": false,
            "is_verified": true
        }
    ]
}
```

## Code Features

- **Automated Account Management**: Creates Instagram accounts using temporary emails
- **Session Persistence**: Stores and reuses session IDs across runs
- **Intelligent Retry Logic**: Recreates accounts when sessions fail (configurable retry count)
- **Comprehensive Data Extraction**: Gets complete followers/following lists with pagination
- **Rate Limiting Protection**: Random delays between requests (1-5 seconds)
- **Error Handling**: Graceful error handling with detailed logging
- **Duplicate Prevention**: Avoids duplicate entries in followers/following lists
- **JSON Export**: Automatic saving of all scraped data to structured JSON files

## Configuration Options

### Retry Settings

You can modify the retry behavior in `insta_scraper.py`:

```python
numb_of_retires = 3  # Number of retry attempts
```

### Rate Limiting

Adjust delays in the `get_accounts()` function:

```python
time.sleep(random.randint(1,5))  # Random delay between 1-5 seconds
```

## Important Notes

⚠️ **Legal and Ethical Considerations:**
- Only scrape public Instagram profiles
- Respect Instagram's Terms of Service
- Use responsibly and don't overload Instagram's servers
- Be aware that automated account creation may violate Instagram's ToS
- Consider the privacy implications of collecting follower data

⚠️ **Technical Limitations:**
- Requires RapidAPI subscription for temporary email service
- Browser automation may be detected by Instagram
- Large follower lists may take significant time to scrape
- Instagram may implement additional anti-bot measures

⚠️ **Rate Limiting:**
- The script includes delays but Instagram has sophisticated rate limiting
- Large accounts with many followers/following may trigger limits
- Consider breaking large scraping jobs into smaller batches

## Troubleshooting

**Common Issues:**

1. **"Failed to get user info" Error:**
   - Check if your RapidAPI key is valid
   - Ensure the target username exists and is public
   - Verify your internet connection
   - Check if Instagram has implemented new anti-bot measures

2. **Account Creation Failures:**
   - Verify RapidAPI subscription is active
   - Check if temporary email service is working
   - Ensure Playwright browsers are installed
   - Try running with `headless=False` to debug visually

3. **Session Expiration:**
   - The script automatically creates new accounts when sessions fail
   - If persistent issues occur, check Instagram's current policies
   - Consider reducing scraping frequency

4. **Browser Automation Issues:**
   - Ensure Playwright is properly installed
   - Try updating browser binaries: `playwright install chromium`
   - Check if Instagram has changed their signup flow

## Dependencies

- `requests`: HTTP requests for Instagram API
- `playwright`: Browser automation for account creation
- `python-dotenv`: Environment variable management
- `hashlib`: Email hashing for temporary mail API
- `random`: Random delays and usernames
- `json`: Data serialization
- `re`: Regular expressions for code extraction
- `logging`: Error tracking and debugging

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Disclaimer

This tool is for educational and research purposes only. Users are responsible for complying with Instagram's Terms of Service, RapidAPI's terms, and applicable laws. The automated account creation feature may violate Instagram's Terms of Service. The developers are not responsible for any misuse of this tool or any consequences resulting from its use.

## License

This project is open source. Please use responsibly and in accordance with Instagram's Terms of Service and applicable laws.