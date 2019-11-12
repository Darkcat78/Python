
Personnages={
"Moutarde":"CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAA",
"Rose":"CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGA",
"Pervenche":"AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGA",
"Leblanc":"CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"
}

ADNk=["CATA","ATGC"]

for suspect, ADN in Personnages.items():
    for i in ADNk:
        if i in ADN:
           ADN = ADN.replace(i,'1111')
        if ADN.count('1111') == len(ADNk):
            print(suspect + " est le/la coupable")