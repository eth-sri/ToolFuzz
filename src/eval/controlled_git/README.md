## Running the git evaluation

The main script of this package is `agent.py`. It is run as follows:
```bash
python agent.py -p PATH_TO_TOOL_DESCRIPTIONS -o OUTPUT_JSON_POSTFIX -m MODE
```

The tool descriptions have to be in a specific format, there are examples in the `./tool_desc`, the modes are `train` and `test`.

The eval.sh script runs sequentially agent.py for many tool descriptions.