#!/usr/bin/python3
#By: Discord "Aerospace_Dev#0007"
#
from time import sleep
from os import system, name
from sys import exit
from random import choice, randint
try:
    from requests import get
except Exception as EEEE:
    print(str(EEEE));w=input("install 'requests' and restart - Hit enter to exit")
    exit(0)
        
class user:
    class settings:
        try:
            f = open("settings.aero","r");settings = str(f.read())
        except Exception as EEE:
            print(str(EEE))
        max_fails = 150 #<<<<#################################################################<<<<<<<<<<MAX Failed Requests Allowed<<<<<<<<<<<<||||||||||||||||||||||||||||||||||||||||||||||
        max_fails_stdout = str(max_fails)
        debug_mode = False #<<<<############################################################<<<<<<<<<<<Enable Debug Mode ["True" or "False"]<<<<<<<<<<<||||||||||||||||||||||||||||||||||||||||||||||
        timeout = 8 #<<<<####################################################################<<<<<<<<<<<Set Timeout (In seconds) For Requests<<<<<<<<<<<|||||||||||||||||||||||||||||||||||||||||||||
        api = "https://api.aero-bot.pro/api/proxies.txt" #<<<<####################################<<<<<<<<<<< Set API! Ours Is a SOCKS-like Proxy like proxyscrape-BETA <<<<<<<<<<<|||||||||||||||||||||||||||||||||||||||||||||

def logo_and_setup():
        #ACME Progress Bar
        print("Setting up  U N I Q U E   V I S I T O R... [#       ]\r", end="");sleep(.2);print("Setting up  U N I Q U E   V I S I T O R... [##      ]\r", end="");sleep(.2);print("Setting up  U N I Q U E   V I S I T O R... [###     ]\r", end="");sleep(.2);print("Setting up  U N I Q U E   V I S I T O R... [####    ]\r", end="");sleep(.2);print("Setting up  U N I Q U E   V I S I T O R... [#####   ]\r", end="");sleep(.2);print("Setting up  U N I Q U E   V I S I T O R... [######  ]\r", end="");sleep(.2);print("Setting up  U N I Q U E   V I S I T O R... [####### ]\r", end="");sleep(.2);print("Setting up  U N I Q U E   V I S I T O R... [########]\r", end="");sleep(.2)
        if name == 'nt': _ = system('cls')
        else: _ = system('clear')
        try:
            with open("logo.aero", "r") as file:
                print(file.read())
        except Exception as E:
            print(str(E))
            pass
                            
class user_agent:
    def get_headers():
        useragents = [
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/57.0.2987.110 '
         'Safari/537.36'),  # chrome
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/61.0.3163.79 '
         'Safari/537.36'),  # chrome
        ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
         'Gecko/20100101 '
         'Firefox/55.0'),  # firefox
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/61.0.3163.91 '
         'Safari/537.36'),  # chrome
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/62.0.3202.89 '
         'Safari/537.36'),  # chrome
        ('Mozilla/5.0 (X11; Linux x86_64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/63.0.3239.108 '
         'Safari/537.36'),  # chrome
        ]
        user_agent = choice(useragents)
        headers = {'User-Agent' : user_agent}
        return headers

###NEEDS ERROR HANDLING IN CASE OF BAD API < [BELOW]
class proxies:
    def get():
        try:
            prox = get(user.settings.api);form = prox.text.split("\n");thing = {}
            for i in form:
                thing.update({"http" : str('http://'+str(i))})
        except Exception as E:
            print(str(E))
        return thing
            
        
    
class visitor:
    def visit(url, lag, runs):
        count = 0;err_count = 0;succ_visits = 0;new_id = 0;ers_remaining1 = ""
        for x in range(0, runs):
            bError = False;count += 1;count_str = str(count)
            try:
                ip = get("http://bot.whatismyipaddress.com/", headers=user_agent.get_headers(), proxies=proxies.get(), timeout=user.settings.timeout);my_ip=ip.text
                if len(my_ip) > 20:
                    my_ip = "127.0.0.1"
                ers_remaining1 = str(int(user.settings.max_fails - err_count))
                print(f"\nUsing New Identity: {my_ip} / User-Agents: Rotated\n\nTrying To Visit...")
            except Exception as Error:
                bError = True
                if name == 'nt': _ = system('cls')
                else: _ = system('clear')
                new_id += 1
                print(f"""
[X] - Bad Node...Renewing Identity!

                        Overall Attempts: {count_str}
                        Successful Visits: {str(succ_visits)}
                        Failed Visits: {str(err_count)}
                        Failed Visits Remaining: {ers_remaining1}
                        Identities Used: {str(new_id)}
                        """)
                if user.settings.debug_mode == True:
                    print(str(Error));stop = input("STOPPED - DEBUGGING")
                pass
            if bError == False:
                sleep(lag)
                try:
                    r = get(url, headers=user_agent.get_headers(), proxies=proxies.get(), timeout=user.settings.timeout)
                except Exception as dd:
                    bError = True;err_count += 1
                    if user.settings.debug_mode == True:
                        print(str(er));stop = input("STOPPED - DEBUGGING")
                        pass
                if err_count > user.settings.max_fails:
                    if name == 'nt': _ = system('cls')
                    else: _ = system('clear')
                    print(f"\nERROR! - [Run Count: {count_str}] - {user.settings.max_fails_stdout} Attepts Exceeded! - Exiting To Start!")
                    bError = True
                    break
                else:
                    if bError == False:
                        stat = str(r.status_code)
                        if name == 'nt': _ = system('cls')
                        else: _ = system('clear')
                        print(f"\n\n[Visited!] - [Run Count: {count_str}] \n-\n Status Code: {stat} \n-\n Our IP: {my_ip}")
                        succ_visits += 1;ting=str(succ_visits);ers_remaining = str(int(user.settings.max_fails - err_count))
                        print(f"""
                        Overall Attempts: {count_str}
                        Successful Visits: {ting}
                        Failed Visits: {str(err_count)}
                        Failed Visits Remaining: {ers_remaining}
                        Identities Used: {str(new_id)}
                        """)
        print(f"\n\nCompleted {count_str} runs!.")
    
def startup_print():
    start = input("\nHit Enter To Start!--->")
    sleep(.2);print("<-------------------|>\r", end="")
    sleep(.2);print("<-------------------\\>\r", end="")
    sleep(.2);print("<------------------_->\r", end="")
    sleep(.2);print("<----------------/--->\r", end="")
    sleep(.2);print("<--------------|----->\r", end="")
    sleep(.2);print("<------------\\------->\r", end="")
    sleep(.2);print("<----------_--------->\r", end="")
    sleep(.2);print("<-------/------------>\r", end="")
    sleep(.2);print("<----|--------------->\r", end="")
    sleep(.2);print("<---\\---------------->\r", end="")
    sleep(.2);print("<--_----------------->\r", end="")
    sleep(.2);print("<-/------------------>\r", end="")
    sleep(.2);print("<|------------------->\r", end="")
    sleep(.2);print("<\\------------------->\r", end="")
    sleep(.2);print("<_------------------->\r", end="")
    sleep(.2);print("</------------------->\r", end="")
    sleep(.2);print("<|------------------->\r", end="")
    sleep(.2);print("<\\------------------->\r", end="")
    sleep(.2);print("<_------------------->\r", end="")
    sleep(.2);print("</------------------->\r", end="")
    sleep(.2);print("<|------------------->\r", end="")
    sleep(.2);print("<-/------------------>\r", end="")
    sleep(.2);print("<--_----------------->\r", end="")
    sleep(.2);print("<---\\---------------->\r", end="")
    sleep(.2);print("<----|--------------->\r", end="")
    sleep(.2);print("<-------/------------>\r", end="")
    sleep(.2);print("<----------_--------->\r", end="")
    sleep(.2);print("<------------\\------->\r", end="")
    sleep(.2);print("<--------------|----->\r", end="")
    sleep(.2);print("<--------------/----->\r", end="")
    sleep(.2);print("<--------------_----->\r", end="")
    sleep(.2);print("<--------------\\----->\r", end="")
    sleep(.2);print("<-----------------|-->\r", end="")
    sleep(.2);print("<------------------/->\r", end="")
    sleep(.2);print("<-------------------_>\r", end="")
    sleep(.2);print("<-------------------\\>\r", end="")
    sleep(.2);print("<-------------------|>\r", end="")

        
def do():
    try:
        place_going = input("""\nEnter URL To Visit (HTTP ONLY ):\n
+----------------------------------------------+\n
http://""")
        
    except Exception as eE:
        print(str(eE))
        main()
    if name == 'nt': _ = system('cls')
    else: _ = system('clear')    
    url = f"http://{place_going}"
    print("\nChecking URL So We Dont Waste Our Time...")
    try:
        r = get(url);print("\nStatus Code: "+str(r.status_code))
        content = r.headers["Content-Type"];connection = r.headers["Connection"];cookie = r.headers["Set-Cookie"]
        print("\nSome Error/s are normal right here <<")
        print(f"""
    Header Info For {url}:
---------------------------------------------
Connection:
{connection}

Cookie:
{cookie}

Content-Type:
{content}
---------------------------------------------
""")
        accept = input("||> < Press Enter To Accept > <||")
        if name == 'nt': _ = system('cls')
        else: _ = system('clear')  
    except Exception as EEE:
        print(str(EEE))
        pass     
    try:
        lag = int(input("\nEnter Lag Time Between Visits (In Seconds ):"))
        if name == 'nt': _ = system('cls')
        else: _ = system('clear') 
        runs = int(input("\nEnter Loop Amount: "))
        if name == 'nt': _ = system('cls')
        else: _ = system('clear')
        start = input("\nHit Enter To Start!--->")
        startup_print() # COMMENT OUT TO REMOVE STARTUP PRINT
    except Exception as d:
        print(str(d))
        main()
    try:
        visitor.visit(url, lag, runs)
    except Exception as D:
        print(str(D))
        pass
    enter = input("\n\n\n\n----------------------------------\nCOMPLETE\n----------------------------------\n\nPress Enter To Restart Or CTRL-C/Z To Exit.")
    main()

    
def main():
    logo_and_setup()
    do()
    idied_peacefully = exit(0)
    return idied_peacefully


def startup_print():
    sleep(.09);print("<-------------------|>\r", end="");sleep(.09);print("<-------------------\\>\r", end="");sleep(.09);print("<------------------_->\r", end="");sleep(.09);print("<----------------/--->\r", end="");sleep(.09);print("<--------------|----->\r", end="");sleep(.09);print("<------------\\------->\r", end="");sleep(.09);print("<----------_--------->\r", end="");sleep(.09);print("<-------/------------>\r", end="");sleep(.09);print("<----|--------------->\r", end="");sleep(.09);print("<---\\---------------->\r", end="");sleep(.09);print("<--_----------------->\r", end="");sleep(.09);print("<-/------------------>\r", end="");sleep(.09);print("<|------------------->\r", end="");sleep(.09);print("<\\------------------->\r", end="");sleep(.09);print("<_------------------->\r", end="");sleep(.09);print("</------------------->\r", end="");sleep(.09);print("<|------------------->\r", end="");sleep(.09);print("<\\------------------->\r", end="");sleep(.09);print("<_------------------->\r", end="");sleep(.09);print("</------------------->\r", end="");sleep(.09);print("<|------------------->\r", end="");sleep(.09);print("<-/------------------>\r", end="");sleep(.09);print("<--_----------------->\r", end="");sleep(.09);print("<---\\---------------->\r", end="");sleep(.09);print("<----|--------------->\r", end="");sleep(.09);print("<-------/------------>\r", end="");sleep(.09);print("<----------_--------->\r", end="");sleep(.09);print("<------------\\------->\r", end="");sleep(.09);print("<--------------|----->\r", end="");sleep(.09);print("<--------------/----->\r", end="");sleep(.09);print("<--------------_----->\r", end="");sleep(.09);print("<--------------\\----->\r", end="");sleep(.09);print("<-----------------|-->\r", end="");sleep(.09);print("<------------------/->\r", end="");sleep(.09);print("<-------------------_>\r", end="");sleep(.09);print("<-------------------\\>\r", end="");sleep(.09);print("<-------------------|>\r", end="")
    
main()    
