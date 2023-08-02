//Решетки
let userNumber = +prompt('Укажите цифру')
for (let i = 0; userNumber > 0; userNumber--) {
    console.log('#'+userNumber);  
}
//От 10 до 0
let i = 10
while(i>=0){
    console.log(i);
    i--
}
//Степень
let userNumber = +prompt('Укажите число')
let degree = +prompt('Укажите степень')
let result = userNumber
for (let index = degree; index > 1; index--) {
    result *= userNumber
}
alert(result)
//Сравнение чисел
function greaterNumber(num_1, num_2){
    if(num_1<num_2){
        return -1
    }else if(num_1>num_2){
        return 1
    }else{
        return 0
    }
}
console.log(greaterNumber(1, 1)); 
//Подсчитать сумму всех чисел в заданном пользователем диапазоне. 
let num_1 = +prompt('Укажите первое число диапазона')
let num_2 = +prompt('Укажите последнее число диапазона')
let sum = 0
function sumOfNumb(num_1, num_2){
    for (let index = num_1; index <= num_2; index++) {
        sum += index
    }
    return sum
}
console.log(sumOfNumb(num_1, num_2));
//Запросить у пользователя число и вывести все делители этого числа.
let num_1 = +prompt('Укажите число')
let i = 1
while (i<=num_1) {
   if(num_1%i==0){
    console.log('Делитель числа '+num_1+' : '+i);
   }
   i++
}
//Определить количество цифр в введенном числе.
let num_1 = +prompt('Укажите число')
let i = 0
while(num_1>1){
    num_1/=10
    i++
}
console.log(i);
//Запросить у пользователя 10 чисел и подсчитать, сколько он ввел положительных, отрицательных и нулей. При этом также посчитать, сколько четных и нечетных. Вывести статистику на экран.
let positiveNum = 0
let negativeNumber = 0
let zero = 0
let even = 0
let odd = 0
for (let index = 1; index <= 10; index++) {
    let num_1 = +prompt('Укажите число')
    if(num_1>=1){
        positiveNum += 1
    }else if(num_1<0){
        negativeNumber += 1
    }else if(num_1==0){
        zero += 1
    }
    if(num_1%2==0){
        even += 1
    }
    else if(num_1%2!=0){
        odd +=1
    }
}
console.log('Положительных чисел: '+positiveNum);
console.log('Отрицательных чисел: '+negativeNumber);
console.log('Нулей: '+zero);
console.log('Чётных: '+even);
console.log('Нучётных: '+odd);
//Зациклить калькулятор. Запросить у пользователя 2 числа и знак, решить пример, вывести результат и спросить, хочет ли он решить еще один пример. И так до тех пор, пока пользователь не откажется.
let num_1 = 0
let num_2 = 0
let sign = ''
let sum = 0
let toggle = true
while (toggle) {
    num_1 = +prompt('Введите первого число')
    num_2 = +prompt('Введите второе число')
    sign = prompt('Введите знак')
    switch(sign){
        case '+': sum = num_1+num_2
        break
        case '-': sum = num_1-num_2
        break
        case '*': sum = num_1*num_2
        break
        case '/': sum = num_1/num_2
        break
    }
    alert(sum)
    toggle = confirm('Хотите повторить запрос?')
}
//Вывести таблицу умножения для всех чисел от 2 до 9. Каждое число необходимо умножить на числа от 1 до 10.
let sum = 0
for (let number = 2; number <= 9; number++) {
    for (let factor = 1; factor <= 10; factor++) {
        sum = number*factor
        console.log(sum);
    }
    console.log('');
}
//Написать функцию, которая принимает 2 числа и знак (+ - * /), считает пример и возвращает результат.
num_1 = +prompt('Введите первого число')
num_2 = +prompt('Введите второе число')
sign = prompt('Введите знак')
function calc(num_1, num_2, sign){
    switch(sign){
        case '+': sum = num_1+num_2
        break
        case '-': sum = num_1-num_2
        break
        case '*': sum = num_1*num_2
        break
        case '/': sum = num_1/num_2
        break
    }
    return sum
}
console.log(calc(num_1, num_2, sign));
//Написать функцию, которая проверяет, является ли переданное ей число простым.
num_1 = +prompt('Введите число')
function primeNumber(num_1){
    for (let index = 2; index < num_1; index++) {
        if(num_1%index==0){
                console.log('Не простое');
                break
        }else{
            console.log('Простое');
            break
        }
    }
}
primeNumber(num_1)
//Написать функцию, которая принимает число и выводит таблицу умножения для этого числа. Вызовите функцию для всех чисел от 2 до 9.
let num = +prompt('Введите число')
function calc(x){
        for (let factor = 1; factor <= 10; factor++) {
            sum = num*factor
            console.log(sum);
        }
    }
calc(num)
//Написать функцию, которая выводит все четные или нечетные числа, в указанном пользователем диапазоне. Какиечисла выводить, определяется третьим параметром типа bool (true – четные, false – нечетные).
alert('Задайте диапазон')
let num_1 = +prompt('Начальное число')
let num_2 = +prompt('Последнее число')
let check = confirm('Вы хотите увидеть чётные числа?')
function evenOdd(num_1, num_2, check){
    for (let index = num_1; index <= num_2; index++) {
        if(check==true){
            if(index%2==0&&index!=0){
                console.log('Чётные числа с указанного диапазона: '+index);
            }
        }else if(check==false){
            if(index%2!=0){
                console.log('Не чётные числа с указанного диапазона: '+index);
            }
        }
    }
}
evenOdd(num_1, num_2, check)