# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014
import random
import datetime
NO_OF_RECENT_SCORES = 3
import pickle
class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0


class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.Date = ''

Deck = [None]
RecentScores = [None]
Choice = ''


def GetRank(RankNo, AceRank):
  if AceRank == 'l':
    Rank = ''
    if RankNo == 1:
      Rank = 'Ace'
    elif RankNo == 2:
      Rank = 'Two'
    elif RankNo == 3:
      Rank = 'Three'
    elif RankNo == 4:
      Rank = 'Four'
    elif RankNo == 5:
      Rank = 'Five'
    elif RankNo == 6:
      Rank = 'Six'
    elif RankNo == 7:
      Rank = 'Seven'
    elif RankNo == 8:
      Rank = 'Eight'
    elif RankNo == 9:
      Rank = 'Nine'
    elif RankNo == 10:
      Rank = 'Ten'
    elif RankNo == 11:
      Rank = 'Jack'
    elif RankNo == 12:
      Rank = 'Queen'
    elif RankNo == 13:
      Rank = 'King'
  elif AceRank == 'h':
    Rank = ''
    if RankNo == 1:
      Rank = 'Two'
    elif RankNo == 2:
      Rank = 'Three'
    elif RankNo == 3:
      Rank = 'Four'
    elif RankNo == 4:
      Rank = 'Five'
    elif RankNo == 5:
      Rank = 'Six'
    elif RankNo == 6:
      Rank = 'Seven'
    elif RankNo == 7:
      Rank = 'Eight'
    elif RankNo == 8:
      Rank = 'Nine'
    elif RankNo == 9:
      Rank = 'Ten'
    elif RankNo == 10:
      Rank = 'Jack'
    elif RankNo == 11:
      Rank = 'Queen'
    elif RankNo == 12:
      Rank = 'King'
    elif RankNo == 13:
      Rank = 'Ace'
  return Rank
  
  
def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print('5. Options')
  print('6. Save High Scores')
  print('7. Load High Scores')
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def DisplayOptions():
  print('Options Menu')
  print()
  print('1. Set Ace to HIGH or LOW')
  print()
  

def GetOptionChoice():
  OptionChoice = input('Select an option from the menu (q for quit)')
  return OptionChoice


def SetOptions(OptionChoice):
  valid = False
  while not valid:
    if OptionChoice == '1':
      return OptionChoice
      valid = True
    elif OptionChoice == 'q':
      valid = True
    else:
      valid = False
      print('Not Valid')
      GetOptionChoice()
      
      


def SetAceHighOrLow():
  Valid = False
  while not Valid:
    selection = input('Would you like the ace to be high or low? (h/l):')
    if selection == 'h':
      AceRank = 'h'
      Valid = True
    elif selection == 'l':
      AceRank = 'l'
      Valid = True
  print('---- Ace Set! ----')    
  return AceRank
      
   
def GetMenuChoice():
  Choice = input()
  print()
  if Choice in ['Q','q','Quit','QUIT','quit']:
    Choice = 'q'
  return Choice

def LoadDeck(Deck):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank, AceRank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank 
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher

def GetPlayerName():
  valid = False
  while not valid:
    print()
    PlayerName = input('Please enter your name: ')
    print()
    if PlayerName == '':
      print('You must enter something for your name!')
      valid = False
    else:
      valid = True
  return PlayerName

def GetChoiceFromUser():
  Valid = False
  while not Valid:
    Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ')
    if Choice in ['y','Y','yes','Yes']:
      Choice = 'y'
      Valid = True
    elif Choice in ['n','N','No','no']:
      Choice = 'n'
      Valid = True
    else:
      Valid = False
  return Choice

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0
    RecentScores[Count].Date = ''
    
def DisplayRecentScores(RecentScores):

  print()
  print('Recent Scores: ')
  print()
  print('{0:<10} {1:<10} {2:<10}'.format('Name','Score','Date'))
  print()
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    print('{0:<10} {1:<10} {2:<10}'.format(RecentScores[Count].Name,RecentScores[Count].Score, RecentScores[Count].Date))
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

def UpdateRecentScores(RecentScores, Score):
  valid = False
  while not valid:
    PlayerChoice = input('Would you like to add your score to the high score table (y or n):')
    if PlayerChoice in ['n','N','No','no']:
      valid = True
    elif PlayerChoice in ['y','Y','yes','Yes']:
      DateOfGame = datetime.date.today()
      Date = DateOfGame.strftime("%d/%m/%y")
      PlayerName = GetPlayerName()
      FoundSpace = False
      Count = 1
      while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
        if RecentScores[Count].Name == '':
          FoundSpace = True
        else:
          Count = Count + 1
      if not FoundSpace:
        for Count in range(1, NO_OF_RECENT_SCORES):
          RecentScores[Count].Name = RecentScores[Count + 1].Name
          RecentScores[Count].Score = RecentScores[Count + 1].Score
          RecentScores[Count].Date = RecentScores[Count + 1].Date
        Count = NO_OF_RECENT_SCORES
      RecentScores[Count].Name = PlayerName
      RecentScores[Count].Score = Score
      RecentScores[Count].Date = Date
      BubbleSortScores(RecentScores)
      valid = True
    else:
      valid = False
      print('Not valid')

def BubbleSortScores(RecentScores):
    swap = True
    while swap:
      swap = False
      for count in range(len(RecentScores)-1):
          if RecentScores[count].Score > RecentScores[count+1].Score:
              swap = True
              RecentScores[count].Name = RecentScores[Count + 1].Name
              RecentScores[count].Score = RecentScores[Count + 1].Score
              RecentScores[count].Date = RecentScores[Count + 1].Date
              temp = RecentScores[count+1].Name
              temp = RecentScores[count+1].Score
              temp = RecentScores[count+1].Date

    return RecentScores

def SaveScores(RecentScores):
  RecentScores = TRecentScore()
  with open("save_scores.dat", mode="wb") as my_file:
      pickle.dump(RecentScores, my_file)
    
def LoadScores():
  RecentScores = TRecentScore
  with open("save_scores.dat", mode="rb") as my_file:
     RecentScores = pickle.load(my_file)
  return RecentScores   
      
    

def PlayGame(Deck, RecentScores):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n'):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard)
    if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  Choice = ''
  AceRank = 'l'
  while Choice != 'q':
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == '5':
      DisplayOptions()
      OptionChoice = GetOptionChoice()
      OptionChoice = SetOptions(OptionChoice)
      if OptionChoice == '1':
        AceRank = SetAceHighOrLow()
    elif Choice == '6':
      SaveScores(RecentScores)
    elif Choice == '7':
      LoadScores()
