#!/bin/bash

filter=$(cat filters-2 | while read label val; do
    echo "| tee >(grep -v $label) >(grep -E '$label $val\b') >/dev/null \\"
done)
eval "cat input $filter" \
    | grep -vE "(cats: [0-7]|trees: [0-3])" \
    | grep -vE "goldfish: ([6-9]|\d{2,})" \
    | grep -vE "pomeranians: ([4-9]|\d{2,})"
