Add protocol and codes for DLC analysis here.

Downstream analysi of DLC

1. prepare filtered.csv file
2. ls | sed s/.csv//g > file_name
6. run `sh tail_loop.sh` new_version tail_loop.sh
7. `cd csv_tmp`
8. run `sh boxcar.sh`
9. run `python cal_velocity_multi2_js_npysave.py` to calculate velocity and save it as npy format.
<!--- 11. run `distance_multi.py’ to calculate the average distance per sec -->
12. `paste -d ',' *sum.csv > all_sum.csv`
13. open all_sum.csv with excel
14. visualize the data with `distance_cal.Rmd`
15. `mkdir vame_data`
16. run `sh tail2.sh` to proceed VAME analysis
