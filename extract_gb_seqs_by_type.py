from Bio import SeqIO
from Bio import SeqFeature
from Bio.SeqRecord import SeqRecord
import sys

def make_feature_fasta(genbank_path, outpath, feature_type):
    seqs_of_interest = []
    feature_count = 0
    genbank_in = SeqIO.parse(genbank_path, 'genbank')
    for record in genbank_in:
        for feature in record.features:
            if feature.type == feature_type:
                sequence_of_interest = feature.location.extract(record).seq
                if 'product' in feature.qualifiers:
                    product = feature.qualifiers['product'][0]
                else:
                    product = ''
                seqs_of_interest.append(SeqRecord(sequence_of_interest,id=feature.qualifiers['locus_tag'][0], description=product))
                feature_count += 1
    fasta_out = open(outpath, 'w')
    SeqIO.write(seqs_of_interest, fasta_out, "fasta")
    print(str(feature_count) + " sequences written to fasta.")

if __name__ == '__main__':
    if len(sys.argv) == 4:
         make_feature_fasta(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
         print("Usage: extract_gb_seqs_by_type.py gb_file_in fasta_file_out feature_type")
         sys.exit(0)
