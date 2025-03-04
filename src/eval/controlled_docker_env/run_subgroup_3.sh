#! /bin/bash

bash run_envs.sh sub_test_1.txt gpt_4o_mini_3_def def
bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_0 0
bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_1 1
bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_2 2
bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_3 3
bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_4 4

docker system prune -f

bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_5 5
bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_6 6
bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_7 7
bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_8 8
bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_9 9
bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_10 10

docker system prune -f

bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_11 11
bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_12 12
bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_13 13
bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_14 14
bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_15 15

docker system prune -f

bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_16 16
#bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_17 17
bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_18 18
bash run_envs.sh sub_test_3.txt gpt_4o_mini_3_19 19
