/**
 * event 함수
 * 
 */

/* 요소.addEventListener("click0", function(){ }) */
const addEventListenerFunc = () => {
    /** click, mouseover,mouseout,mouseup,mousedown */
    let button = document.querySelector('button');

    button.addEventListener('click', function(e) { // 클릭했을 때
        alert('click');
    })

    button.addEventListener('mouseover', function(e) { // 요소에 커서를 올렸을 때
        console.log('mouseover');
    })

    button.addEventListener('mouseout', function(e) { // 마우스가 요소를 벗어날 때
        console.log('mouseout');
    })

    button.addEventListener('mouseup', function(e) { // 마우스 버튼을 누르고 있는 상태
        console.log('mouseup');
    })

    button.addEventListener('mousedown', function(e) { //  마우스 버튼을 떼는 순간
        console.log('mousedown');
    })

}

const addEventListenerFunc2 = () => {
    
    /* focus,  blur */
    const querySelectorInput = () => { //queryselector로 처리

        let input = document.querySelector('input');
        input.addEventListener('focus', function(e) { // 포커스가 갔을 때
            e.target.style.backgroundColor = "black";
        })
        input.addEventListener('blur', function(e) { // 포커스 아웃 됐을 때
            e.target.style.backgroundColor = "transparent";
        })
    }

    const querySelectorAllInput = () => { //queryselectorAll로 처리

        let input = document.querySelectorAll('input');

        for ( let i=0; i<input.length; i++ ) {

            input[i].addEventListener('focus', function(e) {
                e.target.style.backgroundColor = "black";
            })

            input[i].addEventListener('blur', function(e) {
                e.target.style.backgroundColor = "transparent";
            })
        }
    }
    const onChange = () => { // Change : 폼 필드의 상태가 변경 되었을 때

        let input = document.getElementById('pw');
        input.addEventListener('onchange', function(e){
            console.log(e.currentTarget.value);
        })
    }

    //querySelectorInput();
    querySelectorAllInput();
    onChange();
}

const addEventListenerFunc3 = () => {
    
    /* Keypress, Keypress, keyup */
    let input = document.getElementById('pw');
    // Keypress : 키를 누르는 순간 + 누르고 있는 동안 계속 발생 
    // Keydown : 키를 누르는 순간에만 발생
    // Keyup : 키를 눌렀다가 떼는 순간
    input.addEventListener("keyup", (e)=> {
        if(e.key === 'Enter') {
            alert('로그인');
        }
    })
}

const addEventListenerFunc4 = () => {
    
    /* load, resize, scroll, unload */
  
    // load : 웹페이지에 필요한 모든 파일(html, css, js 등)의 다운로드가 완료 되었을 때
    window.addEventListener("load", (e)=> {
        let box = document.querySelector('div');

        box.addEventListener('mouseover', function(e) {
            e.currentTarget.style.backgroundColor = "yellow";
            e.currentTarget.style.marginLeft = "50px";
        })
        box.addEventListener('mouseout', function(e) { // 마우스가 요소를 벗어날 때
            e.currentTarget.style.backgroundColor = "red";
            e.currentTarget.style.marginLeft = "0";
        })
        console.log('로드됨');
    })
    // resize :  브라우저 창의 크기가 변경 될 때
    window.addEventListener('resize', (e) => {
        // console.log(window.innerWidth);         
    })

     // scroll : 스크롤이 발생할 때
     window.addEventListener('scroll', (e) => {
        console.log(window.scrollY);         
    })

    // unload :  링크를 타고 이동하거나, 브라우저를 닫을 때
    window.addEventListener('unload', (e) => {
        console.log('닫힘');       
    })
}


// addEventListenerFunc();
// addEventListenerFunc2();
// addEventListenerFunc3();
addEventListenerFunc4();