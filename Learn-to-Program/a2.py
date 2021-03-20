__author__ = 'aliyyousuf@gmail.com'



def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if len(dna1) > len(dna2):
        return True
    else:
        return False

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for letter in dna:
        if letter == nucleotide:
            count += 1
    return count

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna2 in dna1:
        return True
    else:
        return False


def is_valid_sequence(dna):
    """

    :param dna: dna sequence
    :return: bool
    >>> is_valid_sequence('')
    False
    >>> is_valid_sequence('AGCTt')
    False
    >>> is_valid_sequence('AGCTTTAATTAAJ')
    False
    >>> is_valid_sequence('A')
    True
    >>> is_valid_sequence('AAAAATTTTT')
    True
    """

    neucleotides = 'AGCT'

    if any(c.islower() for c in dna):
        return_val = False
    # elif not bool(dna.strip()):
    elif len(dna) == 0 or len(dna.strip()) == 0:
        return_val = False
    else:
        for n in dna:
            if n in neucleotides:
                return_val = True
            else:
                return_val = False
                break
    return return_val

def insert_sequence(str1,str2,index):

    if index == len(str1):
        return str1 + str2
    elif index == 0:
        return str2+str1
    else:
        return str1[:index] + str2 + str1[index:]




def get_complement(string):

    complementary_dit = {'A':'T','T':'A','G':'C','C':'G'}

    return complementary_dit[string]

def get_complementary_sequence(dna):

    complementary_dit = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    comp_seq = ''

    for n in dna:
        comp_seq = comp_seq + complementary_dit[n]

    return comp_seq