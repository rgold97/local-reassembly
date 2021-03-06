"""
Jack Petrillo and Rose Gold
Local Re-Assembly Final Project
CS 321
Generate Randomized Variant Reads from a Sequence
"""

from random import randint

def get_gene(filename):
    """
    Takes as an input a file name to read.
    Ignores the first line of the file (has identifying info in applicable genome files).
    Returns a string of gene devoid of new line chars.
    """
    with open(filename, 'r') as file_object:
        file_object.readline()
        input_str = file_object.read().strip()
        input_str = input_str.replace("\n", "")
    return input_str



def rand_variant(seq, prob):
    """
    Takes a sequence and a probability.
    Each character independently changes to a new character with proabibility prob.
    """
    nuc_bases = "ACGT"
    new_seq = ""
    for nuc in seq:
        cur_prob = randint(1, prob+1)
        if cur_prob == 1:
            temp_bases = nuc_bases.replace(nuc, '')
            new_nuc = temp_bases[randint(0,2)]
            new_seq += new_nuc
        else:
            new_seq += nuc
    return new_seq


def readList(read_len, seq):
    """
    Takes as inputs an integer read_len and a String seq.
    Returs a list of all the read_len-mers of seq.

    """

    read_list = []
    for index in range(len(seq) - read_len + 1):
        read_list.append(seq[index : index + read_len])

    return read_list



def main():
    """
    Main method for testing. Never called.
    """
    gene = get_gene("OPN1LW.txt")
    #gene = "ACTGCCCGGGTTT"
    #print(gene)
    prob = 10 #each nuc has a prob of 1/50 that it will become a variant
    read_len = 50 #temp
    rand_variant(gene, prob)
    var_seq = rand_variant(gene, prob)
    #print(var_seq)
    read_list = readList(read_len, var_seq)


if __name__ == '__main__':
    main()
