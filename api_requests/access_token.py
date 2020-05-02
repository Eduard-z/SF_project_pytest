import requests

params_post = {
    "grant_type": "password",
    "client_id": "YjkyMzJmNDUzMGNmOTYzODVlNDQ0ZjE2OTUxOTU1NDI5MGViN2I3NWU3YTFjNmY300D6F000002JvCk",
    "client_secret": "3490590311975058371",
    "username": "ed@ed.ed",
    "password": "Cheglad3e|"
    }

get_access_token = requests.post("https://login.salesforce.com/services/oauth2/token", params=params_post)
