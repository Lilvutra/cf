num_cases = int(input())
results = []


for _ in range(num_cases):
    card_list = list(map(int, input().split()))
    Suneet_cards = [card_list[0], card_list[1]]
    Slavic_cards = [card_list[2], card_list[3]]
    
    Suneet_wins = 0
    Slavic_wins = 0
    
    for i in range(2):
        for j in range(2):
            Suneet_remains = Suneet_cards[1 - i]
            Slavic_remains = Slavic_cards[1 - j]
            
            if Suneet_cards[i] > Slavic_cards[j]:
                
                print("Suneet card: " + str(Suneet_cards[i])) 
                print("Slavic card: " + str(Slavic_cards[j])) 

                Suneet_wins_rounds = 1
                Slavic_wins_rounds = 0
                
                print("Suneet wins")
                print("Suneet wins rounds: " + str(Suneet_wins_rounds))

            else:
                print("Suneet card: " + str(Suneet_cards[i]))
                print("Slavic card: " + str(Slavic_cards[j])) 
    

                print("Slavic wins")
                Suneet_wins_rounds = 0
                Slavic_wins_rounds = 1
                
                print("Slavic wins rounds: " + str(Slavic_wins_rounds))
        
            if Suneet_remains > Slavic_remains:
                print("Suneet remains: " + str(Suneet_remains))
                print("Slavic remains: " + str(Slavic_remains))

                Suneet_wins_rounds += 1
                print("Suneet wins rounds: " + str(Suneet_wins_rounds))
            else:
                print("Suneet remains: " + str(Suneet_remains))
                print("Slavic remains: " + str(Slavic_remains))
                Slavic_wins_rounds += 1 
                print(Slavic_wins_rounds)
    
            if Suneet_wins_rounds > Slavic_wins_rounds:
                Suneet_wins += 1
                print("Suneet wins: " + str(Suneet_wins))
            else:
                Slavic_wins += 1 
                print("Slavic wins: " + str(Slavic_wins))
            
    results.append(Suneet_wins) 
                
for result in results:
    print(result)