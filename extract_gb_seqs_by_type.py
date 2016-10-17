from Bio import SeqIO
from Bio import SeqFeature
from Bio.SeqRecord import SeqRecord

seqs_of_interest = []
for record in SeqIO.parse('IGR_genbank.gb', 'genbank'):
    for feature in record.features:
        if feature.type == 'rRNA':
            sequence_of_interest = feature.location.extract(record).seq
            seqs_of_interest.append(SeqRecord(sequence_of_interest,id=feature.qualifiers['locus_tag'][0]))



#with open("IGRs_from_genbank.fasta", "w") as igr_output:
    #SeqIO.write(seqs_of_interest, igr_output, "fasta")
