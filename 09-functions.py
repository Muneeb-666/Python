#Cricket team calculator
def cricket_team_calculator(no_of_players):
    if no_of_players==12:
        print("You are A complete team")
    elif no_of_players<12:
        print("your players are incomplete")
    else:
        print("12 palyers will play and other will be resrved")
cricket_team_calculator(20)

#age calculator

def current_age(birth_year,current_year):
    age=current_year-birth_year
    print("your currnet age is",age)

current_age(2007,2022)

#Python functions (Code with harry)
#1)
def greetings(user_name):
    print("Good day", user_name)
    return 

greetings("muneeb")
  
#Default argument value
def greetings(user_name,name='stranger'):
    print("Good day",user_name,name)
    return 

greetings("Mjneeb")















