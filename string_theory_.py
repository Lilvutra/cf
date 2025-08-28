lex_alphabet = list("abcdefghijklmnopqrstuvwxyz")
#print(lex_alphabet)

def is_universal(r, r_r, k):
    #r_r = r[::-1]  # Reverse the string
    print(r_r)
    swap_operation = 0
    
    r = list(r)  # Convert to list for mutability
    
    if len(r) == 1:
        return "NO"
   
    for i in range(len(r)):
        
        if r[i] != r_r[i]:  # Found the i index that letter in a and b differ
            if lex_alphabet.index(r[i]) < lex_alphabet.index(r_r[i]):
                return "YES"
            else:
                # 
                for j in range(i, len(r) - 1):
                    # Check if there exists a letter < letter in b in remaining letters of a
                    if lex_alphabet.index(r[j]) < lex_alphabet.index(r_r[i]):
                        # Swap with current r[i]
                        r[i], r[j] = r[j], r[i]
                        print(r)
                        swap_operation += 1
                        
                    
                        
                    
                    # if lex_alphabet.index(r[j]) > lex_alphabet.index(r[j + 1]):
                    #     r[j], r[j + 1] = r[j + 1], r[j]  # Swap letters
                    #     print(r)
                    #     swap_operation += 1
                        is_universal(r, r_r, k)
                        if swap_operation > k:
                            return "NO"
        return "NO"
   
    return "YES" if swap_operation <= k else "NO"


# Read input
num_cases = int(input())
for _ in range(num_cases):
    n, k = map(int, input().split())
    r = input()
    r_r = r[::-1]
    print(is_universal(r, r_r, k))
