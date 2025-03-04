#! /bin/bash

docker system prune -f

bash run_envs.sh test_envs.txt test_baseline_td_src_10 10