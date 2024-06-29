// DO NOT USE ARGUMENTS FOR INPUTS
// Input num valus is in variable *num*
var N = parseInt(readLine().trim());
// YOUR CODE GOES HERE
var negationN = ~N;

var orResult = N | negationN;

var xorResult = N ^ orResult;

console.log(xorResult);
