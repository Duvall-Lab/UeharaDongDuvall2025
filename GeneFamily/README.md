# Protocol for CAFE and downstream analysis.
## Environment
- OrthoFinder v 2.5.5
- mafft v7.520
- trimal v1.4.rev15
- iqtree v2.2.6
- r8s v1.81

All software can be installed by `conta install`. Building virtual environment like `conda create -n cafe` is recommended.

## Construnting ML-phylogenetic tree
1. Collect protein sequences of species you are interested in.
2. Run orthofinder (version 2.5.5) `orthofinder -I 0.8 -f /path/to/protein_directory/`
3. `mv` ~/OrthoFinder/Results_Date/Single_Copy_Orthologue_Sequences/
4. run `sh ./util/align_trim.sh`
5. `cd` ~/OrthoFinder/Results_Date/OrthoGroups/
6. `cat` Orthogroups.tsv | `grep -f` Orthogroups_SingleCopyOrthologues.txt > OG_SingleCopy.tsv
7. add species names to the first row of OG_SingleCopy.tsv
8. `cd` ~/OrthoFinder/Results_Date/Single_Copy_Orthologue_Sequences/
9. run `python ./util/change_OTU.py OG_SingleCopy.tsv OG000XXXX.alined.trimmed.fa` -- you can use for loop
10. To run iqtree for constructing phylogenetic tree, make nexus file first. If you have OG list, you can use ./util/generate_nexus.py id.txt
11. `iqtree -sp id.nex -nt AUTO -bb 1000`
12. Then you can get newwick format ML-phylogenetic tree

## Convert ML-phylogeny to divergence time considered phylogeny
1. Get python scripts here for preparing r8s: https://github.com/hahnlab/cafe_tutorial/tree/6b407cabda460224e70e12e66f7144cef0f4d97c/python_scripts/cafetutorial_prep_r8s.py
2. run as follows:
```
r8s -b -f r8s_ctl_file.txt > r8s.tmp
tail -n 1 r8s.tmp | cut -c 16- > aedes_spp_r8s_ultrametric.txt
```

## Run CAFE5
1. `/CAFE5/bin/cafe5 -i Orthogroups.GeneCount2.1.tsv -t aedes_spp_r8s_ultrametric2.txt -p -o ./results2`

### Processing for large fulctuation gene family
`python cafetutorial_clade_and_size_filter.py -i Orthogroups.GeneCount2.tsv -o filtered_cafe_input.txt -s`
