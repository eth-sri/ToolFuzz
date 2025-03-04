#! /bin/bash

bash run_envs.sh sub_test_1.txt gpt_4o_mini_5_def def
bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_0 0
bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_1 1
bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_2 2
bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_3 3
bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_4 4

docker system prune -f

bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_5 5
bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_6 6
bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_7 7
bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_8 8
bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_9 9
bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_10 10

docker system prune -f

bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_11 11
bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_12 12
bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_13 13
bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_14 14
bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_15 15

docker system prune -f

bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_16 16
bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_17 17
bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_18 18
bash run_envs.sh sub_test_5.txt gpt_4o_mini_5_19 19
