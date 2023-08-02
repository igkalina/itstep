// let a = prompt('Введите строку')
// function upper(){
//     let i = a.charAt(0)
//     i = i.toUpperCase()
//     i += a.slice(1)
//     return i
// }
// console.log(upper());

// var userText = prompt("Введите строку");
// function searchSpam(userText) {
//   spam = userText.toLowerCase();
//   spamWords = [
//     "100% бесплатно",
//     "увеличение продаж",
//     "только сегодня",
//     "не удаляйте",
//     "xxx",
//   ];
//   for (let word of spamWords) {
//     if (userText.includes(word)) return true;
//   }
//   return false;
// }
// console.log(searchSpam(userText));

// function reduction(str, maxLength){
//     if(str.length>maxLength){
//         res = str.slice(0, maxLength) + '...'
//     }
//     return res
// }
// alert(reduction(prompt('Введите строку'), +prompt('Введите количество отображаемых знаков')));

// function polyndrom(str) {
//   let a = [];
//   for (let index = 0; index < str.length; index++) {
//     a[index] = str[index];
//   }
//   if (
//     a[0] === a[a.length - 1] &&
//     a[1] === a[a.length - 2] &&
//     a[2] === a[a.length - 3]
//   )
//     return console.log("Палиндром");
//   else return console.log("Не палиндром");
// }
// polyndrom(prompt("Введите слово"));

// function countWords(str){
//     let a = str.split(' ')
//     return a.length
// }
// alert('Это предложение содержит ' + countWords(prompt('Введите предложение')) + ' слов.')

// function maxLength(str) {
//   let words = str.split(" ");
//   let max = "";
//   for (let word of words) {
//     if (word.length > max.length) {
//       max = word;
//     }
//   }
//   return max;
// }
// alert("Самое длинное слово " + maxLength(prompt("Введите предложение")));

// function calculateDaysUntilNextBirthday(birthdate) {
//   const today = new Date(); // Текущая дата
//   const nextBirthday = new Date(
//     today.getFullYear(),
//     birthdate.getMonth(),
//     birthdate.getDate()
//   ); // Дата следующего дня рождения

//   // Если день рождения в этом году уже прошел, увеличиваем год следующего дня рождения на 1
//   if (nextBirthday < today) {
//     nextBirthday.setFullYear(nextBirthday.getFullYear() + 1);
//   }

//   // Разница в миллисекундах между текущей датой и следующим днем рождения
//   const timeDiff = nextBirthday.getTime() - today.getTime();

//   // Конвертируем разницу в днях
//   const daysUntilNextBirthday = Math.ceil(timeDiff / (1000 * 3600 * 24));

//   return daysUntilNextBirthday;
// }

// // Пример использования
// const userInput = prompt("Введите дату своего рождения в формате ДД-ММ-ГГГГ");
// const birthdateParts = userInput.split("-");
// const birthdate = new Date(
//   birthdateParts[2],
//   birthdateParts[1] - 1,
//   birthdateParts[0]
// );

// const daysUntilNextBirthday = calculateDaysUntilNextBirthday(birthdate);

// alert('До вашего следующего дня рождения осталось ' + daysUntilNextBirthday + ' дней')
