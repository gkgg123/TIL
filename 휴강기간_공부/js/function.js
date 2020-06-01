function hello(){
    console.log('hello')
}

hello()


const world = function(){
    console.log('world')
}
world()


const js = () => {
    console.log('js')
}
js()

const python = (a) => {
    console.log(a)
}
python('hello python');
///// 즉시 실행 함수 /////
(function(){ console.log('python')})();
///////////////////////
let numbers = [6,2,3,4,5]

// for (let number of numbers){
//     console.log(number*2)
// }

// const hello = (num) => {
//     console.log(num*2)
// }

// numbers.forEach(hello)