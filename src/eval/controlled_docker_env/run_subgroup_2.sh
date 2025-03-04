#! /bin/bash

bash run_envs.sh sub_test_1.txt gpt_4o_mini_2_def def
bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_0 0
bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_1 1
bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_2 2
bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_3 3
bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_4 4

docker system prune -f

bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_5 5
bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_6 6
bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_7 7
bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_8 8
bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_9 9
bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_10 10

docker system prune -f

bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_11 11
bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_12 12
bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_13 13
bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_14 14
bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_15 15

docker system prune -f

bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_16 16
bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_17 17
bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_18 18
bash run_envs.sh sub_test_2.txt gpt_4o_mini_2_19 19
