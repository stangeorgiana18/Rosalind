def count_nucl(file_name):
    with open(file_name, 'r') as f:
        dna = f.read().strip()
        for i in 'ACGT':
            print(dna.count(i), end = " ")

count_nucl('rosalind_dna.txt')
