// DO NOT USE ARGUMENTS FOR INPUTS
// Input num valus is in variable *num*
var N = parseInt(readLine().trim());
// YOUR CODE GOES HERE
var square = N ** 2;

var cube = N ** 3;

var result = square + cube - N;

console.log(result);
