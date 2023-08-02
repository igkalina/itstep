//Создать html-страницу с таблицей.При наведении мышкой на ячейку таблицы, у этой ячейки должен меняться фон. Учтите, что когда мышку уводят с ячейки, то ее фон возвращается к прежнему. Выполнить задание с помощью JS, а не с помощью CSS.
let myTd = document.querySelector('td')
myTd.addEventListener('mouseover', function(){
    myTd.style.background = 'red'
})
myTd.addEventListener('mouseout', function(){
    myTd.style.background = 'white'
})
//Создать html-страницу с кнопкой Like, при нажатии на которую увеличивается счетчик лайков.
//css
		button{
            width: 100px;
            height: 50px;
            margin-top: 10px;
        }
        div{
            display: flex;	
            justify-content: center;
        }
//html
	<div>
        <button>Like</button>
	</div> 
//js
let myTd = document.querySelector('td')
myTd.addEventListener('mouseover', function(){
    myTd.style.background = 'red'
})
myTd.addEventListener('mouseout', function(){
    myTd.style.background = 'white'
})

let myButton = document.querySelector('button')
let a = 0
myButton.addEventListener('mousedown', function(){
    myButton.style.color = 'red'
    a += 1
    console.log('Количество лайков: ' + a);
})
myButton.addEventListener('mouseup', function(){
    myButton.style.color = 'black'

})
//Создать html-страницу «Калькулятор». Реализовать его функциональность
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <!-- <meta http-equiv="X-UA-Compatible" content="IE=edge"> -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        button{
            width: 50px;
            height: 50px;
            margin: 5px;
            font-size: 30px;
            border-radius: 10px;
        }
        input{
            margin: 10px 5px 5px 5px;
            height: 50px;
            width: 232px;
            font-size: 40px;
            border-radius: 10px;
            background-color: rgb(183, 245, 245);
            box-shadow: inset 0px 0px 30px -10px #000000;
        }
        #content{
            width: 252px;
            background: #646464;
            background: linear-gradient(to right, #646464 0%, #DCDCDB 50%, #C2BCC3 100%);
            margin: auto;
            border-radius: 10px;
            border: 2px solid #363636;
        }
        #reset{
            padding: 0;
            padding-top: 5px;
            font-size: 27px;
        }
        button:hover{
            box-shadow: inset 0px 0px 3px 1px rgba(0,0,0,0.59);
        }
    </style>
</head>
<body>
    <div id = 'content'>
        <input type="text" id="calc">
        <div>
            <button id="reset">CE</button>
        </div>
        <div>
            <button id="n1">1</button>
            <button id="n2">2</button>
            <button id="n3">3</button>
            <button id="signPlus">+</button>
        </div>
        <div>
            <button id="n4">4</button>
            <button id="n5">5</button>
            <button id="n6">6</button>
            <button id="signMinus">-</button>
        </div>
        <div>
            <button id="n7">7</button>
            <button id="n8">8</button>
            <button id="n9">9</button>
            <button id="signMulti">*</button>
        </div>
        <div>
            <button id="dot">.</button>
            <button id="n0">0</button>
            <button id="equals">=</button>
            <button id="singDivision">/</button>
        </div>
    </div>
    <script>
        let num_1 = document.querySelector('#n1')
let num_2 = document.querySelector('#n2')
let num_3 = document.querySelector('#n3')
let num_4 = document.querySelector('#n4')
let num_5 = document.querySelector('#n5')
let num_6 = document.querySelector('#n6')
let num_7 = document.querySelector('#n7')
let num_8 = document.querySelector('#n8')
let num_9 = document.querySelector('#n9')
let num_0 = document.querySelector('#n0')
let signP = document.querySelector('#signPlus')
let signM = document.querySelector('#signMinus')
let signMul = document.querySelector('#signMulti')
let signD = document.querySelector('#singDivision')
let eq = document.querySelector('#equals')
let dot = document.querySelector('#dot')
let ce = document.querySelector('#reset')
const inputElement = document.querySelector('#calc');
inputElement.value = 0
let sum = ''
num_1.addEventListener('click',function(){
    inputElement.value += 1
    sum+= 1
    if(inputElement.value==01) inputElement.value = '1'
})
num_2.addEventListener('click',function(){
    inputElement.value += 2
    sum+= 2
    if(inputElement.value==02) inputElement.value = '2'
})
num_3.addEventListener('click',function(){
    inputElement.value += 3
    sum+= 3
    if(inputElement.value==03) inputElement.value = '3'
})
num_4.addEventListener('click',function(){
    inputElement.value += 4
    sum+= 4
    if(inputElement.value==04) inputElement.value = '4'
})
num_5.addEventListener('click',function(){
    inputElement.value += 5
    sum+= 5
    if(inputElement.value==05) inputElement.value = '5'
})
num_6.addEventListener('click',function(){
    inputElement.value += 6
    sum+= 6
    if(inputElement.value==06) inputElement.value = '6'
})
num_7.addEventListener('click',function(){
    inputElement.value += 7
    sum+= 7
    if(inputElement.value==07) inputElement.value = '7'
})
num_8.addEventListener('click',function(){
    inputElement.value += 8
    sum+= 8
    if(inputElement.value==08) inputElement.value = '8'
})
num_9.addEventListener('click',function(){
    inputElement.value += 9
    sum+= 9
    if(inputElement.value==09) inputElement.value = '9'
})
num_0.addEventListener('click',function(){
    inputElement.value += 0
    sum+= 0
    if(inputElement.value==00) inputElement.value = '0'
})
eq.addEventListener('click', function(){
    inputElement.value = eval(sum)
    console.log(sum);
})
signP.addEventListener('click', function(){
    sum += '+'
    inputElement.value = ''
})
signM.addEventListener('click', function(){
    sum += '-'
    inputElement.value = ''
})
signMul.addEventListener('click', function(){
    sum += '*'
    inputElement.value = ''
})
signD.addEventListener('click', function(){
    sum += '/'
    inputElement.value = ''
})
dot.addEventListener('click', function(){
    sum += '.'
    inputElement.value += '.'
})
ce.addEventListener('click', function(){
    sum = ''
    inputElement.value = '0'
})

    </script>
</body>
</html>
//Создать html-страницу с кнопкой, по нажатию на которую добавляются цветные блоки на страницу. По клику на сам блок, он должен удаляться со страницы.