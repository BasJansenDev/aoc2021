import math

def main(inp):
    outputs = [g[1].split(' ') for g in inp]
    summation = sum([sum([1 if len(value) == 2 or len(value) == 3 or len(value) == 4 or len(value) == 7 else 0 for value in output]) for output in outputs])
    return summation

def main2(inp):
    output_value = 0
    for entry in inp:
        patternslist, outputs = [g.split(' ') for g in entry]
        true_patterns = dict()
        last_len = 0
        while last_len != 10:
            for pattern in patternslist:
                if len(pattern) == 2:
                    true_patterns['1'] = pattern
                elif len(pattern) == 3:
                    true_patterns['7'] = pattern
                elif len(pattern) == 4:
                    true_patterns['4'] = pattern
                elif len(pattern) == 5:
                    if '7' in true_patterns and not '3' in true_patterns and set(true_patterns['7']).issubset(set(pattern)):
                        true_patterns['3'] = pattern
                    elif '3' in true_patterns and not '5' in true_patterns and '6' in true_patterns and len(set(true_patterns['6']).symmetric_difference(pattern)) == 1:
                        true_patterns['5'] = pattern
                    elif '5' in true_patterns and '3' in true_patterns and not '2' in true_patterns:
                        true_patterns['2'] = pattern
                elif len(pattern) == 6:
                    if '4' in true_patterns and not '9' in true_patterns and set(true_patterns['4']).issubset(set(pattern)):
                        true_patterns['9'] = pattern
                    elif '9' in true_patterns and '1' in true_patterns and not '0' in true_patterns and set(true_patterns['1']).issubset(set(pattern)):
                        true_patterns['0'] = pattern
                    elif '9' in true_patterns and '0' in true_patterns and not '6' in true_patterns:
                        true_patterns['6'] = pattern
                elif len(pattern) == 7:
                    true_patterns['8'] = pattern
                if(last_len != len(true_patterns)):
                    patternslist.remove(pattern)
                last_len = len(true_patterns)
        output_res = ""
        for output in outputs:
            for key in true_patterns:
                if set(true_patterns[key]) == set(output):
                    output_res += key
        output_value += (int(output_res))
    return output_value

def input_as_list(inp):
    f = open(inp)
    return [j.split(' | ') for j in [i for i in list(f.read().splitlines())]]

print('Part 1: ' + str(main(input_as_list('input'))))
print('Part 2: ' + str(main2(input_as_list('input'))))
