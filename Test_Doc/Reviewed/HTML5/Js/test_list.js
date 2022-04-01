// list allows elements of different types.
var strs=["a","b",'c'];
console.log(strs[0]);
console.log(strs);

strs.shift(); // left shift, and "a" is removed
strs.pop();   // remove the last element "c"
strs.push("100"); // add 100 to the end
var extended = strs.concat([200,300]); // expand strs and assign to extended, strs is not changed
strs.sort()



var mixed_list=["a",100];
console.log(mixed_list[1]);

var matrix=[ [1,2,3],[4,5,600]];
console.log(matrix[1][2]);