Add protocol and codes for VAME analysis here.

Downstream analysi of DLC
1. prepare filtered.csv file
5. `ls | sed s/.csv//g > file_name`
6. run `sh tail_loop.sh` new_version tail_loop.sh
7.  run `cal_velocity_multi.py` to calculate velocity
8. run `behavior_trajectory_loop.Rmd` to produce trajectory
9. run `distance_multi.py’ to calculate the distance per sec
10. `paste -d ',' *sum.csv > all_sum.csv`
11. open all_sum.csv with excel
12. visualize the data with `distance_cal.Rmd`
13. `mkdir vame_data`
14. run `sh tail2.sh` to proceed VAME analysis
