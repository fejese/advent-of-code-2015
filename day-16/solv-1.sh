#!/bin/bash

filter=$(cat filters | while read label val; do
    echo "| tee >(grep -v $label) >(grep -E '$label $val\b') >/dev/null \\"
done)
eval "cat input $filter"
