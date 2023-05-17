from art import logo
from replit import clear
import random 
def logo_design():
  print(logo)
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
def check_score(lists):
  if(sum(lists)==21 and len(lists)==2):
    return 0
  if(sum(lists)>21 and 11 in user_card):
    user_card.remove(11)
    user_card.append(1)
  return sum(lists)
def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"
while True:
  ans=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  user_card=[]
  computer_card=[]
  if(ans=="y"):
    clear()
    logo_design()
    for _ in range(0,2):
      user_card.append(deal_card())
      computer_card.append(deal_card())
    # print(user_card)  
    ans_check = check_score(user_card)
    ans_check1 = check_score(computer_card)
    print(f"   Your cards: {user_card}, current score: {ans_check}")
    print(f"   Computer's first card: {computer_card[0]}")
    
    # print(ans_check)
    # print(user_card)
    while True:
      ans_repete = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if(ans_repete=="y"):
        user_card.append(deal_card())
        ans_check = check_score(user_card)
        ans_check1 = check_score(computer_card)
        if ans_check1<17 and ans_check1!=0:
          computer_card.append(deal_card())
        
      elif(ans_repete=="n"):
        print(f"   Your final hand: {user_card}, final score: {ans_check}")
        print(f"   Computer's final hand: {computer_card}, final score: {ans_check1}")
        print(compare(ans_check, ans_check1))
        break
    # print(computer_card)
    
    
  else:
    break
