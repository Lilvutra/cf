num_cases = int(input())
results = []

for _ in range(num_cases):
    card_list = list(map(int, input().split))
    Suneet_cards = [card_list[0], card_list[1]]
    Slavic_cards = [card_list[2], card_list[3]]
    
    Suneet_wins = 0
    Slavic_wins = 0
    
    # first turn: Suneet(a1) vs Slavic(b1, b2)
    if Suneet_cards[0] > Slavic_cards[0]:
        Suneet_wins += 1
    elif Suneet_cards[1] > Slavic_cards[1]:
        Suneet_wins += 1
    
    