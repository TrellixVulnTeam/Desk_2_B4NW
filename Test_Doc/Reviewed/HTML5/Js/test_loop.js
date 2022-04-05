//loop

var todos=[
    "clean room",
    "brush teeth",
    "exercise",
    "study Javascript",
    'eat healthy'
];

for (var i=0; i<todos.length; i++){
    console.log(todos[i]);
}

var j = 0
while (j<todos.length){
    console.log(todos[j]);
    j++;
}

todos.forEach(function(todo,k){
    console.log(todo,k);
})

todos.forEach(function (todo, m) {
    console.log(m,todo);
})

function write_test(){
    console.log("I am writing a test !");
}
write_test()