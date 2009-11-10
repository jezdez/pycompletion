#!/bin/sh
# source all completions found in the "complete" directory

src_dir="`dirname ${BASH_SOURCE:-$0}`/complete"
for script in $src_dir/*; do
    source $script 2>/dev/null
done
