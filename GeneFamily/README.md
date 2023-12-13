# Add protocol for CAFE and folloing analysis here.
1. Collect protein sequences of species you are interested in.
2. Run orthofinder (version 2.5.5)
3. `mv` ~/OrthoFinder/Results_Date/Single_Copy_Orthologue_Sequences/
4. run `sh align_trim.sh`
5. `cd` ~/OrthoFinder/Results_Date/OrthoGroups/
6. `cat` Orthogroups.tsv | `grep -f` Orthogroups_SingleCopyOrthologues.txt > OG_SingleCopy.tsv
7. `cd` ~/OrthoFinder/Results_Date/Single_Copy_Orthologue_Sequences/
