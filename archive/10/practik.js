function check(){
    let checkLog = document.getElementById('lg')
    let pasLog = document.getElementById('ps')
    if(checkLog.value.length<3||pasLog.value.length<5||pasLog.value.length>10){
        checkLog.style.borderColor = 'red'
        pasLog.style.borderColor = 'red'
        return false
    }else{
        document.getElementById('myForm').submit
    }
}