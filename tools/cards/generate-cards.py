#!/usr/bin/python3

#debug = True
debug = False
cards = {}

order = 7
cards_n = (order + 1)*order + 1

cardsep = {}
cardsep[7] = [0,1,3,13,32,36,43,52]

if debug:
    print("Order:             %d" % order)
    print("Cards:             %d" % cards_n)
    print("Symbols:           %d" % cards_n)
    print("Card Symbols:      %d" % len(cardsep[order]))
    print("Symbol Separation: %s" % cardsep[order])

for x in range(0, cards_n):
    cards[x] = []
    for c in range(0, len(cardsep[order])):
        cards[x].append("")
    if debug: print("Create card: %d %s" % (x, cards[x]))

for x in range(0, cards_n):
    if debug:
        print("Allocate symbol: %d" % (x))

    for c in range(0, len(cardsep[order])):
        separation = cardsep[order][c]
        if debug: print("  separation: %d" % separation)
        card = ( x + separation ) % cards_n

        if debug: print("  x:%d -> card:%d pos:%d" % (x, card, c))

        cards[card][c] = x

# Output
print("card, icon1, icon2, icon3, icon4, icon5, icon6, icon7, icon8")
for x in range(0, cards_n):
    cards_string = ["icon-"+str(y)+".svg" for y in cards[x]]
    separator = ", "
    string = separator.join(cards_string)
    print("%d, %s" % (x+1, string))
