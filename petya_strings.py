str_1 = str(input())
str_2 = str(input())

alphabet_dict = {'A': 'a',
                 'B': 'b',
                 'C': 'c',
                 'D': 'd',
                 'F': 'f'}


for i in str_1:
    for j in str_2:
        str_1[i] == alphabet_dict[str_1[i]]
        str_2[j] == alphabet_dict[str_2[j]]


if str_1 < str_2:
    print("-1")
if str_1 > str_2:
    print("1")
if str_1 == str_2:
    print("0")
    
