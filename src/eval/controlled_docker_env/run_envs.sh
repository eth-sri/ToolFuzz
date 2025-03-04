#!/bin/bash

envs=${1}
prefix=${2}
prompt_desc=${3}

parallel -a $envs --jobs 10 --result ./logs --joblog ./logs/joblog.txt \
"python evaluate.py -p ${prefix} -i ${prompt_desc} -c {}"
