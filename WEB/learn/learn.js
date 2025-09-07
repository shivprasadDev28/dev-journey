/*

// Basics
console.log(`Hello`);
console.log(`I Like Pizza`);

window.alert(`This is an alert`);
window.alert(`I LIKE PIZZA`);

document.getElementById("myh1").textContent = `Hello`;
document.getElementById("myp").textContent = `I Like Pizza`;


// Variables
let x = 123;

console.log(x);

let age = 21;

console.log(typeof age);

let fname = "Shiv";

console.log(typeof fname);
let isonline = true;

console.log(isonline);

// Arithmetic Operators
+ - * / % **


let s = 1;
//s = s + 1;
//s = s - 1;
//s = s / 1;
//s = s * 1;
//s1 = s % 1; // for modulus use seperate variable
//s = s ** 2;
console.log(s);

+= -= *= /= **= %=

s++, s--

presedence = (), **, *, /, %, +, -


// input
let uname;

uname = window.prompt();
console.log(uname)


let un;
document.getElementById("mysubmit").onclick = function(){
    un = document.getElementById("mytext").value;
    document.getElementById("welcome").textContent = `Hello ${un}`;
}

//type conversion
let age = window.prompt("How old are you?");
age = Number(age);
age+=1;

console.log(age);

let un = 0;

document.getElementById("mysubmit1").onclick = function(){
    un--;
    document.getElementById("welcome").textContent = un;
}

document.getElementById("mysubmit2").onclick = function(){
    un = 0;
    document.getElementById("welcome").textContent = un;
}

document.getElementById("mysubmit3").onclick = function(){
    un++;
    document.getElementById("welcome").textContent = un;
}
    

let min = 1;
let max = 6;
let rn;
document.getElementById("but").onclick = function(){
    rn = Math.floor(Math.random()*max)+min;
    document.getElementById("lab").textContent = rn;
}

const minval = 1;
const maxval = 100;
const ans = Math.floor(Math.random() * maxval - minval + 1)+minval;

let a = 0;
let g;
let running = true;

while(running){
    g = window.prompt("Enter your guess from 1 to 100");
    g = Number(g);

    if(isNaN(g)){
        window.alert("Enter valid");
    }
    else if(g < minval || g > maxval){
        window.alert("Enter Valid");
    }
    else{
        a++;
        if (ans == g){
            window.alert(`Thats correct the number is ${g} and you took ${a} tries`);
            running = false;
        }
        else if (ans > g){
            window.alert("correct number is greater");
        }
        else{
            window.alert("correct number is smaller");
        }
    }
}
*/

