from pprint import pprint
from typing import List

from trello import TrelloClient, Board, Card

MY_API_KEY = 'SUPPOSE_THIS_IS_MY_API_KEY'
MY_API_SECRET = 'SUPPOSE_THIS_IS_MY_API_SECRET'

client = TrelloClient(
    api_key=MY_API_KEY,
    api_secret=MY_API_SECRET
)

BOARD_ID = '4d5ea62fd76aa1136000000c'
trello_roadmap_board: Board = client.get_board(BOARD_ID)
cards_of_trello_roadmap_board: List[Card] = trello_roadmap_board.get_cards()
pprint([card.name for card in cards_of_trello_roadmap_board])
