// setTimeOut(code, deley) : deley동안 기다리다가 code를 실행

console.log(1);

setTimeout(() => {

    console.log(2);

},[2000])
console.log(3);

// 편의점에 들어가서 음료수를 사고 나오는 상황
function goMart() {
    console.log('마트에 가서 어떤 음료를 살지 고민한다.');
}

function pickDrink (callback) {
   
    setTimeout(() => {
        console.log('고민 끝');
        product = '제로 콜라';
        price = 2000;
        callback();
    },[3000])
}

function pay (product, price) {
    console.log(`상풍명: ${product}, 가격: ${price}`);
}

let product;
let price;
goMart();
pickDrink(pay(product, price));