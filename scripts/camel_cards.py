#/1usr/bin/env python

def parse_input(path:str="input/camel_cards.txt") -> list:
    data = open(path).read().splitlines()
    
    hands=[]
    bids={}
    for line in data:
        hand, bid = line.split(" ")
        #hand = tuple("23456789TJQKA".index(card) for card in hand) # Part 1
        hand = tuple("J23456789TQKA".index(card) for card in hand) # Part 2
        bids[hand] = int(bid.strip())
        hands.append(hand)
    return hands, bids
        
hands, bid = parse_input()

hand_type={i:[] for i in range(0,7)}

def get_type(card) -> int:
    if len(set(card)) == 5: # high card
        return 0
    elif len(set(card)) == 4: # one pair
        return 1
    elif len(set(card)) == 3:
        if sorted([card.count(x) for x in set(card)]) == [1,2,2]: #two pair
            return 2
        else:
            return 3 #three of a kind
    elif len(set(card)) == 2:
        if sorted([card.count(x) for x in set(card)]) == [2, 3]: #full house
            return 4
        else:
           return 5 # four of a kind
    else:
        return 6 # five of a kind

for hand in hands:
    types=[]
    for replacement in [1,2,3,4,5,6,7,8,9,10,11,12]: #Part2
        new_hand=[]
        for i in hand:
            if i == 0:
                new_hand.append(replacement)
            else:
                new_hand.append(i)
        types.append(get_type(new_hand))
    hand_type[max(types)].append(hand)

        
ranks = {i:None for i in range(len(hands))}

counter=0
for typ, hands in hand_type.items():
    if len(hands) == 1:
        ranks[counter]=hands[0]
        counter+=1
    elif len(hands) > 1:
        hands = sorted(hands)
        for hand in hands:
            ranks[counter]=hand
            counter+=1 
    else:
        pass 

result=0
for rank, hand in ranks.items():
    result = result + (1+rank)*bid[hand]
    
print(result)