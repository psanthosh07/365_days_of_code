#!/bin/bash
# Incase you have to take input, please take it from file named 'input' (without quotes) [E.g. grep input OR cat input]
# Print you final output to console, do not redirect to another file
# E.g. Suppose the question is to print the content of a file.
#      Your solution should be 'cat input'(without quotes) instead of 'cat input > output'. That's it!
# Your code starts from here...
cat input | tr -d '[:punct:]'
