# seed the pseudorandom number generator
from random import seed
from random import randint
import time
from os import system

seed(1)
base_call = "http://0.0.0.0:5000"

try:
    while True:
        host_int = randint(0,8)
        call_int = randint(0,4)
        
        if(host_int == 0):
            host = "Nils_Styger"
        elif(host_int == 1):
            host = "Lady_of_All_Sorrows"
        elif (host_int == 2):
            host = "Dr._Rory_Campbell"
        elif (host_int == 3):
            host = "Liz_Allan"
        elif (host_int == 4):
            host = "Bart_Gallows"
        elif (host_int == 5):
            host = "Thomas_Halloway"
        elif (host_int == 6):
            host = "Aaron_Nicholson"
        elif (host_int == 7):
            host = "Peter_Parker"
        elif (host_int == 8):
            host = "Ant-Man"
        else:
            host ="Squadron_Supreme"
            
        
        if(call_int == 0):
            call = base_call + "/join_a_guild/" + str(randint(0,39))
        elif(call_int == 1):
            call = base_call + "/kill_enemy/" + str(randint(0,49))
        elif(call_int == 2):
            call = base_call + "/take_damage/" + str(randint(0,8))
        elif(call_int == 3):
            call = base_call + "/accepted_a_quest/"+ str(randint(0,14))
        else:
            call = base_call + "/transaction/" + str(randint(0,14))
            
            
            
        system("docker-compose exec mids ab -n 1 -H " +
               "\"" +host +  "\" " +
               call)
        
        time.sleep(0.5)
        
except KeyboardInterrupt:
    print('interrupted!')