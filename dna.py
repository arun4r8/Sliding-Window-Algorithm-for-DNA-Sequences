# File: dna.py

# Description: This program finds the longest common subsequence(s)
#              between two strands of DNA.

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrigns that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.

"""
DNA
"""

def longest_subsequence(s1, s2):
    """
    This longest subsequence reads a pair of sequences
    and returns the longest one.
    """
    if len(s1) < len(s2):
        short, long = s1.upper(), s2.upper()
    else:
        short, long = s2.upper(), s1.upper()
    l = []
    for i in range(len(short), 0, -1): #window size
        for x in range(len(short)-i+1):
            if short[x:x+i] in long and short[x:x+i] not in l:
                l.append(short[x:x+i])
        if l:
            return sorted(l)
    return []

def main():
    """
    This main function reads the data input files and
    prints to the standard output. 
    NO NEED TO CHANGE THE MAIN FUNCTION.
    """

    # read the data
    # number of lines
    n_lines = int(input())

    # for each pair
    for _ in range(0, n_lines):
        str_1 = input()
        str_2 = input()

        # call longest_subsequence
        subsequences = longest_subsequence(str_1, str_2)

        # write out result(s)
        if not subsequences:
            print("No Common Sequence Found")

        for subsequence in subsequences:
            print(f"{subsequence}")

        # insert blank line
        print()


if __name__ == "__main__":
    main()
