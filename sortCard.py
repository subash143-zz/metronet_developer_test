#Card Object creation
#The function getValue() defined below can be added to new class and the old class can be inherited. 
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    #Display information in string format
    def toString(self):
        return self.value + " of " + self.suit

    #Assign numerical value to the object for sorting
    def getValue(self):
        retVal = 0
        if self.suit == "Hearts":
            retVal += 0
        elif self.suit == "Diamonds":
            retVal += .1
        elif self.suit == "Clubs":
            retVal += .2
        elif self.suit == "Spades":
            retVal += .3
        
        if self.value == "A":
            retVal += 14
        if self.value == "2":
            retVal += 2
        if self.value == "3":
            retVal += 3
        if self.value == "4":
            retVal += 4
        if self.value == "5":
            retVal += 5
        if self.value == "6":
            retVal += 6
        if self.value == "7":
            retVal += 7
        if self.value == "8":
            retVal += 8
        if self.value == "9":
            retVal += 9
        if self.value == "10":
            retVal += 10
        if self.value == "J":
            retVal += 11
        if self.value == "Q":
            retVal += 12
        if self.value == "K":
            retVal += 13
        
        return retVal


#Sorting function
def sortCards(cards, descending=False):
    result_list = sorted(cards, key=lambda cards: cards.getValue(), reverse=descending)
    return result_list

#Generating input values for testing
cards = []
cards.append(Card("Hearts", "A"))
cards.append(Card("Hearts", "7"))
cards.append(Card("Clubs", "3"))
cards.append(Card("Spades", "A"))

#Calling sorting function
retVal = sortCards(cards, True)

#Displaying output after sorting
for value in retVal:
    print(value.toString())