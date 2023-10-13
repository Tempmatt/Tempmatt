from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

print("Welcome to the secret auction program.")

auction_on = True
dic = {}

def func(diction):
  highest_num = 0
  winner = ""
  for loop in diction:
    bid = diction[loop]
    if bid > highest_num:
      highest_num = bid
      winner = loop
  print(f"The winner is {winner} with a bid of ${highest_num}.")


while auction_on:
  
  auction_name = input("What is your name?: ").lower()
  bid_price = int(input("What is your bid?: $"))
  dic[auction_name] = bid_price
  no_of_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
  
  if no_of_bidders == "no":
    auction_on = False
    func(diction=dic)
  elif no_of_bidders == "yes":
    clear()
    print(logo)
