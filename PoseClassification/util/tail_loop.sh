#!/bin/bash

mkdir csv_tmp
for i in $(cat id); do
  
  infile="${i}.csv"
  tail -n +4 "${infile}" > "csv_tmp/${i}_${j}t.csv"
  
done
