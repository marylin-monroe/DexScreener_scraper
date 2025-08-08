import random
import tls_client
from fake_useragent import UserAgent
import time

class CloudflareBypass:
    """
    Класс для обхода Cloudflare защиты на сервисе DexScreener
    адаптирован из моего рабочего GMGN скрапера
    """
    
    def __init__(self):
        self.sendRequest = None
        self.proxyPosition = 0
        
    def randomise(self):
        self.identifier = random.choice(
            [browser for browser in tls_client.settings.ClientIdentifiers.__args__
             if browser.startswith(('chrome', 'safari', 'firefox', 'opera'))]
        )
        parts = self.identifier.split('_')
        identifier, version, *rest = parts
        identifier = identifier.capitalize()
        
        
        self.sendRequest = tls_client.Session(
            random_tls_extension_order=True, 
            client_identifier=self.identifier
        )
        self.sendRequest.timeout_seconds = 60

        
        if identifier == 'Opera':
            identifier = 'Chrome'
            osType = 'Windows'
        elif version.lower() == 'ios':
            osType = 'iOS'
        else:
            osType = 'Windows'

        # random User-Agent
        try:
            self.user_agent = UserAgent(os=[osType]).random
        except Exception:
            self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"

        
        self.headers = {
            'Host': 'dexscreener.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9,fr;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'cache-control': 'max-age=0',
            'user-agent': self.user_agent
        }

    def make_request(self, url, retries=3):
        for attempt in range(retries):
            try:
                self.randomise()  # random for every request
                
                response = self.sendRequest.get(
                    url, 
                    headers=self.headers, 
                    allow_redirects=True
                )
                
                if response.status_code == 200:
                    return response
                elif response.status_code == 429:
                    print(f" Rate limit, waiting 10 seconds...")
                    time.sleep(10)
                    continue
                else:
                    print(f" Status {response.status_code}, retrying...")
                    
            except Exception as e:
                print(f"Request failed on attempt {attempt+1}/{retries}: {e}")
                
            time.sleep(2)  # Pause between requests
        
        print(f" Failed to fetch {url} after {retries} attempts")
        return None
