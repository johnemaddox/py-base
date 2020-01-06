#!/bin/bash

# Remove __pycache__ directories
find . -name __pycache__ -type d -print0 | xargs -0 rm -r --
