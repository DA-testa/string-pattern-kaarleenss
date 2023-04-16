# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    inp = input()
    pattern = ""
    line = ""
    
    if inp[0] == "I":
        # first two tests are from keyboard, third test is from a file

        # input from keyboard
        pattern = input()
        text = input()
        

    elif inp[0] == "F":
        #Fname = input()
        path = "./tests/" + "06"
        with open(path, "r") as file:
            content = file.readlines()
        pattern = content[0].replace('\n', '')
        text = content[1].replace('\n', '')
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    lenPat = len(pattern)
    lenText = len(text)
    pos = []
    sp = ""
    for i in range(0, lenText - lenPat + 1):
        a = 0
        sp = text[i : i + lenPat]
        for j in range(lenPat):
            if pattern[j] == sp[j]:
                a = a + 1
            else:
                break
        if a == lenPat:
            pos.append(i)
    #print(pos)
    # and return an iterable variable
    return pos


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

