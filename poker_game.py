class Card:
    def __init__(self):
        SUITS = ["♣","♦","♥","♠"]
        RANKS = ["1","2","3","4","5","6","7","8","9","10","A","J","k","Q"]

        def __init__(self, rank, suit):
            if rank not in self.RANKS:
                raise Exception(f"Invalid rank, must be one of {self.RANKS}")
            if suit not in self.SUITS:
                raise Exception(f"Invalid suit, must be one of {self.SUITES}")
            self._rank = rank
            self ._suit = suit

        def __gt__(self, other):
            return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

        @property
        def suit(self):
            return self.rank

        @property
        def rank(self):
            return self._rank

        def __str__(self):
            return f"{self.rank}{self.suit}"

        def __repr__(self):
            return self.__str()

#c1= Card("A","♣")
# c2 = Card("1","♥")
# c2 = Card("1","#")
#c2 = Card("Q","♥")
#print(c2)

class Deck:
    def __init__(self):
     cards = []
    for rank in Cards.RANKS:
     for suit in Cards.SUITS:
         card = Card(rank,suit)
         cards.append(card)
        self._cards = tuple(cards)

     @property
     def cards(self):
         return self._cards

    def shuffle(self):
        # shuffles the cards in the deck
        cards = list(self.cards)
        random.shuffle(cards)
        self._cards = tuple(cards)

d = Deck()
print(d)
d.shuffle()
print(d)

#acel1 = Card("A", Card,SUITS[0])
#acel2 = Card("A", Card,SUITS[1])
#print(ace1,ace2)
#list_aces =[ace1, ace2]
#d.cards.append(ace1)
#d.cards.append(ace2)
#print(d)

class Hand:
    def __init__(self, deck):
        # deck is shuffled before
        cards = []
        for i in range(5):
             cards.append(decl.cards[i])
        self._cards = tuple(cards)

    def __str__(self):
        return str(self._cards)

    @property
    def is_flush(self):
        suit = self._cards[0].suit
        for i in range(1, 5):
            if self._cards[i].suit != suit:
                return False
            return True
    @property
    def is_pair(self):
        rank = []
        for card in self.cards:
            ranks.append(card.rank)
        for rank in ranks:
            if ranks.count(rank) == 2:
                return True
            return False
    @property
    def is_4_kind(self):
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        for rank in ranks:
            if ranks.count(rank) == 4:
                return True
            return False

    @property
    def is_full_house(self):
        return self.is_3_kind and self.is_pair

    @property
    def is_2_pair(self):
        ranks = {}
        for card in self.cards:
            ranks.append(card.rank)
        ranks = set(ranks)
        return len(ranks) == 3 and not self.is_3_kind:

    def sort_hand(self):
        cards = list(self.cards)
            cards.sort()
            print(f"sorted hand is: {cards})

    @property
    def is_straight(self):
        cards = list(self.cards)
        cards.sort()
        distance = Card.RANKS.index(cards[4].rank)- Card.RANKS.index(cards[0].rank)
        return distance == 4 and not self.is_pair and not self.is_3_kind

precision = Tries = 100
i = 0
while True:
    i = i +1
    d = Deck()
    d.shuffle()
    hand = Hand(d)
    if hand .is_2_pair:
    #if hand.is_flush:
        tries -= 1
         #print("Found a flush!!")
         #print(hand)
    if tries == 0:
         break

probability = tries/i * 100
print(f"The odds of getting a flush are {probability}%")


