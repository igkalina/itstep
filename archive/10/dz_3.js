let select1 = document.getElementById("select1");
let select2 = document.getElementById("select2");
let radioButtons = document.getElementsByName("gr");
select1.addEventListener("change", function () {
  select2.innerHTML = "";
  if (select1.value === "Ukraine") {
    select2.add(new Option("Dnepr"));
    select2.add(new Option("Kiev"));
    select2.add(new Option("Lviv"));
  } else if (select1.value === "Poland") {
    select2.add(new Option("Krakow"));
    select2.add(new Option("Augustów"));
    select2.add(new Option("Alwernia"));
  } else if (select1.value === "France") {
    select2.add(new Option("Marseille"));
    select2.add(new Option("Lyon"));
    select2.add(new Option("Toulouse"));
  }
});
document.getElementById("myForm").addEventListener("submit", function (event) {
  event.preventDefault();
  let name1 = document.getElementById("name1");
  if (name1.value.length < 3 || name1.value.length > 13)
    name1.style.borderColor = "red";
  else if (name1.value.length >= 3) name1.style.borderColor = "";
  let name2 = document.getElementById("name2");
  if (name2.value.length < 3 || name2.value.length > 13)
    name2.style.borderColor = "red";
  else if (name2.value.length >= 3) name2.style.borderColor = "";
  let date = document.getElementById("date");
  let div = document.getElementById("newForm");
  let selectCheck = document.querySelectorAll('input[type="checkbox"]:checked');
  let valueCheck = [];
  selectCheck.forEach(function (selectCheck) {
    valueCheck.push(selectCheck.value);
  });
  div.style.display = "block";
  let firstname = document.getElementById("firstname");
  let lastname = document.getElementById("lastname");
  let birthday = document.getElementById("birthday");
  let country = document.getElementById("country");
  let city = document.getElementById("city");
  let skills = document.getElementById("skills");
  firstname.innerHTML = name1.value;
  lastname.innerHTML = name2.value;
  birthday.innerHTML = date.value;
  country.innerHTML = select1.value;
  city.innerHTML = select2.value;
  skills.innerHTML = valueCheck.join(", ");
});
let gender = document.getElementById("gender");
radioButtons.forEach(function (radioButtons) {
  radioButtons.addEventListener("change", function () {
    if (radioButtons.checked) {
      let selectOption = radioButtons.value;
      if (selectOption === "Male") {
        gender.innerHTML = radioButtons.value;
      } else if (selectOption === "Female") {
        gender.innerHTML = radioButtons.value;
      }
    }
  });
});
