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