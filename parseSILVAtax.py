acclines = []

with open('test_taxprocedure/phase3/arb-silva.de_2020-05-12_id821915_allVibrio.fasta','r') as f:
    for line in f:
        if(line[0] == '>'):
            acclines.append(line)

f.close()


with open('test_taxprocedure/phase3/allSILVAaccessionsVibrio.csv','w') as of:
    #HEADER
    of.write('Accession Numbers')
    of.write(',')
    of.write('Start Position')
    of.write(',')
    of.write('Stop Position')
    of.write(',')
    of.write('Taxonomy\n')

    #DATA
    for line in acclines:
        index_per1 = line.find('.')
        seg1 = line[1:index_per1]
        line = line[index_per1+1:]
        
        index_per2 = line.find('.')
        seg2 = line[:index_per2]
        line = line[index_per2+1:]
        
        index_space = line.find(' ')
        seg3 = line[:index_space]
        
        of.write(seg1)
        of.write(',')
        of.write(seg2)
        of.write(',')
        of.write(seg3)
        of.write(',')
        of.write(line[index_space+1:])

of.close()
