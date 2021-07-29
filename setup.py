import game
import simulator

while True:
    decks = input("Enter number of decks: ")
    try:
        int(decks)
    except ValueError:
        print("Not an integer!")
    else:
        decks = int(decks)
        if decks < 1:
            print("Deck number too small!")
        else:
            break

while True:
    pene = input("Enter percentage deck penetration: ")
    pene = pene.strip("%")
    try:
        int(pene)
    except ValueError:
        print("Not an integer!")
    else:
        pene = int(pene)
        if 1 < pene < 100:
            pene = pene / 100
            break
        else:
            print("Outside percentage range!")

while True:
    s17 = input("Dealer stands on soft 17? (Y/N): ")[0].upper()
    if s17 == "Y":
        s17 = True
        break
    elif s17 == "N":
        s17 = False
        break
    else:
        print("Not yes or no!")

while True:
    bjpayout = input("Enter multiplier for natural blackjack (1.5 for 3 to 2, 1.2 for 6 to 5): ")
    try:
        bjpayout = float(bjpayout)
    except ValueError:
        print("Not a number!")
    else:
        break

while True:
    totcandouble = input("Enter all totals player can double on, seperated by spaces (Enter 'All' for all totals): ")
    if totcandouble == "All":
        totcandouble = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        break
    values_str = totcandouble.split(" ")
    totcandouble = []
    for value in values_str:
        try:
            totcandouble.append(int(value))
        except ValueError:
            print("Not an integer!")


while True:
    das = input("Double after split? (Y/N): ")[0].upper()
    if das == "Y":
        das = True
        break
    elif das == "N":
        das = False
        break
    else:
        print("Not yes or no!")

while True:
    resplit = input("Enter number of hands player can split to (Enter 0 for no limit): ")
    try:
        resplit = int(resplit)
    except ValueError:
        print("Not an integer!")
    else:
        if resplit == 0:
            resplit = 100
        break

while True:
    resplitaces = input("Can the player resplit aces? (Y/N): ")[0].upper()
    if resplitaces == "Y":
        resplitaces = True
        break
    elif resplitaces == "N":
        resplitaces = False
        break
    else:
        print("Not yes or no!")

while True:
    hitaces = input("Can the player hit split aces? (Y/N): ")[0].upper()
    if hitaces == "Y":
        hitaces = True
        break
    elif hitaces == "N":
        hitaces = False
        break
    else:
        print("Not yes or no!")

# losebj = input("Does the player lose original or all bets against dealer blackjack (All/Original)")

while True:
    peeks = input("Dealer peeks for blackjack? (Y/N): ")[0].upper()
    if peeks == "Y":
        peeks = True
        break
    elif peeks == "N":
        peeks = False
        break
    else:
        print("Not yes or no!")

while True:
    latesurr = input("Can the player late surrender? (Y/N): ")[0].upper()
    if latesurr == "Y":
        latesurr = True
        break
    elif latesurr == "N":
        latesurr = False
        break
    else:
        print("Not yes or no!")

while True:
    sim = input("Simulator Mode? (Y/N): ")[0].upper()
    if sim == "Y":
        sim = True
        break
    elif sim == "N":
        sim = False
        break
    else:
        print("Not yes or no!")

rules = {
    "decks": decks,
    "pene": pene,
    "s17": s17,
    "bj_payout": bjpayout,
    "can_double": totcandouble,
    "das": das,
    "resplit": resplit,
    "resplit_aces": resplitaces,
    "hit_aces": hitaces,
    "peeks": peeks,
    "late_surr": latesurr,
}

if sim:
    basic_strategy = simulator.StrategyTable()
    while True:
        strat_name = input("Enter strategy name, 'Rookie' for KO Rookie, 'Rad' for KO Rad, and 'Pref' for KO Preferred: ")
        if strat_name == "Rookie":
            bet_spread = int(input("Enter high value of bet spread: "))
            strategy = simulator.Strategy(basic_strategy, rules, bet_spread, False)
            break
else:
    strategy = None


print("")
game.run(rules, strategy)
