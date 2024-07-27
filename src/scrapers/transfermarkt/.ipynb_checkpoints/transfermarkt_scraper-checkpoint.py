import re
import requests

from bs4 import BeautifulSoup

def main():
    transfermarkt_urls = get_transfermarkt_urls()
    scrape_urls(transfermarkt_urls)

    return

def scrape_urls(urls):
    for url in urls:
        player_id = url.split('/')[-1]

    # find user agent header from https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending in order to avoid being blocked by transfermarkt
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    # make request to webpage
    response = requests.get(url, headers=headers)

    # create soup and parse html
    soup = BeautifulSoup(response.content, "html.parser")

    # use css selectors to find class and then get text, remove whitespace, remove null
    player_name = soup.select_one('h1[class="data-header__headline-wrapper"]').text.split('\n')[-1].strip()
    player_number = soup.select_one('span[class="data-header__shirt-number"]').text.replace('#', '').strip()
    
    # use regex101.com to find pattern for player contract expiration date
    player_contract_expiry = re.search("Contract expires: .*__content\">(.*?)</span>", str(soup)).group(1)
    player_foot = re.search("Foot:</span>\s*<span class=\"info-table__content info-table__content--bold\">(.*?)</span>", str(soup)).group(1)
    player_agent = re.search("Player agent:</span>\s*<span[^>]*>\s*<a[^>]*>([^<]+)</a>", str(soup)).group(1)
    player_outfitter = re.search("Outfitter:</span>\s*<span class=\"info-table__content info-table__content--bold\">\s*(.*?)\s*</span>", str(soup)).group(1)
    player_citizenship = re.search("Citizenship:</span>[\s\S]*?alt=\"([^\"]+)\"", str(soup)).group(1)
    player_contract_start = re.search("Joined:</span>\s*<span[^>]*>\s*([^<]+)</span>", str(soup)).group(1)
    player_birthplace = re.search("Place of birth:</span>\s*<span[^>]*>\s*<span[^>]*>([^<\s]+)", str(soup)).group(1)
    # TO:DO regex for player current club

    # call api endpoint to get market value development over time
    response = requests.get(f'https://www.transfermarkt.us/ceapi/marketValueDevelopment/graph/{player_id}', headers=headers)
    response.json().keys()
    # TO:DO clean data and create dict of value, date, team, age

    # TO:DO: api endpoint for transfer history
    # TO:DO: api endpoint for relevant news 
    # TO:DO: api endpoint for current rumors

def get_transfermarkt_urls():
    urls = []
    return urls

if __name__ == "__main__":
    main()