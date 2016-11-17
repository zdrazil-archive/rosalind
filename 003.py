input_string = input('Enter your DNA string: ')


def reverse_complement(dna_string):
    reversed_dna_string = dna_string[::-1]
    complemented_string = []
    for letter in reversed_dna_string:
        complemented_letter = None
        if letter == 'A':
            complemented_letter = 'T'
        elif letter == 'T':
            complemented_letter = 'A'
        elif letter == 'C':
            complemented_letter = 'G'
        elif letter == 'G':
            complemented_letter = 'C'
        complemented_string.append(complemented_letter)
    return ''.join(complemented_string)


print(reverse_complement(input_string))
