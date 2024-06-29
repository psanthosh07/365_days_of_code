// DO NOT USE ARGUMENTS FOR INPUTS
// Input num valus is in variable *num*
var N = parseInt(readLine().trim());
// YOUR CODE GOES HERE
for (var i = 0; i < N; i++) {

    if (i % 2 === 0) {
        continue;
    }

    console.log(i);

    if (i >= N) {
        break;
    }
}
