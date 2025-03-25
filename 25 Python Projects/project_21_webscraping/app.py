import requests
from bs4 import BeautifulSoup as bs

github_user = input("Input Github User: ")
url = f'https://github.com/{github_user}'

# Set headers to mimic a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

r = requests.get(url, headers=headers)

if r.status_code == 200:
    soup = bs(r.content, "html.parser")
    profile_image_tag = soup.find('img', {'alt': f'@{github_user}'})  # Updated search
    if profile_image_tag:
        print(profile_image_tag['src'])
    else:
        print("Profile image not found.")
else:
    print("User not found or request blocked.")
