// DO NOT USE ARGUMENTS FOR INPUTS
// Input num valus is in variable *num*
var num = parseInt(readLine().trim());
// YOUR CODE GOES HERE
for (var i = 0; i < num; i++) {
    if (i % 2 !== 0) {
        console.log(i);
    }
}
