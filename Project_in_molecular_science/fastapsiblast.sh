#cd ../fasta_data/
for i in fasta_data/*.fasta
do
psiblast -query $i -db /home/u2343/Desktop/uniprot_sprot.fasta -num_iterations 3 -evalue 0.01 -out_ascii_pssm PSSM/$i.pssm -num_threads 8
done
