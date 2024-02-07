def slice_string(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        file_content = content.split('\n') # numbers and text are on diff lines
        text = file_content[0]
        index = list(map(lambda x: int(x), file_content[1].split())) # apply lambda to each el in the list from file_content..
        # map turned into a list to access the values by index 
        
    return text[index[0] : index[1] +1], text[index[2]: index[3] + 1]

print(slice_string('rosalind_ini3.txt')) # result as tuple


# ANOTHER WAY

with open('rosalind_ini3.txt') as f:
    line = f.readline() # read the first line of the file 
    a, b, c, d = [int(x) for x in f.readline().split()] # read the 2nd line of the file and split it into a list of strings

    print(line[a : b+1],line[c : d+1])

print('\n')

# conditions and loops 

with open('rosalind_ini4.txt', 'r') as f:
    a, b = [int(x) for x in f.readline().split()]
    if a % 2 == 0:
        a += 1

    print(sum(range(a, b+1, 2)))

print('\n')

# working with files

# Given: A file containing at most 1000 lines.

# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
    
with open('rosalind_ini5.txt', 'r') as f:
    content = f.read()

# open a new file for writing
with open('new_file.txt', 'w') as new_file:
    for i in range(1, len(content.splitlines()), 2):
        new_file.write(content.splitlines()[i] + '\n')


# another way
with open('rosalind_ini5.txt','r') as f:
    print(''.join(f.readlines()[1::2]))


# another way
f = open('rosalind_ini5.txt','r')
templines = f.readlines()[1::2] # read all lines from the file, selecting every second line
f.close()

f = open('output.txt','w')
f.writelines(templines) # write a seq of strings to the file
f.close()


# dictionaries
with open('rosalind_ini6.txt', 'r') as f:
    content = f.read()
    occurrence = {}
    for word in content.split():
        if word not in occurrence.keys():
            occurrence[word] = 1
        else:
            occurrence[word] += 1
        
    for key, value in occurrence.items():
        print (key, value)
