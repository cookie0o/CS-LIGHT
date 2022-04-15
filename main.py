
# cs-light a low performance csgo cheat



#imports
from colorama import init, Fore, Back
init(autoreset=True)
import os
import time
import pymem
import pymem.process
import configparser
from datetime import datetime
import keyboard
import secrets
import ctypes
import re
import gc
#import offsets
from offsets.OFFSETS import *

#clear cmd and checking if computer is linux or windows 
#basically this cheat is for windows but idk who uses linux so maby this cheat works for it too but idk again
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


#define version an dev
PROCESS_NAME = "csgo.exe"
VERSION      = "v1.1"
DEV          = "cookie0_o github: https://github.com/cookie0o"

#get current path
dirname = os.path.dirname(__file__)

#def colors
BLUE = Fore.BLUE
RED = Fore.RED
GREEN = Fore.GREEN
CYAN = Fore.CYAN
light_GREEN = Fore.LIGHTGREEN_EX
light_RED = Fore.LIGHTRED_EX

#start
def main():

    # +[CREATE LOGS]
    print (f"{light_GREEN}-[info] loading log file")
    log_file_path = os.path.join(dirname, 'logs/logs.txt')
    log_file = open(log_file_path, "w")
    print (f"{light_GREEN}-[info] log file path {log_file_path}")

    log_file.write(f"""                      CS-LIGHT-{VERSION}
       dev;{DEV}
##############################LOGS##############################
\n""")

    log_file.write(f"[info- {datetime.now()}] hack started\n")
    log_file.write(f"[info- {datetime.now()}] loaded log file\n")


    #load config
    config = configparser.ConfigParser()
    CONFIG_PATH = os.path.join(dirname, 'config.ini')
    config.read(CONFIG_PATH)
    log_file.write(f"[info- {datetime.now()}] loaded config file\n")


    #clear cmd
    clear()

    #change cmd title
    ctypes.windll.kernel32.SetConsoleTitleW(f"ACCEPT LEGAL DISCLAIMER - CS-LIGHT ✳ {VERSION} ✳ {DEV}")


    # +[LEGAL DISCLAIMER]
    
    #check if legal discplaimer was already accepted

    #check for file in logs with name legal_disclaimer_accepted.txt
    if os.path.isfile(os.path.join(dirname, 'logs/legal_disclaimer_accepted.txt')):
        print (f"{light_GREEN}-[info] legal disclaimer was already accepted")
        show_disclaimer_on_off = "OFF"
    else:
        show_disclaimer_on_off = "ON"
        
    


    if show_disclaimer_on_off == "ON":
        print (f"""{light_RED}\
----------LEGAL DISCLAIMER----------
:I`m not responsable for::
Using this software for illegal purposes.
Getting baned bec. of this software on any platform usw.
And all other things that may happen.
!!THIS SOFTWARE IS WITHOUT WARRANTY!!

you agree (YES/NO)""")
        agree_disclaimer = input ("")
        
        if agree_disclaimer == "YES":
            log_file.write(f"[info- {datetime.now()}] legal disclaimer accepted\n")

            # generate file in logs folder and name it legal disclaimer accepted
            with open(os.path.join(dirname, 'logs/legal_disclaimer_accepted.txt'), 'w') as f:
                f.write("legal disclaimer accepted skiping disclaimer on next start")
            f.close()    
            pass

        elif agree_disclaimer == "NO":
            log_file.write(f"[info- {datetime.now()}] legal disclaimer declined: EXITING APP\n")
            exit() 
    else:
        pass


    # +[MAIN PART]
    #clear cmd
    clear()

    #reading/write cfg
    print (f"{light_GREEN}-[INFO] Read config from [config.ini]...")

    esp_on_off = config["-ESP-"]["esp_on"]
    radar_on_off = config["-RADAR-"]["radar_on"]
    noflash_on_off = config["-NOFLASH-"]["noflash_on"]
    bunnyhop_on_off = config["-BUNNYHOP-"]["bunnyhop_on"]
    money_reveal_on_off = config["-MONEY-REVEAL-"]["money_reveal_on"]

    raw_delay = config["-SECONDS-DELAY-"]["delay"]
     
    T_R = config["T_COLOR"]["T_Red"]
    T_G = config["T_COLOR"]["T_Green"]
    T_B = config["T_COLOR"]["T_Blue"]

    CT_R = config["CT_COLOR"]["CT_Red"]
    CT_G = config["CT_COLOR"]["CT_Green"]
    CT_B = config["CT_COLOR"]["CT_Blue"]


    #get time and format it
    time_now = datetime.now()
    CURRENT_TIME = time_now.strftime("%H:%M:%S")

    #changing cmd title
    ctypes.windll.kernel32.SetConsoleTitleW(f"CS-LIGHT ✳ {VERSION} ✳ {DEV}")

    #print title and start screen
    print (f"{light_GREEN}-[INFO] developer; [{DEV}]")
    print (f"""{RED}\

░█████╗░░██████╗░░░░░░██╗░░░░░██╗░██████╗░██╗░░██╗████████╗
██╔══██╗██╔════╝░░░░░░██║░░░░░██║██╔════╝░██║░░██║╚══██╔══╝
██║░░╚═╝╚█████╗░█████╗██║░░░░░██║██║░░██╗░███████║░░░██║░░░
██║░░██╗░╚═══██╗╚════╝██║░░░░░██║██║░░╚██╗██╔══██║░░░██║░░░
╚█████╔╝██████╔╝░░░░░░███████╗██║╚██████╔╝██║░░██║░░░██║░░░
░╚════╝░╚═════╝░░░░░░░╚══════╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░""")
    print (f"{CYAN}- The best low performance cs:go cheat [{VERSION}]  [{CURRENT_TIME}] -")
    print (" ")

    #show cfg;
    print (f"""{BLUE}\
----------[CONFIG]----------""")
    print (f"""{light_RED}\
[-ESP-]          =       {esp_on_off}
[-RADAR-]        =       {radar_on_off}
[-NOFLASH-]      =       {noflash_on_off}
[-BUNNYHOP-]     =       {bunnyhop_on_off}
[-MONEY-REVEAL-] =       {money_reveal_on_off}
(loop delay)     =       {raw_delay}sec.
""")
    print (" ")
    print (f"{BLUE}press [P] to deject.")
    print (" ")
    log_file.write(f"[info- {datetime.now()}] showed activated cheats and title.\n")

    #clear memory
    gc.collect()
    log_file.write(f"[info- {datetime.now()}] memory cleared.\n")


    #check if csgo was started and get the dlls
    print (f"{light_GREEN}-[INFO] checking if csgo was started and getting values.")

    #check if csgo was started
    def check_if_csgo_is_open():
        time.sleep(1)

        #check if csgo is open
        try:
            pm=pymem.Pymem(PROCESS_NAME)

        # csgo not ruing waiting for start
        except:
            print (f"{RED}-[ERROR] Pls start {PROCESS_NAME}.", end='\r')
            check_if_csgo_is_open()

        # csgo was started pass
        finally:
            time.sleep(15)
            print (f"{light_GREEN}-[INFO] csgo was found.     ", end='\r')
            log_file.write(f"[info- {datetime.now()}] csgo was found.\n")
            pass

    check_if_csgo_is_open()

    try:
        pm=pymem.Pymem(PROCESS_NAME)
        log_file.write(f"[info {datetime.now()}] getting dlls and offsets\n")
        client=pymem.process.module_from_name(pm.process_handle,'client.dll').lpBaseOfDll
        engine=pymem.process.module_from_name(pm.process_handle,'engine.dll').lpBaseOfDll

        player = pm.read_int(client + dwLocalPlayer)
        localplayer = pm.read_int(client + dwLocalPlayer)
        pass

    except pymem.exception.ProcessNotFound:
        print (f"{RED}-[ERROR] Pls start {PROCESS_NAME} and restart the cheat.")
        log_file.write(f"[info- {datetime.now()}] cs:go not found: EXITING APP.\n")
        

    # +[RUN CHEATS]
    print (f"{light_GREEN}-[INFO] starting cheat loop.")

    ## CHEATS ##

    #money-reveal
    if money_reveal_on_off == "ON":
        log_file.write(f"[info- {datetime.now()}] activating money reveal\n")
        client_money_reveal = pymem.process.module_from_name(pm.process_handle, 'client.dll')
        clientModule = pm.read_bytes(client_money_reveal.lpBaseOfDll, client_money_reveal.SizeOfImage)
        address = client_money_reveal.lpBaseOfDll + re.search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF', clientModule).start()
        pm.write_uchar(address, 0xEB if pm.read_uchar(address) == 0x75 else 0x75)
        log_file.write(f"[info- {datetime.now()}] money reveal activated\n")
    else:
        pass

    #making the delay string to float
    delay = float(raw_delay)
    log_file.write(f"[info- {datetime.now()}] converted delay str to float\n")

    cheat_loop = 1
    log_file.write(f"[info- {datetime.now()}] cheat loop started\n")
    count_raw = 0
    while cheat_loop == 1:


        try:

            #clear memory to avoide vac detections or help i guess
            gc.collect()
            log_file.write(f"[info- {datetime.now()}] memory cleared.\n")
            

            #delay so cheat uses less cpu
            time.sleep(delay)

            #deject
            if keyboard.is_pressed("P"):
                if money_reveal_on_off == "ON":
                    client_money_reveal = pymem.process.module_from_name(pm.process_handle, 'client.dll')
                    clientModule = pm.read_bytes(client_money_reveal.lpBaseOfDll, client_money_reveal.SizeOfImage)
                    address = client_money_reveal.lpBaseOfDll + re.search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF', clientModule).start()
                    pm.write_uchar(address, 0xEB if pm.read_uchar(address) == 0x75 else 0x75)
                    cheat_loop = 0
                    print (f"{light_GREEN}-[INFO] Cheat dejected.")
                    log_file.write(f"[info- {datetime.now()}] cheat dejected\n")
                    print(" ")
                    print (f"{BLUE} do you want to restart the cheat or exit? type RESTART or EXIT")
                    restart_or_exit = input("")
                    if restart_or_exit == "RESTART":
                        log_file.write(f"[info- {datetime.now()}] exiting cheat\n")
                        main()
                    else:
                        log_file.write(f"[info- {datetime.now()}] exiting cheat\n")
                        exit()
                else:
                    cheat_loop = 0
                    print (f"{light_GREEN}-[INFO] Cheat dejected.")
                    log_file.write(f"[info- {datetime.now()}] cheat dejected\n")
                    print(" ")
                    print (f"{BLUE} do you want to restart the cheat or exit? type RESTART or EXIT")
                    restart_or_exit = input("")
                    if restart_or_exit == "RESTART":
                        log_file.write(f"[info- {datetime.now()}] restarting cheat\n")
                        log_file.write(f" ")
                        main()
                    else:
                        log_file.write(f"[info- {datetime.now()}] exiting cheat\n")
                        log_file.write(f" ")
                        exit()


            else:
                pass
                    
            #no flash
            if noflash_on_off == "ON":
                if player:
                    flash_value=player+m_flFlashMaxAlpha
                    if flash_value:
                        pm.write_float(flash_value,float(0))
            else:
                pass

            #radar
            if radar_on_off == "ON":
                for i in range(1,32):
                    entity=pm.read_int(client+dwEntityList+i*16)
                    if entity:
                        pm.write_uchar(entity+m_bSpotted,1)
            else:
                pass
                
            #bunnyhop
            if bunnyhop_on_off == "ON":
                if pm.read_int(client+dwLocalPlayer):
                    force_jump=client+dwForceJump
                    on_ground=pm.read_int(player+m_fFlags)
                    velocity=pm.read_float(player+m_vecVelocity)
                    if keyboard.is_pressed('space')and on_ground==257:
                        if velocity<1 and velocity>-1:
                            pass
                        else:
                            pm.write_int(force_jump,5)
                            time.sleep(0.17)
                            pm.write_int(force_jump,4)
            else:
                pass

            #esp
            if esp_on_off == "ON":
                glow_manager = pm.read_int(client + dwGlowObjectManager)

                for i in range(1, 32):  # Entities 1-32 are reserved for players.
                        entity = pm.read_int(client + dwEntityList + i * 0x10)

                        if entity:
                                entity_team_id = pm.read_int(entity + m_iTeamNum)
                                entity_glow = pm.read_int(entity + m_iGlowIndex)

                                if entity_team_id == 2:  # Terrorist
                                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(T_R))   # R
                                        pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(T_G))   # G
                                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(T_B))  # B
                                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))    # Alpha
                                        pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)       # Enable glow

                                elif entity_team_id == 3:  # Counter-terrorist
                                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(CT_R))   # R
                                        pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(CT_G))   # G
                                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(CT_B))  # B
                                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))     # Alpha
                                        pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)         # Enable glow
            else:
                pass

        #if csgo was closed or cheat crashedprint error in cmd and log
        except:
            #print error in cmd
            print (f"{light_RED}-[ERROR] Cheat crashed and will now restart in 5 seconds.")
            #log error
            log_file.write(f"[error- {datetime.now()}] cheat crashed restarting in 5sec.\n")
            time.sleep(5)
            #restart
            main()
            
        

#start main function
if __name__ == "__main__":
    time.sleep(0.5)
    print (f"{light_GREEN}-[INFO] Hack started...")
    main()

