import numpy as np

#File import

#open text file as read only
file1 = open('PF04264_full_length_sequences.fasta', 'r') #filepath if you're already in directory, otherwise need full filpath

allText = file1.read() #read in text

#open write-only output file
outFile = open('mod_PF04264_full_length_sequences.fasta','w') #filepath if you're already in directory, otherwise need full filpath

Entries=allText.split('>') #split text into discrete entries using > header char

IDs=[]

for entry in Entries: #for each fasta entry

    IDend=entry.find(')') #End of each fasta ID is ')'
    
    ID=entry[:IDend+1]
    
    IDs.append(ID) #collect IDs in to a list
    
for ID in np.unique(IDs):  #for each unique ID
    if IDs.count(ID)> 1:    #if it occurs more than once

        inds= [i for i, x in enumerate(IDs) if x == ID] #get indexes where they occur in IDs list (which should be same ordering as Entries list)
        
        del(Entries[inds[-1]]) #get the last index in the list of indexes, and delete the corresponding entry in Entries

outStr = "" #initialize an empty string

outStr=outStr.join(Entries) #join all entries from modified Entries list into on string of text

outFile.write(outStr) #file output

#close all files
file1.close()
outFile.close()
