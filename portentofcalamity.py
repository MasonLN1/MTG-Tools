import numpy as np
import random
import matplotlib.pyplot as plt

types = ["Land", "Instant", "Kindred Instant", "Kindred Sorcery", "Sorcery", "Artifact", "Creature", "Enchantment"] # Adjust if additional card types or mixed types are added
amount = [12, 15, 4, 2, 14, 5, 8, 0] # Adjust to however your deck is built, types may need to be adjusted if mixed types are included (artifact creature, etc).

deck = [np.repeat(n,t) for n,t in zip(types, amount)]
def flatten(seq):
    l = []
    for elt in seq:
        t = type(elt)
        if t is tuple or t is list:
            for elt2 in flatten(elt):
                l.append(elt2)
        else:
            l.append(elt)
    return l
deck = [l.tolist() for l in deck]
deck = flatten(deck)

def portent(seq):
    # Note: if additional mixed types are added to the list "types", then additional if statements will need to be added to the while loop to accomodate the new types (same fashion).
    l = []
    while len(set(l))<4:
        l.append(seq[random.randint(0,len(seq)-1)])
        if "Kindred Instant" in l and "Kindred" not in l:
            del l[-1]
            l.append("Kindred")
        if "Kindred Sorcery" in l and "Kindred" not in l:
            del l[-1]
            l.append("Kindred")
        if "Kindred Instant" in l and "Kindred" in l:
            del l[-1]
            l.append("Instant")
        if "Kindred Sorcery" in l and "Kindred" in l: 
            del l[-1]
            l.append("Sorcery")
    return len(l)

total=0
i=0
max=0
carlo=300000
while i < carlo:
    total=total+portent(deck)
    i=i+1
avg = total/carlo

i=0
test=0
count=[0]*13
placeholder=0
while i < carlo:
     placeholder=portent(deck)
     if placeholder > len(count)+3:
         placeholder = len(count)+3
     count[placeholder-4]=count[placeholder-4]+1
     i=i+1

AvgCount = []
for x in count:
    AvgCount.append(x/carlo)

i=0
TotalCount=[]
while i < len(AvgCount):
    TotalCount.append(round(sum(AvgCount[0:i+1]),5))
    i=i+1

plt.bar(["4","5","6","7","8","9","10","11","12","13","14","15","16+"] , TotalCount, width=0.90)
plt.xlabel("X mana paid")
plt.ylabel("Probability")
plt.title("Portent of Calamity Free Spell Odds")
plt.show()
print("-------------------------------------------------------------------------")
print("Average X value to meet Portent of Calamity condition (Modified Blue Portent List):", round(avg,5))
print("Odds of meeting Portent of Calamity condition within X=4:", round(TotalCount[0]*100,3), "%")
print("Odds of meeting Portent of Calamity condition within X=5:", round(TotalCount[1]*100,3), "%")
print("Odds of meeting Portent of Calamity condition within X=6:", round(TotalCount[2]*100,3), "%")
print("Odds of meeting Portent of Calamity condition within X=7:", round(TotalCount[3]*100,3), "%")
print("-------------------------------------------------------------------------")
plt.bar(["4","5","6","7","8","9","10","11","12","13","14","15","16+"] , AvgCount, width=0.90)
plt.xlabel("X mana paid")
plt.ylabel("Probability")
plt.title("Portent of Calamity Chance It Will Take X")
plt.show()
