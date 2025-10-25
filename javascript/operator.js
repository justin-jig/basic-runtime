/** 연산자 (operator) 
 * 대입 연산자 : =
 * 비교 연산자 : ==, !=, ===
 * 산술 연산자 : +,-,*,/
 * 논리 연산자 : !,&&,||
*/

let num;
num = 5
let numString = "5";


console.log(num != 3);
console.log(num > 3);
console.log(num <= 3);


console.log(num + 5)
console.log(num - 5)
console.log(num * 5)
console.log(num / 5)


console.log(num === numString)


console.log((num % 4) == 0) 
// num 나누기 2를 했을 때 나머지를 출력

console.log(num ** 3) 
// num(5)의 3승


// 증가, 감소 연산자
num += 5; // num = num + 5
num *= 5; // num = num * 5

num = num + 1;
num +=1;
num ++;

num = num - 1;
num -=1;
num --;

// 논리 연산자 ( ==, !=, <, <=, >, >=, ===, !==)

console.log(true && false);
// && => and 연산 : 앞과 뒤가 모두 참일 때, true를 반환 

console.log(true || false);
// || => or 연산 : 앞과 뒤 중 하나라도 참일 경우, true 반환

console.log(!true);
// ! => Not 연산 : 반대로 연산됨







