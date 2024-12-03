DIGITS = [str(x) for x in range(10)]

def get_muls(s):
    # modes: nuttin, start_mul, first_num, second_num
    total = 0
    mode = 'nuttin'
    n1 = ''
    n2 = ''
    for i in range(len(s)):
        if s[i] == '(' and i > 3 and s[i-3:i] == 'mul':
            mode = 'start_num'
        elif mode == 'start_num':
            if s[i] in DIGITS:
                n1 += s[i]
                if len(n1) > 3:
                    mode = 'nuttin'
                    n1 = ''
            elif s[i] == ',' and len(n1) > 0:
                mode = 'second_num'
            else:
                n1 = ''
                mode = 'nuttin'
        elif mode == 'second_num':
            if s[i] in DIGITS:
                n2 += s[i]
                if len(n2) > 3:
                    mode = 'nuttin'
                    n1 = ''
                    n2 = ''
            elif s[i] == ')' and len(n2) > 0:
                total += int(n1) * int(n2)
                mode = 'nuttin'
                n1 = ''
                n2 = ''
            else:
                mode = 'nuttin'
                n1 = ''
                n2 = ''
    return total

with open('input.txt', 'r') as f:
    mem = f.read()
    
print(get_muls(mem))
