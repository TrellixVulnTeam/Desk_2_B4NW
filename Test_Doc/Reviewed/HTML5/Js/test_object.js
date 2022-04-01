//Javascript type: object

var user={
    name: "Jason",
    age: 34,
    spells: [1,3,4]
};

var arr=[
    {
        hr: 10,
        min: 30,
        sec: 100

    }
]

//facebook
var database=[
    {
        username: "andy",
        password: "song"
    }
];
var newsfeed=[
    {
        username: "Bobby",
        timeline: " Checked in"
    },
    {
        username: "Sally",
        timeline: "Javascript is so cool"
    }
];

var userNamePrompt=prompt("username?");
var passwordPrompt=prompt("password?");

function signIn(user, pass){
    if (user===database[0].username &&
        pass===database[0].password) {
            console.log(newsfeed);
        }else{
            alert("sorry, wrong user credentials")
        }
}

signIn(userNamePrompt, passwordPrompt);
