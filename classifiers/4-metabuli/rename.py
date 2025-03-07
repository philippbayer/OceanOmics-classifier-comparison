from Bio import SeqIO
import itertools
import string

names = itertools.product(string.ascii_lowercase, repeat=4)

with open('for_metabuli.fasta', 'w') as out1, \
        open('for_metabuli.taxa.txt', 'w') as out2:
    # accession       accession.version       taxid   gi
    #12S_NC_073553.1:71-1018 12S_NC_073553.1:71-1018.1       1003736 0
    out2.write('accession\taccession.version\ttaxid\tgi\n')

    for n, s in zip(names, SeqIO.parse('12s_v010_final.fasta', 'fasta')):
        full_name = s.description
        taxid = full_name.split(' ')[1]
        name = ''.join(n) + '.1'
        s.id = name
        s.name = name
        s.description = name
        out1.write(s.format('fasta'))
        out2.write(f'{"".join(n)}\t{name}\t{taxid}\t0\n')
