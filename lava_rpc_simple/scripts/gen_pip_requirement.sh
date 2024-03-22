#!/bin/bash

script_dir=$(cd $(dirname $0);pwd)
echo "script_dir is ${script_dir}"
pip freeze > ${script_dir}/../requirement.txt