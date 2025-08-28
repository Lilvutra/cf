# String 

lex_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


num_cases = int(input())

for _ in range(num_cases):
    n, k = map(int, input().split())
        
    r = input()
    
        
def is_universal(r):

        # Reverse the string r 
        r_r = reverse(r)
        
        swap_operation = 0 
        
        for i in range(len(r)):
            # Case 1: check if the first different position,  the string 𝑎
            # already has a letter that appears earlier in the alphabet than the corresponding letter in 𝑏

            if r[i] != r_r[i]:
                if lex_alphabet.index(r[i]) < lex_alphabet.index[r_r[i]]:
                    print("YES")
                    
                # If a and b differ, alphabet order of that letter in a is > than that of the letter in b 
                else: 
                    # Find the < letter in remaining letters
                    for j in range(i, len(r)):
                        if lex_alphabet.index(r[j]) < lex_alphabet.index(r[j+1]):
                            r[j] = r[j+1]
                            r[j+1] = r[j]
                            swap_operation += 1
                            is_universal(r)
        if swap_operation > k:
            print("NO")
                            
def reverse(r):
    return r[::-1]


print(is_universal('rev'))