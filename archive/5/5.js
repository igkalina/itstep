//Растояние/скорость
let a = prompt('Растояние, км')
let b = prompt('Скорость, км/ч')
let res = ((a/b)*3600)/ 60
alert ("Время в пути " + Math.floor(res) + " мин.")
//Долларв в евро
let a = prompt('Доллары')
let res = a*.9301
alert (a + " долларов = " + Math.floor(res) + " евро.")
//Флешка
let a = prompt('Объём флешки')
let res = a/.820
alert ("Количество помещаемых файлов размером 820 МБ на флешку " + a + "Гб = " + Math.floor(res) )
//Шоколадки
let a = prompt('Количество денег в кошельке, грн')
let b = prompt('Стоимость шоколадки')
let res = a/b
let res_1 = a%b
alert ("Можно купить " + Math.floor(res) + " шоколадок. Останется в кошельке " + Math.floor(res_1* 100 ) / 100 + " грн")
//Число задом наперёд
let a = prompt('Число')
let res_1 = a%10
let res_2 = (a/10)%10
let res_3 = (a/100)%10
alert ("Число задом на перёд " + res_1 + Math.floor(res_2) + Math.floor(res_3))
//чётное нечётное
let a = prompt('Число')
let res
res=(a%2==0) ? 'чётное':'нечётное'
alert ("Число " + a + ' ' + res)
