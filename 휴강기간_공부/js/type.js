let a = 123
/// let 과 const는 둘다 중복생성 x
/// let 은 재할당 가능
/// const 은 재할당 불가능 
const b = 'hello'
var c = 'asdf'

console.log(typeof 123)
let name = 'changwan'
//// 자바스크릅티에서  문자열 포맷팅을 할려면
/// `으로 감싸주고, ${변수명} 을 안에 써준다. template literal 이라 한다.
let hello_msg  = `hello ${name}`
console.log(hello_msg)

/// True False 가 소문자이다. true,false
/// empty_
console.log(undefined)

/// and 연산자는 && 이다.
/// or 연산자는 || 이다.
console.log(true && true)


/// 삼항 연산자 
result = true ? 1:2
console.log(result)