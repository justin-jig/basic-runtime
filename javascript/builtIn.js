
/* 문자 관련 메소드 **/

const stringMethod = () => {

    let str = "happy day~!";
    let strLength = str.length; // 문자 길이
    let strUpper = str.toUpperCase(); // 대문자로 변경
    let strLower = str.toLowerCase(); // 소문자로 변경
    let strIndexOf = str.indexOf('p'); // 문자에 포함되어 있는지 탐색  
    let strSlice = str.slice(); // slice('시작 인덱스', '끝 인덱스'); 문자 자르기 
    let strReplace = str.replace('p', 'a'); // replace('대체될 문자', '대체할 문자') 문자 하나를 찾아서 대체해줌 
    let strReplaceAll = str.replaceAll('p', 'a'); // replaceAll('대체될 문자', '대체할 문자') 문자를 다 찾아서 대체해줌 
    let strRepeat = str.repeat(2); // 문자를 반복해서 출력
    let strTrim = str.trim(); // 문자 공백 제거
    let strSplit = str.split('a'); // 문자 자르기 => 배열로 출력    
}

// stringMethod();

const methodChaining = () => {

    let hello = "Hello";
    let helloRvs = hello.split("").reverse().join();
    let helloRvs2 = hello.split("").reverse().join('/');
    console.log(helloRvs);
    console.log(helloRvs2);
}

// methodChaining();

/** Date 객체 (표준 객체) */
const dateObject = () => {

    let date = new Date();
    date.getFullYear(); // 년도를 출력
    date.getMonth() + 1 ; // 월 출력 (-1 해서 출력됨)
    date.getDate(); // 날을 출력
    date.getDay(); // 요일 출력 (1.2.3.4.5.6) 0은 일요일
    date.getTime(); // 1970년 1월 1일 00시 00분 00초 UTC를 기준 시간을 출력
   
    /** 시간 비교 */
    let expired = new Date('2023-06-07');
    console.log(date.getTime() >= expired.getTime());
    let nowget = `${date.getFullYear()} - ${(date.getMonth() + 1) >= 10 ? (date.getMonth() + 1) : '0' + (date.getMonth() + 1) } - ${date.getDate() >= 10 ? date.getDate() : '0' + date.getDate()}`
    console.log(nowget)
}

// dateObject();

/** Math 객체 (표준 객체) */
const mathObject = () => {

    let math1 = Math.PI; // 파이
    let math2 = Math.E; // 자연수
    let math3 = Math.min(2,5,8); // 가장 작은 값 출력
    let math4 = Math.max(2,5,8); // 가장 큰 값 출력
    let math5 = Math.random(); // 랜덤 수 출력
    let math6 = Math.round(7.2); // 반 올림 
    let math7 = Math.floor(7.2); // 무조건 내림
    let math8 = Math.ceil(7.2); // 소수점 무조건 올림

    /** 정수 랜덤값 
     * (Math.random() * (최댓값 - 최솟값) + 최솟값)
     * 
    */
    let math9 = Math.floor((Math.random() * (100 - 1) + 1));

}

// mathObject();







