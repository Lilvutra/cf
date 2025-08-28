num_cases = int(input())
results = []

for _ in range(num_cases):
    card_list = list(map(int, input().split))
    Suneet_cards = [card_list[0], card_list[1]]
    Slavic_cards = [card_list[2], card_list[3]]
    
    #first turn
    if Suneet_cards[0] > Slavic_cards[0]:
        Suneet_wins += 1
    elif Suneet_cards[1] < Slavic_cards[1]:
        Slavic_wins += 1
    
    #
    if Suneet_cards[0] > Slavic_cards[1]:
        Suneet_wins += 1
    elif Suneet_cards[1] < Slavic_cards[0]:
        Suneet_wins += 1
    
    #
    if Suneet_cards[1] > Slavic_cards[0]:
        Suneet_wins += 1
    elif Suneet_cards[0] < Slavic_cards[1]:
        Slavic_wins += 1 
    # 
    if Suneet_cards[1] > Slavic_cards[1]:
        Suneet_wins += 1
    if Suneet_cards[0] < Slavic_cards[0]:
        Slavic_wins += 1 
    
    if Suneet_wins > Slavic_wins:
        results.append(Suneet_wins)
    if Suneet_wins == Slavic_wins or Suneet_wins > Slavic_wins:
        results.append(0)
   

for result in results:
    print(result)
