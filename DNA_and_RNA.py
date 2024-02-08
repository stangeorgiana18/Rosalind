def count_nucl(file_name):
    with open(file_name, 'r') as f:
        dna = f.read().strip()
        
        return map(dna.count, "ACGT")

result = count_nucl('rosalind_dna.txt')
print(*result) # unpacking operator for the iterable elements

# equivalent to: print(result[0], result[1], result[2], result[3])


def transcription(file_name):
    with open(file_name, 'r') as f:
        dna = f.read().strip()

        rna = ''.join(['U' if base == 'T' else base for base in dna])

        # or with map and lambda
        # rna = ''.join(map(lambda base: 'U' if base == 'T' else base, dna))

        # or using replace
        #rna = dna.replace('T', 'U')

        # alternatively
        # rna = 'U'.join(dna.split('T'))

        return rna
    
result = transcription('rosalind_rna.txt')
print(result)


# in bash:
# cat rosalind_rna.txt | tr T U
# tr - translate/transliterate to replace characters 

print('\n')


def rev_compl(file_name):
    with open(file_name, 'r') as f:
        dna = f.read().strip()

        complement = ''.join(['A' if base == 'T' else 'T' if base == 'A' else 'C' if base == 'G' else 'G' if base == 'C' else base for base in dna])[::-1]
        #complement = complement[::-1]

        # or:
        # complement = dna.replace('A', 'T').replace('T', 'A').replace('C', 'G').replace('G', 'C')[::-1]
        return complement
    
result = rev_compl('rosalind_revc.txt')
print(result, '\n')


def hamming_distance(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
        sequence = content.split()

        count = 0
        for i in range(len(sequence[0])):
            if sequence[0][i] != sequence[1][i]:
                count += 1

        return count
    
print(hamming_distance('rosalind_hamm.txt'))