def count_nucl(file_name):
    with open(file_name, 'r') as f:
        dna = f.read().strip()
        
        return map(dna.count, "ACGT")

result = count_nucl('rosalind_dna.txt')
print(*result) # unpacking operator for the iterable elements

# equivalent to: print(result[0], result[1], result[2], result[3])

