var formData={
    username:'hong',
    password:'1q2w3e4r',
    password_confirmation:'1q2w3e4r'
}
var user=['hong','choi','kim']
function isValid(inputData,subs){
    if (subs.indexOf(inputData['username'])>=0){
        alert('존재하는회원입니다.')
    }
    else{
        if (inputData.password==inputData.password_confirmation){
            alert(inputData.username+'님 회원축하합니다.')
        }
        else{
            alert('비밀번호가 일치하지 않습니다.')
        }
    }
}
isValid(formData,user)
