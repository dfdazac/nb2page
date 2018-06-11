#!/bin/bash
jupyter nbconvert --to markdown "$1"
python nb2page.py "$1" "$2"
