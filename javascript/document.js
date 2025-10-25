/** document 객체 (document object model) 
 * HTML 문서 요소의 집합
 * 
*/


/* *요소 선택 element selector */
const documentObjectModel  = () => {

    const getRedEl = document.getElementById("red");  // 무조건 하나만 선택 
    const getBoxesEl = document.getElementsByClassName("box");  // 다중 선택
    const getTagEl = document.getElementsByTagName('div'); // 다중 선택
    const passwordInput = document.getElementsByName('password');
    const boxesBySelector = document.querySelector(".box"); // 무조건 하나만 선택
    const boxesByAllSelector = document.querySelectorAll('.box'); // 모든 .box elemet 선택 
    const orange = document.querySelectorAll('#orange');


    console.log(getRedEl);
    console.log(getBoxesEl);
    console.log(getTagEl);
    console.log(passwordInput);
    console.log(boxesBySelector);
    console.log(boxesByAllSelector);
    console.log(orange);
}

//documentObjectModel();

/** 요소 다루기 */
const documentObjectModelAction = () => {

    /** wirte, innerText, innerHTML, textContent */
    document.write('안녕'); // body 태그 맨 아래 생김
    let redBox = document.getElementById('red');
    console.log(redBox.innerText); //텍스트 가져오기
    console.log(redBox.innerHTML); // html 가져오기
    console.log(redBox.textContent); // 요소 안 텍스트 가져오기
    redBox.innerText = "안녕하세요"; //요소안에 텍스트 가져오기
    redBox.innerHTML= redBox.innerText +  "<p>빨간상자</p>"; //요소안에 텍스트 가져오기
    redBox.textContent = '빨간상자';
}

const documentObjectModelAction2 = () => {

    /** className, classList (contains, toggle) */
    let redBox = document.getElementById('red');
    // redBox.className = "box yellow";
    console.log(redBox.classList); // 클래스 가져오기
    //redBox.remove(); // 괄호 안에 들어온 값을 클래스 리스트 안에 삭제
    //redBox.add() // 괄호 안에 들어온 값을 클래스 리스트 안에 추가
    //redBox.classList.contains() // 괄호 안에 들어온 값이 클래스에 존재하는 지 검사
}   //redBox.classList.toggle() // 괄호 안에 들어온 값을 자동으로 추가하거나 삭제함.

const documentObjectModelAction3 = () => {

    /** setAttribute  */
    let redBox = document.getElementById('red');
    redBox.setAttribute('name', 'box'); // 속성을 변경할 때 사용

}

const documentObjectModelAction4 = () => {

    /** children, createElement, appand, appandChild */
    
    // children (parentNode, nextElementSibling, previosElementSibling)
    let container = document.querySelector('.container');
    console.log(container.children); // children 출력
    console.log(container.children[container.children.length - 1]); 

    let redBox = document.getElementById('red');
    console.log(redBox.parentNode); // 상위 요소 부모출력
    console.log(redBox.nextElementSibling); // 요소에 다음 형제 출력

    let orangeBox = document.getElementById('orange');
    console.log(orangeBox.previousElementSibling); // 요소에 이전 형제 출력
    
    /** createElement */
    let createbox = document.createElement('div');
    createbox.className = "box green";

    // appand = 매개변수로 문자열과 노드객체를 모두 받을 수 있다.
    // appndChild = 매개변수로 노드객체만 받을 수 있다.
    // prepend = 첫번쨰 자식으로 괄호 안에 요소를 추가한다.
    // before
    // after
    // remove
    // removeChild

}

// documentObjectModelAction();
// documentObjectModelAction2();
// documentObjectModelAction3();
documentObjectModelAction4();