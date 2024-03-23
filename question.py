
questions = ["Please describe any medication needs ",
             "Please describe any transportation needs ",
             "Please describe any specific needs ",
             "Please describe any dietary restrictions or preferences",
             "What hobbies or interests do you have? "]

basic = ["What is your caretaker gender preference? ",
         "What is your caretaker age preference? ",
         "What language do you primarily speak? ",
         "Who should the caretaker contact in case of an emergency? (email or phone number) ",
         "When in the day do you need assistance? (time range) ",
         "What city are you located in? "]

print('Hello! We would like to collect some data on your preferences')
for question in questions:
    print(question)
    response = input()
    print(response)
    # extract
