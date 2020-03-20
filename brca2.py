origin=""
exons=""
fptr1=open("origin_brca2.txt","r")
Str1=fptr1.read()

for i in Str1:
    if ord(i)>=65 and ord(i)<=90:
        origin+=i

cds=[]
temp=""
fptr2=open("cds_brca2.txt","r")
Str2=fptr2.read()
Str2=Str2.replace("..",",")

for i in Str2:
    if ord(i)!=44 and ord(i)!=32 and ord(i)!=10:
        temp+=i
    if ord(i)==44:
        cds.append(temp)
        temp=""
cds.append(temp)

for i in range(0,len(cds),2):
    for k in range(int(cds[i])-1,int(cds[i+1])):
        exons+=origin[k]

#print(len(exons))

f=open("exons.txt","w+")
for i in exons:
    f.write(i)

codon_table={ 
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
    }

sub_exon=""
protein_seq=""

for i in range(0,len(exons),3):
    for j in range(i,i+3):
        sub_exon+=exons[j]

    encoding=codon_table[sub_exon]
    protein_seq+=encoding
    sub_exon=""

print(len(protein_seq))










