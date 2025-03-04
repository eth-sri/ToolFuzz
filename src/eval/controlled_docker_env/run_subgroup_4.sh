#! /bin/bash

bash run_envs.sh sub_test_1.txt gpt_4o_mini_4_def def
bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_0 0
bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_1 1
bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_2 2
bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_3 3
bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_4 4

docker system prune -f

bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_5 5
bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_6 6
bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_7 7
bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_8 8
bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_9 9
bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_10 10

docker system prune -f

bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_11 11
bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_12 12
bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_13 13
bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_14 14
bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_15 15

docker system prune -f

bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_16 16
bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_17 17
bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_18 18
bash run_envs.sh sub_test_4.txt gpt_4o_mini_4_19 19
