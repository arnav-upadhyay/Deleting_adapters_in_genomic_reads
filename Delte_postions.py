
import pandas as pd
import numpy as np

from Bio import SeqIO

# reading CSV file of postion
pos = pd.read_csv (r"D:\New_seq_deletr\Position.csv",header=None)

# replacing nan value with 0
pos = pos.fillna ( 0 )

# coverting col as int
pos[3] = pos[3].astype ( int )
pos[4] = pos[4].astype ( int )

# confimation
pos.info ()


# final dataframe
pos


my_dict = {}

# reading from seq file
with open ( r'D:\New_seq_deletr\Input_seq.fasta' ) as seq_file:
    seq = SeqIO.parse ( seq_file, "fasta" )

    for line in seq:  # loop on fasta file

        for ind in range ( len ( pos ) ):  # data from position file

            if (line.id == pos.iloc[ind][0]):

                # values of position
                pos_1 = pos.iloc[ind][1]
                pos_2 = pos.iloc[ind][2]
                pos_3 = pos.iloc[ind][3]
                pos_4 = pos.iloc[ind][4]

                len_seq = len ( line.seq )

                if (pos_3 == 0):
                    if (pos_1 ==1):
                        my_dict.update ( {line.id: (line.seq[(pos_2):len_seq])} )
                    else:
                        my_dict.update ( {line.id: (line.seq[0:(pos_1-1)])})

                else:
                    my_dict.update ( {line.id: line.seq[(pos_2):(pos_3-1)] } )


fo = open(r"D:\New_seq_deletr\Final_removed_391_sequences_lastttttttt","w")

for k, v in my_dict.items():
    fo.write('>'+str(k)+'\n'+ str(v) + '\n')

fo.close()



