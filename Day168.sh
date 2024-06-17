#!/bin/bash
# Incase you have to take input, please take it from file named 'input' (without quotes) [e.g. cat input]
# Print your final output to console. Do not redirect to another file.
# E.g. Suppose the question is to print the content of a file.
#      Your solution should be 'cat input'(without quotes) instead of 'cat input > output'. That's it!
# Your code starts from here...

# Read the input file line by line
while IFS=, read -r FirstName LastName Address City CountryCode Email PhoneNumber; do
  # Combine CountryCode and PhoneNumber
  CombinedPhoneNumber="+${CountryCode}-${PhoneNumber}"
  
  # Output the processed line
  echo "${FirstName},${LastName},${Address},${City},${Email},${CombinedPhoneNumber}"
done < input
