import requests
import json

trello_api = "8f226c254a80e9d55de41c6efcee20c2"
trello_token = "ATTAb83d3f692c65052cfdc50d696338531a5fa1e1f3901f39c6dd0dcdfb0aac81af5FD0AE6A"

# deklaracija identifikacije kartica
cards = ["fHA0pVBH", "qMVH4Yaz", "om6iRfSm"]


# funkcija za prikazivanje kartica
def get_cards():
    for card in cards:
        url = "https://api.trello.com/1/cards/" + card

        headers = {
            "Accept": "application/json"
        }

        query = {
            'key': trello_api,
            'token': trello_token
        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )

        print("Card ID: " + json.dumps(json.loads(response.text)['id']) +
              "\nCard name: " + json.dumps(json.loads(response.text)['name']) +
              "\nCard description: " + json.dumps(json.loads(response.text)['desc']) + "\n")


# funkcija za kreiranje kartice
def create_card(name, desc):
    url = "https://api.trello.com/1/cards"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'idList': '66438240fd83e15957862231',
        'key': trello_api,
        'token': trello_token,
        'name': name,
        'desc': desc
    }

    response = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )

    print("Created a new card with ID: " + json.dumps(json.loads(response.text)['id']) +
          "\nCard name: " + json.dumps(json.loads(response.text)['name']) +
          "\nCard description: " + json.dumps(json.loads(response.text)['desc']) + "\n")


# create_card("Nova kartica", "Opis kartice")

get_cards()
