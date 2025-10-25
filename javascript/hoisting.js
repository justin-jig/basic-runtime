


//함수 선언문과 함수 표현식
var sum =(a,b)=>{
    return a + '+' + b + '=' + (a+b)
}
console.log(sum(1,2))


function sum(a,b){
    return a+b
}
console.log(sum(3,4))

// 함수 스코프, 실행 컨텍스트에 관한 호이스팅
var a =1 ;

function outer(){
    console.log(a);
    function inner(){
        var a =3
        console.log(a)
    }
    inner();
    console.log(a);
}
outer()
console.log(a)