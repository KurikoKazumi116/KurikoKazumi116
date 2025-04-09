import random
print("WELCOME TO GUESS THE NUMBER!!\nCHOOSE YOUR DIFFICULTY LEVEL!")
print("Easy, Medium, Hard")
diff = input("> ")
chances = 0
num = random.randint(1,100)

if diff == "Easy":
    chances = 10
    guesses = 0
    print("YOU HAVE CHOSEN EASY LEVEL!")
    while chances > 0:
          guess = input("PICK A NUMBER BETWEEN 1 AND 100!")
          if int(guess) == num:
              guesses +=1
              print("Correct!")
              print("It took you",guesses,"guesses")
              break
          else:
              print("Incorrect.")
              chances -= 1
              guesses += 1
              if num > int(guess):
                  print("Too low")
              elif num < int(guess):
                  print("Too high")
    print("Game over")   

if diff == "Medium":
    chances = 5
    guesses = 0
    print("YOU HAVE CHOSEN MEDIUM LEVEL!")
    while chances > 0:
          guess = input("PICK A NUMBER BETWEEN 1 AND 100!")
          if int(guess) == num:
              guesses +=1
              print("Correct!")
              print("It took,", guesses," guesses")
              break
          else:
              guesses +=1
              print("Incorrect.")
              chances -= 1
              if num > int(guess):
                  print("Too low")
              elif num < int(guess):
                  print("Too high")
    print("Game over")

if diff == "Hard":
    chances = 3
    guesses = 0
    print("YOU HAVE CHOSEN HARD LEVEL!")
    while chances > 0:
          guess = input("PICK A NUMBER BETWEEN 1 AND 100!")
          if int(guess) == num:
              guesses +=1
              print("Correct!")
              print("It took,", chances," guesses")
              break
          elif guess != num:
              guesses +=1
              print("Incorrect.")
              chances -= 1
              if num > int(guess):
                  print("Too low")
              elif num < int(guess):
                  print("Too high")
    print("Game over")        

   
  
        
       
   
