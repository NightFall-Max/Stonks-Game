import random
import time
from colorama import Style, Fore

bold = Style.BRIGHT
dim = Style.DIM
reset = Style.RESET_ALL
blue = Fore.BLUE
lightblue = Fore.LIGHTBLUE_EX
lightmagenta = Fore.LIGHTMAGENTA_EX
magenta = Fore.MAGENTA
cyan = Fore.CYAN
lightcyan = Fore.LIGHTCYAN_EX
white = Fore.WHITE
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
lightyellow = Fore.LIGHTYELLOW_EX
reset = Style.RESET_ALL
bold = Style.BRIGHT
dim = Style.DIM

print(
  f"{lightblue}In this game your goal is to buy low and sell high for {bold}HUGE{reset}{lightblue} gains in the stock market"
 )
while True:
  try:
    days = int(input(
      f"\n{lightblue}How many days would you like to play the stock market for?: \n"))
    break
  except ValueError:
    print(
      f"-\n{red}Please input integer only...")  
    print("----------")

time.sleep(0.25)

def c():
  print("\033c", end="", flush=True) #faster clearing

c()

i=0
average=0
avg=0
times=0
share=0
bal=1000

while i < int(days):
  left=int(days)-i
  print(
    f"{bold}{yellow} ____  _____ |||||| ______     __   __    ____\n/        |   |    | |     |   | |  / /   /     \n|        |   |    | |     |   | | / /    |     \n ----    |   |    | |     |   | |/ /      ---- \n     |   |   |    | |     |   | |_ _          |\n    /    |   |    | |     |   | | _ _        / \n----     |   |||||| |     |   | |  _ _   ----  ")
  print(
    f"{white}\n============================================================================================\n")
  print(f"{blue}Days Left: "+str(left), end='   -   ')
  print(f"{green}Balance: $"+str(bal), end='   -   ')
  print(f"{blue}Shares: "+str(share), end='   -   ')
  print(f"{green}Average Buy Cost: $"+str(avg))
  print(" \n")
  stock=random.randint(1,1100)
  print("Today's stock price: $"+str(stock))
  i=i+1
  maxbuy=(bal/stock)
  maxbuy=int(maxbuy)
  invest=str(input(f"{lightblue}\nWhat would you like to do?    Buy(1)?    Sell(2)?    Or wait to the next day(3)?\n\nYour Choice?: "))
  print("\n----------")
  if(invest=="1"):
    print("The max amount of shares you can buy is: "+str(maxbuy)+"\n----------")
    print("If you want to buy max shares type '12345'.\n-")
    amount=int(input("How many shares would you like to buy?: "))
    print("----------")
    if(str(amount)=="12345"):
      amount=maxbuy
    elif(amount>maxbuy):
      print("----------\nHEY THERE! STOP! Do you forget? You don't have enough money... I'm buying the max amount you can afford instead.")
      amount=maxbuy
      time.sleep(1.75)
    elif(amount<0):
        
      print("As a result, I'm skipping this day!")
      amount=0
      time.sleep(5)
    bal=(bal-amount*stock)
    share=(share+amount)
    if(maxbuy>0):
      if(amount>0):
        if(amount==12345):
          times=times+1
          average=average+stock
        else:
          times=times+1
          average=average+stock

  elif(invest=="2"):
    print("The max amount of shares you can sell is "+str(share)+".\n----------")
    print("If you would like to sell all of your shares type '12345', else...")
    sell=int(input("\nHow many shares would you like to sell?: \n"))
    if(str(sell)=="12345"):
      sell=share
      bal=bal+sell*stock
      share=share-sell
    elif(sell>share):
      print("----------\n\nBRUH how are you supposed to sell the money you don't even OWN?\n\n----------")
      time.sleep(1.5)
    elif(sell<0):
      print("As a result, I'm skipping this day!")
      time.sleep(5)
    else:
     bal=bal+sell*stock
     share=share-sell
  else:
    print("You skipped the day... Don't you feel USELESS sometimes?!")
    time.sleep(0.675)
  if(times>0):
    avg=average/times
    avg=int(avg)
  c()
    
if(share>0):
  lprice=random.randint(50,1050)
  print("Last day's stock price: "+str(lprice)+"\n----------")
  convert=int(input("Would you like me to convert your shares to dollars using the last share price? Yes(1) No(2): "))
  if(convert==1):
    bal=(bal+share*int(lprice))
    share=0

print("----------\n\nYou have 0 days left to make money. Lets see how you did!\n\n----------")

print(f"{red}\nAfter "+str(days)+" day you have $"+str(bal)+" dollars you started with $1000 do the math yourself.\n\n-")
print(f"{red}\nYou own "+str(share)+" shares.\n\n----------")
if(bal<1000):
  print(f"{green}\n\nYOU LOST THE MONEY!!! Oh well... Back to McDonald's I guess...")
elif(bal==1000):
  print(f"{red}\n\nAre you sure that you played the game at all?!?!?!")
elif(bal<1000000):
  print(f"{green}\n\nPretty good but I think you can do better, maybe if you play for longer?!")
elif(bal<1000000000):
  print(f"{bold}{green}\n\nWOW WOW WOW, very good indeed. Very stonks!")
elif(bal<1000000000000):
  print(f"{bold}{green}\n\nCan you teach me your ways? Because that was amazing!")
else:
  print(f"{bold}{blue}\n\nVERY VERY Impressive!!! Now just do that in the real world and you will be set ;)")