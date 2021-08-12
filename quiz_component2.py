def quiz_question(question):
  valid=False
  while not valid:
    user_response = input (question) .lower()

    if user_response == "whero":
        user_response = "whero"
        return user_response 

    else:
      print("Incorrect, try again") 

def quiz_question2(question):
  valid=False
  while not valid:
    user_response = input (question) .lower()

    if user_response == "awa":
        user_response = "awa"
        return user_response 

    else:
      print("Incorrect, try again") 



qna_whero = quiz_question ("What’s red in Te Reo Maaori?\n")

if qna_whero == "whero":
  print("Correct")
  print()

else:
  print("Incorect, try again")
  print()

qna_awa = quiz_question2 ("What’s ocean in Te Reo Maaori?\n")

if qna_awa == "awa":
  print("Correct")
  print()

else:
  print("Incorect, try again")
  print()
