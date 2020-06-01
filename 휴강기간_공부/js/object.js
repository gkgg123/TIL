const me = {
    name: 'change',
    location : 'gj',
    language : ['python','js','sql'],
    product : {
        phone :'iphone',
        computer : 'desktop',
    },
    greeting : function( num ){return num*2},
    double : (num) => {return num*2},


}

// console.log(me.double(5))


let meJson = JSON.stringify(me)

console.log(meJson)
let newMe =JSON.parse(meJson)
console.log(newMe)