# this is python program for computing longest sequenece of pattern that is palindrome

def expansion(left,right,sequence):

    length=len(sequence)

    while left>=0 and right<length and sequence[left]==sequence[right]:

        left=left-1

        right=right+1

    return sequence[left+1:right]


def longest_pattern(sequence):

    length=len(sequence)

    longest=""

    for index in range(length):

        current=expansion(index,index)

        if len(longest)<len(current):

            longest=current

        current=expansion(index,index+1)

        if len(longest)<len(current):

            longest=current

    return longest

# test code

sequence=input("Enter DNA sequence: ")

longest=longest_pattern(sequence=sequence)

print("The longest pattern is: ",longest)

