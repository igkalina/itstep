// let str1 = prompt('enter 1 text')
// let str2 = prompt('enter 2 text')
// function compareText(){
//     if(str1.length>str2.length) return 1
//     else if(str1.length<str2.length) return -1
//     else if(str1.length==str2.length) return 0
// }
// console.log(compareText(str1,str2));
let counter = 0;
let minute = 0;
let id = 0;
let stp = document.getElementById("stp");
let play = document.getElementById("play");
let pause = document.getElementById("pause");
stp.addEventListener("click", function () {
  clearInterval(id);
  minute = 0;
  counter = 0;
  sec.innerHTML = counter;
  min.innerHTML = minute;
});
play.addEventListener("click", function () {
  id = setInterval(function () {
    counter++;
    sec.innerHTML = counter;
    if (counter == 60) {
      counter = 0;
      minute++;
      min.innerHTML = minute;
    }
  }, 10);
});
pause.addEventListener("click", function () {
  clearInterval(id);
});

let currentData = new Date();
console.log(currentData);
let oldData1 = new Date("2023-06-18");
console.log(oldData1);

setInterval(function(){
    day.innerHTML = (Math.round((oldData1 - currentData) / 24 / 60 / 60 / 1000));
    
    minute.innerHTML = (Math.round((oldData1 - currentData)  / 60 / 1000));
    console.log(minute);
})