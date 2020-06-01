
//// 기본 for 문법
for (let a = 0 ; a < 5 ; a++){
    console.log('hello')
}

let menus = ['짜장면','짬뽕','탕수육']

for (let menu of menus ){
    console.log(menu)
    /// 주의할점은 menu도 for문 안에서만 돌아가는 변수이지만, 할당을 해줘야한다.
}


for (let menu in menus){
    console.log(menu)
}

let numbers = {
    '광주':062,
    '서울':02,
}


/// key가 발생
for (let number in numbers){
    console.log(number)
}


//// 에러가 발생
// for (let number of numbers){
//     console.log(number)
// }

menus.forEach(function(menu)){
    console.log(menu)
}