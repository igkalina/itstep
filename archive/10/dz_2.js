function check() {
  let login = document.getElementById("login");
  let pas1 = document.getElementById("pas_1");
  let pas2 = document.getElementById("pas_2");
  let email = document.getElementById("email");
  if (login.value.length < 4) {
    login.style.borderColor = "red";
    alert("Логин менее 4 знаков");
    return false;
  } else if (pas1.value != pas2.value) {
    pas1.style.borderColor = "red";
    pas2.style.borderColor = "red";
    alert("Пароли отличаются между собой");
    return false;
  } else if (pas1.value.length < 5 && pas2.value.length < 5) {
    pas1.style.borderColor = "red";
    pas2.style.borderColor = "red";
    alert("В пароле менее 5 знаков");
    return false;
  } else {
    alert("На почту " + email.value + " отправлено письмо с подтверждением");
    document.getElementById("sbmt").submit;
  }
}
