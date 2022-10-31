#automate the boring stuff chapter 2 - guess the number
import random
import sys


zahl = random.randint(0,20) #Random Integer generieren


print("Errate die Zahl, an die ich gerade denke..\n")
print("Tipp, die Zahl liegt zwischen 0 und 20. ")
print("Du hast nur 6 Versuche!\n")


for a in range(1,7):

    x  = int(input()) #Zahl eingeben

    #If else Struktur, um zu schauen, ob die Zahl richtig ist

    if x == zahl:
        print("Wow. Du hast es richtig erraten! Die gesuchte Zahl war " + str(zahl) + ".\n")
        print("Du hast es in " + str(a) + " Versuchen geschafft.")
        sys.exit()
    elif x > zahl: 
        print("Leider ist die Zahl zu groß.")
        
    else:
        print("Leider ist die Zahl zu klein.")
    

 #Am Ende ein Satz, damit der Spieler, wenn er verloren hat und nicht die Zahl erraten hat, die Lösung erfährt.   
if a == 6:
    print("Schade, du hast es nicht geschafft. Die gesuchte Zahl war " + str(zahl) + " ...")
    
else:
    sys.exit()
        








