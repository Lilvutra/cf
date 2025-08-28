# t - number of test cases (input)
# n,k - number of people and the threshold at which Robin Hood takes the gold
# n - the gold of each person

num_cases = int(input())


for i in range(num_cases):
    input0 = list(map(int, input().split())) # number of people and threshold
    input1 = list(map(int, input().split()))
    print(f"num_people: {input0[0]}")
    print(f"threshold {input0[1]}")
    print(f"gold of each person: {input1}")

    for i in range(input0[0]):
        num_get_gold = 0
        robin_start_gold = 0
        if input1[i] >= input0[1]:
            robin_start_gold += input1[i]
        if input1[i] == 0 and robin_start_gold >= 0:
            num_get_gold += 1
    print(num_get_gold)

































