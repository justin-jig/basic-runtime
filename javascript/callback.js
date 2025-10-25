

//콜백함수 : 함수 타입 파라미터 맨 마지막에 하나 더 선언
function mainFunc(param1,param2, callback) {

    console.log(param1, param2);
    callback();
}

function callbackFunc (param) {

    console.log('콜백 함수입니다.');
}

mainFunc(1,2,callbackFunc);