
/**
 * jquery
    자바스립트 언어를 간편하게 사용할 수 있도록 단순화
    시킨 오픈 소스 기반의 자바스크립트 라이브러리
 */


/** $(선택자).동작함수 */

const submitt = () => {
    let valueJquery = $('#id').val();
    let valueJs = document.getElementById("id").value;
    console.log(valueJquery, valueJs);
}
//** value 값 넣기 */
const jqueryval = () => {
    // document.getElementById("id").value = 'aaa';
    $('#id').val("aaa");
}
//jqueryval();

/** style 변경 */
const jqueryStyle = () => {
    $('div').css('background-color', 'blue');
    $('div').css('border-radius', '20px');
} 
// jqueryStyle();

/** 속성 변경 */
const jqueryAttr = () => {
    $('input').attr('placeholder', '아이디를 입력하세요.');
} 
// jqueryAttr();

/** 텍스트 변경 */
const jqueryText = () => {
    $('div').text('안녕?');
} 
// jqueryText();

/** html 변경 (innerhtml) */
const jqueryhtml = () => {
    $('div').html('<p>Hi</p>');
} 
// jqueryhtml();

/** 요소 조작 */
const jqueryElement = () => {
    /** 요소 추가 */
    $('div').append('<span>안녕</span>'); // 선택된 요소의 자식 요소 중 마지막으로 추가
    $('div').prepend('<p>안녕</p>'); // 선택된 요소의 자식 요소 중 첫번째로 추가
    $('div').before('<h2>안녕</h2>'); // 선택된 요소의 형제 요소로 이전 형제로 추가
    $('div').after('<h3>안녕</h3>'); // 선택된 요소의 형제 요소로 다음 형제로 추가
    /** 요소 삭제 */
    $('div > span').remove(); //선택한 요소를 DOM 트리에서 삭제. 선택자 조건을 만족하는 요소만 삭제
    $('div').empty(); // 선택한 요소의 자식 요소를 모두 삭제

    /** 요소 탐색 */
     $('div').parent(); //바로 위에 존재하는 하나의 부모 요소 선택
     $('div').parents(); // 바로 위 부모뿐만 아니라 부모의 부모, 모든 조상을 선택
     $('div').next(); // 선택된 요소 바로 다음에 위치한 형제 요소 선택
     $('div').nextAll(); // 선택된 요소 다음에 위치한 형제 요소 모두 선택
     $('div').prev(); // 선택된 요소 바로 이전에 위치한 형제 요소 선택
     $('div').prevAll(); // 선택된 요소 바로 이전에 위치한 형제 요소 모두 선택
     // $('div').prevAll('선택자')
     $('div').children();// 선택된 요소의 자식 요소 모두 선택
}   
// jqueryElement();

/** class 조작 */
const jqueryClass = () => {

    // $('div').addClass('box'); // 선택된 요소에 클래스 추가
    //$('div').removeClass(''); // 선택된 요소에 클래스 삭제
    $('div').hasClass('box'); // 선택된 요소에 클래스가 있는지 여부 확인 true & false
    // $('div').toggleClass('box'); // 선택된 요소에 클래스가 있으면 추가, 없으면 삭제
}
//jqueryClass();

/** 이벤트 리스너 */
const jqueryEventListenr = () => {
    
    /** 로딩 이벤트 ready, $() */
    
    $(window).ready(function(){ // 페이지 로드 후에 실행하는 함수

    }); 
    $(function(){

    })

    /** mouse Event */
    // $().on("click", function(){ })
    // $().on("mouseover", function(){ })
    // $().on("mouseout", function(){ })
    // $().on("mouseup", function(){ })
    // $().on("mousedown", function(){ })
    $('.btn2').click(function(){ // 클릭
        alert('클릭');
    })
    $('.btn2').mouseover(function(){ // 마우스 over 마우스 올라가는 순간 1번

    })
    $('.btn2').hover(function(){ // 마우스 over 마우스 올라가 있는 동안
    })

    $('.container').scroll(function(){ // 스크롤 이벤트
        console.log('scroll')
    })


    $('input').keydown(function(e){ // keydown 키를 누르는 순간에만 발생
        console.log(e.key === 'Enter');
    })

    $('input').keyup(function(e){ // keyup 키를 눌렀다가 떼는 순간
        console.log(e.key === 'Enter');
    })

    $('input').keyup((e) => {

    })
}

jqueryEventListenr();











