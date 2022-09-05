import logging
from steam.client import SteamClient
from dota2.client import Dota2Client

logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)


client = SteamClient()
dota = Dota2Client(client)

@client.on('logged_on')
def start_dota():
    dota.launch()

@dota.on('ready')
def fetch_profile_card():
    jobid = dota.request_profile_card(70388657)
    profile_card = dota.wait_msg(jobid, timeout=10)

    if profile_card:
        print(str(profile_card))

@dota.on('profile_card')
def print_profile_card(account_id, profile_card):
    if account_id == 70388657:
        print(str(profile_card))


client.cli_login("login_here :)", "passwrod_here :)")
client.run_forever()
