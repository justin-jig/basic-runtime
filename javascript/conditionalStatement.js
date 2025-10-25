/**
 * 조건문 = 조건에 따라 다른 스크립트를 실행
 */


/** if문 */
if (false) { 

} else if (false) { // 조건 1이 아니면서 다음조건(else if)을 만족하는 경우 true

} else { // 위 조건들이 만족지 않으면

}

let isShow = true;
if (isShow) {
    // 위조건이 참일 경우 실행
    console.log('show!');
} else {
    // 위 조건이 거짓일 경우 실행
}


/** switch 문 */

let num = "성춘향"; 

switch (num) {

    case "성춘향":
    console.log("여자");
    break;
    case "홍길동":
    console.log("남자");
    break;
    default : 
    break;
}

/** 삼항 연산자 
 *  조건? 참일 경우 실행할 코드 : 거짓일 경우 실행할 코드
 * 
*/
let age = 18;   
(age >= 20 && age < 100) ? console.log('성인') : console.log('미성년자');

let state = (age >= 20 && age < 100) ? "성인" : "미성년자";
