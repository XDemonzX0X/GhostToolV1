from requests import post as p
from requests import delete as rdel
from random import choice as ch
import os
from time import sleep
import requests

from utilities.Settings.common import *
from utilities.Settings.libarys import *
from utilities.Settings.update import search_for_updates

import utilities.Plugins.Account_Nuker
import utilities.Plugins.Auto_Login
import utilities.Plugins.DM_Deleter
import utilities.Plugins.Token_Info
import utilities.Plugins.QR_Grabber

w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
rr = Fore.RED
# r = Fore.RESET

#########################################################

def Spinner():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		time.sleep(0.1)

global cls
def cls():
 os.system('cls' if os.name=='nt' else 'clear')

def tool():
  os.system('cls' if os.name=='nt' else 'clear')

def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')

global useragent
def useragent():
    file = open('data/useragent.txt','r')
    useragent = (random.choice(list(file)))
    useragent2 = []
    useragent2.append(useragent)
    useragent1 = []

#########################################################

try:
    with open('data/logins.json') as f:
        config = json.load(f)
except:
    with open('data/logins.json', 'w') as f:
            print(f"\n[{g}#\x1b[95m\x1B[37m] Logging Into GANG-Nuker")
            login = input("[\x1b[95m#\x1b[95m\x1B[37m] Enter A Username: ")
            json.dump({"Login": login}, f, indent=4)
    input(f"\n[\x1b[95m#\x1b[95m\x1B[37m] Successfully Logged in as: [{m}{login}{w}]\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER to Continue: ")
    pass
with open('data/logins.json') as f:
    config = json.load(f)
login = config.get('Login')

languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'aud'   : 'English, Austrlia',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

regions = [
    'brazil',
    'hongkong',
    'india',
    'japan',
    'rotterdam',
    'russia',
    'singapore',
    'southafrica',
    'sydney',
    'us-central',
    'us-east',
    'us-south',
    'us-west'
]


def spammer():
    global threads
    setTitle(f"")
    asc = asyncio.get_event_loop()
    tokens = open('tokens.txt', 'r').read().splitlines()
    clear = lambda: os.system('cls')
    clear()

    colorama.init()
    Write.Print(f'{login}\n', Colors.blue_to_red,  interval=0.000)
    print('')
    print('')
    Write.Print("""
  ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓
 ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒
▒██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░
░▓█  ██▓░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░ 
░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ 
 ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   
   ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░    
   ░ ░   ░  ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░      
         ░  ░  ░  ░    ░ ░        ░               
          
  Version: 1.1.0
  By _GhostCrimm \n\n""", Colors.red_to_blue, interval=0.000)
   
print("\n\n")
def cw(z):
    if z[0:32]!="https://discord.com/api/webhooks":
        return 0
    k=p(z,json={}).json()['code']
    if k==10015 or k==50027:
        return 0
    return 1
def cc(a):
    try:
        c=open(a,"r")
    except:
        return 0
    else:
        u=c.read()
        c.close()
        return u
w=cc("./link")
if not w :
    w=input("Enter the webhook link: ")
if not cw(w):
    print("Bad link.");exit(0)
eo=0
j={}
e={}
while 1:
    if not eo :
        u=input("$")
        if u not in ("quit","help","name","msg","embed","data","send","bomb","","?","pfp","avatar","cfge","cfgi","chat","del"):
            print("Invalid option. Use help for option list.")
        if u=="quit":
            break
        if u=="help" or u=="?":
            Write.Print("Options: \n", Colors.red_to_blue, interval=0.000)
            Write.Print("help - This msg \n", Colors.red_to_blue, interval=0.000)
            Write.Print("name - Webhook name \n", Colors.red_to_blue, interval=0.000)
            Write.Print("msg - The message \n", Colors.red_to_blue, interval=0.000)
            Write.Print("embed - Set embed contents \n", Colors.red_to_blue, interval=0.000)
            Write.Print("data - Preview the json data \n", Colors.red_to_blue, interval=0.000)
            Write.Print("send - Send the message \n", Colors.red_to_blue, interval=0.000)
            Write.Print("bomb - Send the message multiple times \n", Colors.red_to_blue, interval=0.000)
            Write.Print("chat - Send messages like a chat \n", Colors.red_to_blue, interval=0.000)
            Write.Print("del - Deletes a webhook \n", Colors.red_to_blue, interval=0.000)
            Write.Print("cfge - Save the data in a file \n", Colors.red_to_blue, interval=0.000)
            Write.Print("cfgi - Import the data from the saved file \n", Colors.red_to_blue, interval=0.000)
            Write.Print("pfp - picture of the webhook \n", Colors.red_to_blue, interval=0.000)
            Write.Print("quit - Exit \n", Colors.red_to_blue, interval=0.000)
        if u=="cfge":
            ex=open("./f.txt","w")
            ex.write(str(j))
            ex.close()
            print("Saved!")
        if u=="del":
            if input("Are you sure? ")=="yes":
                rq=rdel(w);os.remove("./link")
                if rq.status_code==204:
                    break
                print(f"{rq.json()['code']},{rq.json()['message']}")
        if u=="cfgi":
            im=cc("./f.txt")
            if not im:
                print("File not found");continue
            j=eval(im)
            e=j["embeds"][0]
            print("Imported!")
        if u=="data":
            print(j)
        if u=="chat":
            d={}
            while 1:
                m=input("chat>")
                m=m.strip()
                if m=="exit":
                    break
                if m=="name":
                    d["username"]=input("Enter the username: ");continue
                d["content"]=m
                r=p(w,json=d)
                if r.status_code == 204:
                    print("Sent!");continue
                print(f"Error: Code: {r.status_code}, Text: {r.json()['message']}")
        if u=="send":
            if "embeds" in j:
                if ("color" not in j["embeds"][0]) and (j["embeds"][0]!={}):
                    j["embeds"][0]["color"]=''.join([ch("0123456789") for _ in range(7)])
            r=p(w,json=j)
            if r.status_code == 204:
                print("Sent!");continue
            print(f"Error, code:{r.status_code}")
        if u=="bomb":
            n=0
            t=0
            l=int(input("Enter limit: "))
            rd=input("Randomize name? [Y for yes, no otherwise] ")
            while n<l:
                if rd=="Y":
                    j["username"]=''.join([ch("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$&_-()+[]{}<>") for w in range(36)])
                s=p(w,json=j)
                if(s.status_code==204) :
                    n+=1
                if(s.status_code==429):
                    t+=1
                print(f"Sent {n}/{l}, {t} rate limits",end='\r')
            print("\n")
        if u=="name":
            j["username"]=input("Enter the webhook name: ")
        if u=="msg":
            j["content"]=input("Enter the text content: ")
        if u=="pfp" or u=="avatar":
            j["avatar_url"]=input("Enter the avatar url: ")
        if u=="embed":
            eo=1
        continue
    u=input("embed>")
    if u not in ("help","title","desc","color","author","footer","img","image","?","tbn","data","reset","save","exit","","cfge","cfgi") :
        print("Invalid option. Use help for option list.")
    if u=="help" or u=="?":
        print("help - This msg")
        print("title - The title")
        print("desc - The description")
        print("color - The color")
        print("author - Author")
        print("footer - Footer")
        print("img - Image url")
        print("tbn - Thumbnail url")
        print("data - Preview the json data")
        print("cfge - Save the data in a file")
        print("cfgi - Import the data from the saved file")
        print("reset - Empty the embed data")
        print("save - Set the embed and exit")
        print("exit - Exit the embed editor without saving")
    if u=="exit":
        eo=0;continue
    if u=="reset":
        e={}
    if u=="cfge":
        ex=open("./e.txt","w")
        ex.write(str(e))
        ex.close()
        print("Saved!")
    if u=="cfgi":
        im=cc("./e.txt")
        if not im:
            print("File not found");continue
        e=eval(im)
        print("Imported!")
    if u=="title":
        e["title"]=input("Enter the title: ")
    if u=="desc":
        e["description"]=input("Enter the description: ")
    if u=="save":
        eo=0;j["embeds"]=[e]
        if e=={}:
            del j["embeds"]
    if u=="data":
        print(e)
    if u=="color":
        e["color"]=str(int(input("Enter a HEX color: "),16))
    if u=="author":
        t={"name":input("Enter author name: ")}
        r=input("Enter author url ( - for none ): ")
        if r != "-" :
            t["url"]=r
        r=input("Enter author icon url ( - for none ): ")
        if r != "-" :
            t["icon_url"]=r
        e["author"]=t
    if u=="footer":
        t={"text":input("Enter footer text: ")}
        r=input("Enter footer icon url ( - for none ): ")
        if r != "-" :
            t["icon_url"]=r
        e["footer"]=t
    if u=="img" or u=="image":
        e["image"]={"url":input("Enter image url: ")}
    if u=="tbn":
        e["thumbnail"]={"url":input("Enter image url: ")}