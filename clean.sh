#!/bin/bash

target="__pycache__"

if [ $(find . -name $target -type d | wc -l) -ne 0 ]
then
    find . -name $target -type d -delete
fi
