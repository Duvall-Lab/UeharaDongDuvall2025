Add protocol and codes for DLC analysis here.

Downstream analysi of DLC

prepare filtered.csv file
ls | sed s/.csv//g > file_name
run sh tail_loop.sh new_version tail_loop.sh
run cal_velocity_multi.py to calculate velocity
run behavior_trajectory_loop.Rmd to produce trajectory
run `distance_multi.py’ to calculate the distance per sec
paste -d ',' *sum.csv > all_sum.csv
open all_sum.csv with excel
visualize the data with distance_cal.Rmd
mkdir vame_data
run sh tail2.sh to proceed VAME analysis
