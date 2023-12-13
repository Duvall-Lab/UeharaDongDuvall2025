#!/bin/sh
for i in `cat id.txt`
do 
mafft --auto ${i}.fa > aligned/${i}.aligned.fa
trimal -in aligned/${i}.aligned.fa -out aligned/${i}.aligned.trimed.fa -htmlout aligned/${i}.aligned.trimed.fa.html -automated1
done
