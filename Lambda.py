def read_file(file_name):
    f = open(file_name, 'rt') # open for reading text
    line = f.read() # read the entire content as a single string
    values = line.split()
    a = int(values[0])
    b = int(values[1])
    f.close()

    return a ** 2 + b ** 2

print(read_file('rosalind_ini2.txt'))

print('\n')


# ANOTHER WAY USING LAMBDA:
    
def read_file(file_name):
    return open(file_name, 'rt').read().split()


values = read_file('rosalind_ini2.txt')
result = sum(map(lambda a: int(a) ** 2, values))

print(result)