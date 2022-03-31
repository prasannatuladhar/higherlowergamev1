from art import logo,vs
import os
game_items = {
  "LeBron James, a Basketball player, from United States.":1123,
  "Ariana Grande, a Musician and actress, from United States.":456,
  "height of mount everest":8849,
  "Dwayne Johnson, a Actor and professional wrestler, from United States.":124,
  "Shawn Mendes, a Musician, from Canada.":325
  }

question_list =[]
value_list = []
for item,val in game_items.items():
  question_list.append(item)
  value_list.append(val)

def compare(first,second):
  user_reply=input("Who has more followers? Type 'A' or 'B':").lower()
  if user_reply=='a' and first>second :
    return 1
  elif user_reply=='b' and first<second:
    return 1
  elif user_reply=='a' and first<second :
    return 0
  else:
    return 0
 
def game():
  print(logo)
  num=0 
  total_score=0
  endofgame = False
  while not endofgame:
    first=question_list[num]
    #handling list over range
    if len(question_list)-1==num:
      num=0
      second=question_list[num]
    else:  
      second=question_list[num+1]
    print(f"Compare A:{first}")
    print(vs)
    print(f"Against B: {second}")
    score = compare(first,second)
    if score==1:
      total_score += score
      num +=1
      os.system("cls") 
      
    else:
      print(f"Sorry that's wrong. Final Score :{total_score}")
      endofgame = True

game()