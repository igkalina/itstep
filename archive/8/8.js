//Прямоугольник
let rectangle = {
    ab: 4,
    bc: 3,
}
function rectangleCord (rectangle){
    for(let r2 in rectangle){
        console.log(r2);
        console.log(rectangle[r2]);
    }
}
function rectangleWidth (rectangle){
    console.log("Ширина: " + rectangle.ab);
}
function rectangleHeight(rectangle){
    console.log("Высота: " + rectangle.bc);
}
function rectangleSquare(rectangle){
    console.log('Площадь: ' + rectangle.ab * rectangle.bc);
}
function rectanglePerimeter(rectangle){
    console.log('Периметр: ' + 2*(rectangle.ab + rectangle.bc));
}
rectangleCord(rectangle)
rectangleWidth(rectangle)
rectangleHeight(rectangle)
rectangleSquare(rectangle)
rectanglePerimeter(rectangle)
//Массив, чётное нечётное 
let a = [1,3,2,4,5,7,8,3,22,42]
let even = 0
function seeArray(){
    for (let i = 0; i < a.length; i++) {
        if(a[i]%2==0){
            console.log(a[i]);
        }
    }
}
seeArray(a)
//Вывод массива
let a = [1,3,2]
function seeArray(a){
    alert(a);
}
seeArray(a)
//Задание 1
let rectangle = {
    ab: 4,
    bc: 3,
}
function rectangleCord (rectangle){
    for(let r2 in rectangle){
        console.log(r2);
        console.log(rectangle[r2]);
    }
}
function rectangleHeight(rectangle){
    console.log("Высота: " + rectangle.bc);
}
function rectangleSquare(rectangle){
    console.log('Площадь: ' + rectangle.ab * rectangle.bc);
}
function rectanglePerimeter(rectangle){
    console.log('Периметр: ' + 2*(rectangle.ab + rectangle.bc));
}
function widthChange(){
    rectangle.ab = prompt('Укажите ширину')
    return rectangle.ab
}
function heightChange(){
    rectangle.bc = prompt('Укажите высоту')
    return rectangle.bc
}
function rectangleWidth (rectangle){
    console.log("Ширина: " + rectangle.ab);
}
function changeWH(a,b){
    rectangle.ab = a
    rectangle.bc = b
}
function widthChangeX(){
    rectangle.ab += +prompt('Укажите ширину')
    return rectangle.ab
}
function heightChangeY(){
    rectangle.bc += +prompt('Укажите высоту')
    return rectangle.bc
}
function changeWHY(a,b){
    rectangle.ab += +a
    rectangle.bc += +b
}
function pointCoordinates(rectangle, a, b){
    if(a<rectangle.ab&&b<rectangle.bc) alert('Точка находится в прямоугольнике')
}
pointCoordinates(rectangle, +prompt('Координаты точки по X'), +prompt('Координаты точки по Y'))
//changeWHY(+prompt('Ширина'), +prompt('Высота'))
// heightChangeY(rectangle)
// widthChangeX(rectangle)
//changeWH(+prompt('Ширина'), +prompt('Высота'))
//widthChange(rectangle)
//heightChange(rectangle)
// rectangleCord(rectangle)
rectangleWidth(rectangle)
rectangleHeight(rectangle)
// rectangleSquare(rectangle)
// rectanglePerimeter(rectangle)
//Задание 2
//Функция принимает массив и возвращает сумму всех элементов массива.
let arr = [1,23,4,5,63,25,566,3,4,6]
let sum = 0
function sumArr(){
    for (let i = 0; i < arr.length; i++) {
        sum +=arr[i]
        console.log(sum);
    }
}
sumArr(arr)
//Функция принимает массив и возвращает его максимальный элемент.
let arr = [1,23,4,5,63,25,566,3,4,6]
let sum = 0
function sumArr(){
    for (let i = 0; i < arr.length; i++) {
        if(arr[i]>sum) sum = arr[i]
    }
    console.log(sum);
}
sumArr(arr)
//Функция добавления нового элемента в массив по указанному индексу.
let arr = [1,23,4,5,63,25,566,3,4,6]
let userIndex = +prompt('Введите индекс')
if(userIndex<arr.length){
    arr[userIndex] = +prompt('Ведите значение')
}
console.log(arr);
//Функция удаления элемента из массива по указанному индексу.
let arr = [1,23,4,5,63,25,566,3,4,6]
let userIndex = +prompt('Введите индекс')
if(userIndex<arr.length){
    arr.splice(userIndex, 1)
}
console.log(arr);