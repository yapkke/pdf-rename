#!/usr/bin/env bash
for f in *.pdf
do
    pdf-rename.py $@ "$f" 
done