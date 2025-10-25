
/** func 함수 */

/** 함수 선언문
 * 
*/
sayHellow();
function sayHellow() { // 함수 선언문
    console.log('say hellow')
}

/** 함수 표현식
 * 
*/
const sayHellow2 = function () { // 함수 표현식
    console.log('say hellow')
}

/** 화살표 함수
 * 
 */
const sayHellow3 = () => { 
    console.log("hellow3");
}


/** 매개변수, 반환값
 *  매개변수 = 함수 외부에서 사용한 변수, 값 등을 함수 내부로 전달하고 싶을 때 사용
 *  반환값 : 함수 내부에서 생성된 변수, 값 등을 함수 외부로 전달하고 싶을 때 사용 (return)
 */

// 1. 매개변수 x 반환값 x
function aaa () {
    console.log('aaa');
}
// 2. 매개변수 x 반환값 o
function bbb () {
    return 'bbb'
}

let number1 = 5;
let number2 = 3;
// 3. 매개변수 o 반환값 x
function ccc (num1, num2) {
    console.log(num1 + num2);
}
ccc(number1, number2);

let number3 = 5;
// 3. 매개변수 o 반환값 o
function ddd (num1) {
    console.log(num1);
    return num1 + 5 
}
ddd(number3);


