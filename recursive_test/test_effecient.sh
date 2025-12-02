#!/bin/bash

cd /Users/roger/Desktop/Program-workspace/python3_workspace/zeroJudge-practice-python

python -m timeit -s "from recursive_test.effecient_compare import factorial_loop" "factorial_loop(500)"
python -m timeit -s "from recursive_test.effecient_compare import factorial_recurive" "factorial_recurive(500)"