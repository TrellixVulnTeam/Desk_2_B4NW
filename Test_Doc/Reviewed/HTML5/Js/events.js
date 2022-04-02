//events
var button=document.getElementById("enter");
var input= document.getElementById("userinput");
var ul= document.querySelector("ul");

// button.addEventListener("click", function(){
//     // console.log("click is working");
//     var li= document.createElement("li");
//     // li.appendChild(document.createTextNode("testing"));
//     li.appendChild(document.createTextNode(input.value));
//     ul.appendChild(li);
//     input.value="";
// })

// # keyboard Event
input.addEventListener("keypress", function(event){
    if (input.value.length > 0 && event.key==="Enter"){
        var li = document.createElement("li");
        // li.appendChild(document.createTextNode("testing"));
        li.appendChild(document.createTextNode(input.value));
        ul.appendChild(li);
        input.value = "";
    }
})


