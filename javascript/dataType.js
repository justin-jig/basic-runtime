/**
 * 자료형 datatype
 */


/** 문자열  ( ''. "", `` ) */
let string = "안녕하세요.";
let string2 = '안녕하세요.2';
let string3 = `안녕하세요.3`;
let string4 = `안녕하세요2 ${5}`
let rtr = string + 'justin';


/** 숫자형  (정수 및 소수점 숫자를 나타냄 ) */
let number = 123;
let opacity = 0.7;


/** 논리형  (참 true , 거짓 false )*/
let checked = true;
let isShow = false;

/** undified형 미할당 데이터 */
let undef;
let obj = {
    abc :123
}

/** null형 의도된 빈 데이터 */
let empty = null

/** array 배열 데이터 
 *  indexing, 
 *  index는 0부터 시작함
 *  push(),pop(), unshift(), shift(), indexOf(), includes()
*/
let names = ["홍길동", "성춘향", "짱구"];

console.log(names.length); //배열의 갯수

names.push("짱아"); // 배열의 마지막값 추가 ["홍길동", "성춘향", "짱구", "짱아"]
console.log("names", names);

names.pop(""); // 배열의 맨 마지막값을 삭제 ["홍길동", "성춘향", "짱구"]
console.log("names", names);

names.unshift("신형만"); // 배열의 맨 앞에 값을 추가 ["신형만", "홍길동", "성춘향", "짱구"]
console.log("names", names);

names.shift(); // 배열의 맨 앞에 값을 삭제 ["홍길동", "성춘향", "짱구"]
console.log("names", names);

names.indexOf("짱구"); // 배열 안에 값이 포함되어 있는지 찾는 방법 특정값이 나옴
// 값이 있을 때는 인덱스 값, 없을 때 -1
let index = names.indexOf("짱구");
console.log("names", index);

names.includes(); // 배열 안에 값이 포함되어 있는지 판별하는 기능
// 값이 있을 때는 true, 없을 때 false
let bool = names.includes("짱아");
console.log("names", bool);


/** object 형 데이터 */

let obj1 = {
    age: 5,
    name : "낭이",
    mew : function() {
        console.log("야옹");
    }
};

let obj2 = {
    name : "초코"
}
console.log(obj1);
console.log(obj1.age);
console.log(obj1.name);
console.log(obj2.name);
obj1.mew();