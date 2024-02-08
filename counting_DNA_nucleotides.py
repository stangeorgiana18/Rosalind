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

