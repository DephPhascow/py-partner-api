from dotenv import load_dotenv
from os import getenv

from py_partner_api.PartnerAPI import PartnerAPI
from py_partner_api.cache.memory_cache import MemoryCache
load_dotenv()

TOKEN = getenv("TOKEN")

def run():
    partner = PartnerAPI(TOKEN, MemoryCache())
    res = partner.load_services()
    print(res[0].description)

if __name__ == "__main__":
    run()