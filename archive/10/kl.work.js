let phoneCounter
function addClick(){
    if(typeof phoneCounter == 'undefined') phoneCounter = 1
    phoneCounter++
    let b = document.createElement('br')
    let f = document.forms[0]
    f.appendChild(b)
    let t = document.createTextNode('Phone number ')
    f.appendChild(t)
    let phoneInput = document.createElement('input')
    phoneInput.type = 'text'
    phoneInput.name = 'phone'+phoneCounter
    phoneInput.placeholder = 'Enter phone number'
    f.appendChild(phoneInput)
    let t2 = document.createTextNode(' Phone type ')
    f.appendChild(t2)
    let selector = f.elements['type']
    let newSelector = selector.cloneNode(true)
    newSelector.name = 'type' + phoneCounter
    f.appendChild(newSelector)
    let t3 = document.createTextNode(' Priority ')
    f.appendChild(t3)
    let mainRadio = document.createElement('input')
    mainRadio.type = 'radio'
    mainRadio.name = 'name'
    mainRadio.value = phoneCounter
    f.appendChild(mainRadio)
}
// function checkForm(event){
//     event.preventDefault()
//     let name = document.getElementById('name')
//     if (name.value.length<3) {
//         name.style.borderColor = 'red'
//         return false
//     } else {
//         return true
//     }
function checkForm(){
    let name = document.getElementById('name')
    if (name.value.length<3) {
        name.style.borderColor = 'red'
        return false
    } else {
        document.getElementById('myForm').submit
    }
}
