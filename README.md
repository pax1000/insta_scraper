# Instagram Scraper

A Python-based tool for scraping Instagram user profile information including basic account details, bio, website links, and post/follower counts.

## Features

✅ **Full name** extraction  
✅ **Bio** text retrieval  
✅ **Website link** extraction  
✅ **Number of posts** count  
✅ **Followers count** retrieval  
✅ **Following count** retrieval  

## Project Structure

```
├── insta_scraper.py              # Main scraper script
├── ig_create_account_get_session.py  # Session management utilities
├── README.md                     # Project documentation
└── .env                         # Environment variables (not included)
```

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd instagram-scraper
```

2. Install required dependencies:
```bash
pip install requests python-dotenv
```

3. Create a `.env` file in the project root:
```bash
touch .env
```

## Configuration

### Environment Variables

Create a `.env` file and add your Instagram session ID:

```env
SESSIONID=your_instagram_session_id_here
```

**How to get your Session ID:**
1. Log into Instagram on your web browser
2. Open Developer Tools (F12)
3. Go to Application/Storage → Cookies → instagram.com
4. Find the `sessionid` cookie and copy its value

## Usage

### Basic Usage

Edit the `example_accounts_to_scrape` list in `insta_scraper.py` to include the usernames you want to scrape:

```python
example_accounts_to_scrape = [
    "username1",
    "username2",
    "username3",
]
```

Run the scraper:

```bash
python insta_scraper.py
```

### Output

The script will create individual JSON files for each scraped account containing:

```json
{
    "user_id": "123456789",
    "user_full_name": "Full Name",
    "user_biography": "Bio text here...",
    "user_bio_links": ["https://website.com"],
    "user_posts_count": 150,
    "user_followers_count": 50000,
    "user_following_count": 500
}
```

## Code Features

- **Rate Limiting Protection**: Built-in delays between requests
- **Error Handling**: Graceful error handling for failed requests
- **JSON Export**: Automatic saving of scraped data to JSON files
- **Modular Design**: Easy to extend and modify

## Important Notes

⚠️ **Legal and Ethical Considerations:**
- Only scrape public Instagram profiles
- Respect Instagram's Terms of Service
- Use responsibly and don't overload Instagram's servers
- Consider rate limiting and be respectful of the platform

⚠️ **Technical Limitations:**
- Requires a valid Instagram session ID
- May break if Instagram changes their API
- Rate limiting may affect large-scale scraping

## Troubleshooting

**Common Issues:**

1. **"Failed to get user info" Error:**
   - Check if your session ID is valid and not expired
   - Ensure the username exists and is public
   - Verify your internet connection

2. **Rate Limiting:**
   - The script includes random delays to avoid rate limiting
   - If you encounter issues, increase the delay intervals

3. **Session Expired:**
   - Instagram sessions expire regularly
   - Update your `.env` file with a fresh session ID

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Disclaimer

This tool is for educational purposes only. Users are responsible for complying with Instagram's Terms of Service and applicable laws. The developers are not responsible for any misuse of this tool.

## License

This project is open source. Please use responsibly and in accordance with Instagram's Terms of Service.