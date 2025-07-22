import requests



url = 'https://api.mail.tm'


r = requests.get(f"{url}/domains")
domains_names = r.json()
domains = domains_names['hydra:member'][0]['domain']
