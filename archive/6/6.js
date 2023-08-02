//Возвраст
let a = prompt('Сколько вам лет?')
if(a>=0 && a<=12){
    alert('Ребёнок')
}else if(a>=13&&a<=18){
    alert('Подросток')
}else if(a>=19&&a<=60){
    alert('Взрослый')
}else if(a>=60&&a<=100){
    alert('Пенсионер')
}else{
    alert('Возвраст должен быть от 0 до 100 лет')
}
//Спец. символы
let a = +prompt('Введите число')
let res
switch(a){
    case 1: 
        res = '!';
        break
    case 2: 
        res = '@';
        break
    case 3: 
        res = '#';
        break
    case 4: 
        res = '$';
        break
    case 5: 
        res = '%';
        break
    case 6: 
        res = '^';
        break
    case 7: 
        res = '&';
        break
    case 8: 
        res = '*';
        break
    case 9: 
        res = '(';
        break
    case 0: 
        res = ')';
        break
}
alert(res)
//Одинаковые числа
let a = +prompt('Введите 3-х значное число')
let res_1 = a%10
let res_2 = (a/10)%10
let res_3 = (a/100)%10
if(res_1==Math.floor(res_2)||res_1==Math.floor(res_3)||Math.floor(res_2)==Math.floor(res_3)){
    alert('Одинаковые цифры найдены');
}else{
    alert('Одинаковые цифры НЕ найдены');
}
//Высокостный год
let a = +prompt('Укажите год')
if(a%400==0||a%4==0&&a%100!==0){
    alert('Это высокостный год')
}else{
    alert('Это НЕ высокостный год')
}
//Полиндром
let a = +prompt('Введите 5-ти значное число')
let res_1 = a%10
let res_2 = (a/10)%10
let res_3 = (a/100)%10
let res_4 = (a/1000)%10
let res_5 = (a/10000)%10
if (res_1==Math.floor(res_5)&&Math.floor(res_2)==Math.floor(res_4)) {
    alert('Число палиндром')
}else{
    alert('Число НЕ палиндром')
}
//Конвертор валют
let usd = +prompt('Укажите сумму в USD')
let val = +prompt('Укажите валюту (цифру) для конвертации: 1. EUR 2. UAH 3. AZN')
let convert
switch(val){
    case 1:
        convert = usd*0.93;
        break
    case 2:
        convert = usd*36.93;
        break
    case 3:
        convert = usd*1.7;
        break
}
alert(convert)
//Скидка
let sum = +prompt('Укажите сумму покупки')
let sale
if(sum>200&&sum<=300){
    sale = (sum-(sum*3)/100)
    alert('Ваша сумма с учётом скидки (3%): ' + sale)
}else if(sum>300&&sum<=500){
    sale = (sum-(sum*5)/100)
    alert('Ваша сумма с учётом скидки (5%): ' + sale)
}else if(sum>500){
    sale = (sum-(sum*7)/100)
    alert('Ваша сумма с учётом скидки (7%): ' + sale)
}else{
    alert('Скидка не предусмотрена')
}
//Вписаный круг
let circumference = +prompt('Укажите длину окружности')
let perimeterSquare = +prompt('Укажите периметр квадрата')
let sCircle = (circumference**2)/(4*Math.PI) //площадь круга 
let sSquare = (perimeterSquare/4)**2 //площадь квадрата
//Площадь круга меньше площади квадрата в 4/π раза тогда ок
if((sCircle/(4/Math.PI)<sSquare)){ 
    alert('Круг вписан')
}else{
    alert('Круг не вписан')
}
console.log('площадь круга: ' + sCircle);
console.log('площадь квадрата: ' + sSquare);
//Викторина
let question_1 = +prompt('Кто из следующих художников был активистом движения "Дадаизм"? Варианты: 1.Пабло Пикассо 2.Винсент ван Гог 3.Марсель Дюшан')
let question_2 = +prompt('Какой французский писатель является автором романа "Ищите время, чтобы любить"? Варианты: 1.Гюстав Флобер 2.Эмиль Золя 3.Андре Жид')
let question_3 = +prompt('Какой из следующих химических элементов относится к группе инертных газов? Варианты: 1.кислород (O) 2.азот (N) 3.неон (Ne)')
let counter = 0;
counter = (question_1==3) ? counter+2:counter
counter = (question_2==1) ? counter+2:counter
counter = (question_3==3) ? counter+2:counter
alert('Количество набранных баллов: ' + counter)
//Следующая дата
let day = +prompt('Укажите дату')
let mounth = +prompt('Укажите месяц')
let year = +prompt('Укажите год')
    if(day==31&&mounth==12){
        day=1
        mounth=1
        year++
        alert('Следующий день от заданной даты: '+day+' число '+mounth+' месяц '+year+' год.')
    }else if(day==31&&(mounth==1||mounth==3||mounth==5||mounth==7||mounth==8||mounth==10)){
        mounth++
        day = 1
        alert('Следующий день от заданной даты: '+day+' число '+mounth+' месяц '+year+' год.')
    }else if(day==30&&(mounth==4||mounth==6||mounth==9||mounth==11)){
        mounth++
        day = 1
        alert('Следующий день от заданной даты: '+day+' число '+mounth+' месяц '+year+' год.')
    }else if(day>28&&year%4!=0&&mounth==2){
        alert('Ошибка ввода: Не высокостный год, в феврале 28 дней.')
    }else if((day==28||day==29)&&mounth==2){
        mounth++
        day = 1
        alert('Следующий день от заданной даты: '+day+' число '+mounth+' месяц '+year+' год.')
    }else if(day>31||day<1&&(mounth== 1||mounth==3||mounth== 5||mounth== 7||mounth== 8||mounth==10)||(day>30||day<1)&&(mounth==4||mounth==6||mounth== 9||mounth==11)){
        alert('Ошибка ввода: не верная дата')
    }else{
        day++
        alert('Следующий день от заданной даты: '+day+' число '+mounth+' месяц '+year+' год.')
    }