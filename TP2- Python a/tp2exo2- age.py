from datetime import datetime as dt

cur_year = dt.today().year
user_age = int(input("Veuillez entrez votre age:"))
def helloworld(_print):
    print(_print)

helloworld(cur_year - user_age)
