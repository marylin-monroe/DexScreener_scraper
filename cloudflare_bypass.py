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

        
        return None
# ... To get access to the code, please contact the scraper creator.
