#!/bin/bash
if [ "$1" == "-h" ]; then
  echo "Usage: `basename $0` NOTEBOOK PAGE_ROOT
    where
    - NOTEBOOK is the path of the notebook
    - PAGE_ROOT is the root directory of the GitHub page"
  exit 0
fi

jupyter nbconvert --to markdown "$1"
python nb2page.py "$1" "$2"
