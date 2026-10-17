import random 

print("vitamashot coinflip")
pasuxi = input("ki tu ara  ").strip()

if pasuxi not in ("ki","ara"):
   print("tu maimunoba ginda agar getamashebi ")
   exit()
elif  pasuxi == "ki" :
   print("kai gavargzelot")

elif pasuxi == "ara":
    print( "kai tuarginda iyavi ise")
    exit()

print("airchie heads an tails")
choose = input("heads tu tails : " )
if choose not in ( "heads","tails"):
    print ("nu maimunob")
#shansebi 

coin_1 = random.choice (['heads', 'tails'])

heads= "heads"
tails  = "tails"

print ("me avirchie " + coin_1)

if choose == heads and coin_1 == tails:
   print("shen wage 50/50 ian shanshi")


elif choose == tails and coin_1 == heads:
   print("shen wage 50/50 ian shanshi")


elif choose == tails and coin_1 == tails :
   print ("shen moigee" )


elif choose == heads and coin_1 == heads:
   print("shen moigeeeeeeeeeee")

else :
   print("ragacam gaweda")
 

