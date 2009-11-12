#!/bin/sh
# source all completions found in the bash or zsh directory

if [ -n "$BASH" ] ; then
    src_dir="`dirname ${BASH_SOURCE:-$0}`/bash"
elif [ -n "$ZSH_VERSION" ] ; then
    src_dir="`dirname ${BASH_SOURCE:-$0}`/zsh"
else
    exit
fi

for script in $src_dir/*; do
    source $script 2>/dev/null
done
