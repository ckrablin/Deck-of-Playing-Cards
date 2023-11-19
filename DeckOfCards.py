import random
class Deck:
  def __init__(self):
    self.deck = []
    self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9','10', 'Jack', 'Queen', 'King']
    self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    self.reset()
  def reset(self):
    self.deck = [f'{rank} of {suit}' for suit in self.suits for
    rank in self.ranks]
  def shuffle(self):
    random.shuffle(self.deck)
  def deal(self):
    if len(self.deck) == 0:
      return None
    return self.deck.pop()
  def count(self):
    return len(self.deck)
  
print("Welcome to the Card Game")
print("There is a deck of 52 cards")


# Create a deck
deck = Deck()
# Shuffle the deck
deck.shuffle()
# Deal a card

NumberOfCards=int(input("how many cards do you want?"))
DealtCards=[]
for _ in range(NumberOfCards):
  card = Deck.deal()
  if card is not None:
    DealtCards.append(f"{card.rank} of {card.suit}" )
  else:
    print("There are no more cards in the deck")
if DealtCards:
  print("Dealt Cards:")
  for card in DealtCards:
    print(card
        )
   
card = deck.deal()
if card is not None:
  print(f"Dealt card: {card}")
else:
  print("No more cards in the deck.")
# Count the remaining cards
count = deck.count()
print(f"Remaining cards in the deck: {count}")
