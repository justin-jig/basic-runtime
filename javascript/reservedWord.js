/**
    예약어  
    특별한 의미를 가지고 있어, 변수나 함수 이름 등으로 사용할 수 없는 단어

*/ 

/** 
    변수 
        - 변수란 특정 값을 저장하는 공간
        - 데이터를 저장하고 참조(사용)하는 데이터의 이름
        - 키워드(var, let, const) 변수이름 = 값

    변수 규칙
        - 이름으로는 문자 / 숫자 / $ / _
        - 첫글자는 숫자가 될 수 없다.
        - 예약어도 사용할 수 없다.
        - 상수는 대문자로 선언함

 * */ 

var number = 5; // 변수의 선언과 할당
var number1; // 변수 선언
number1 = 5; // 변수에 값을 할당한다.

let string = "가나다라마바사";
const string2 = "가가가";

// var let const
// var : 재선언 가능, 재할당 가능
// let : 재선언 불가능, 재할당은 가능
// const : 재선언 불가능, 재할당 불가능
        

/** 자료형을 알려주는 typeof */
const typeofFunc = () => {
    console.log(typeof "안녕");
    console.log(typeof 3);
    console.log(typeof null); // null => object 자료형
}

// typeofFunc();

/** promot */
const promotFunc = () => {
    let score1 = prompt("첫번째 선정을 입력하세요.");
    let score2 = prompt("두번째 선정을 입력하세요.");
    console.log(score1, score2);
    let avg = (Number(score1) + Number(score2)) / 2;
    console.log(avg)
}

// promotFunc();

/** String, toString 문자열로 형변한 & Number 숫자형으로 형변환 */
const transFunc = () => {
    let num = 5;
    console.log(String(num));
    console.log(num.toString());

    let string = "5";
    console.log(Number(string));
}
// transFunc();



