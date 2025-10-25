/**
 * for 문
 * 
 *  continue : 해당 index 반복문에서 continue를 만나면 다음 증감문으로 넘어간다.
 *  break : 반복문 멈추고 실행 종료;
*/

const forLoop = () => {
    for ( let i; i < 10; i++ ) {
        console.log('안녕');
    }
    
    let fruits = ["apple", "banana", "orange", "grape"];
    for ( let i; i < fruits.length; i++ ) {
        console.log(fruits[i]);
        // continue
        // break
    }
    
    let number = 5;
    let rtn = 0;
    
    for ( let i = 1; i <= number; i++ ) {
        rtn +=i;
    }
    console.log(rtn);
}

/** 이중 for문 */
const nestedForLoop = () => {

    for (let i=1; i<5; i++) {
        for(let j=0; j<5; j++) {
            console.log(i,j)
        }
    }
}

// forLoop();
// nestedForLoop();


/** while 문 
 * 
 *  반복횟수를 특별히 지정할 수 없을 떄 사용함.
 * 
 *  while(조건) {
 *  
 *  }
 * 
*/

const whileLoop = () => {

    let fruits = ["apple", "banana", "orange", "grape"];
    let index = 0;
    while (index < fruits.length) {

        console.log(fruits[index]);
        index ++;
    }

    /**
    let num = NaN;
    while (isNaN(num)) {
        num = Number(prompt("숫자를 입력해주세요."));
    }

    */

    let number = 5;
    while(true) {
        number = Number(prompt("10 이상의 숫자를 입력하세요~~~"))
        if (number >= 10) {
            break;
        }
    }

}

const doWhileLoop = () => {

    // do에 있는 스크립트를 먼저 실행 
    let index = 0;
    do {
        console.log(index);
        index ++
    } while (index < 10)

}

// doWhileLoop();
// whileLoop();


/** continue */
const continueLoop = () => {

    let fruits = ["apple", "banana", "orange", "grape"]
    for(let i=0; i < fruits.length; i++) {
        if(fruits[i] == "banana") {
            continue
        }
        console.log(fruits[i]);
    }

    let index = -1;
    while(index < fruits.length-1){
        index++;
        if(fruits[index] == "banana") {
            continue
        }
        console.log(fruits[index]);
    }
}

//continueLoop();

/** for of */
const forOfLoop = () => {
    let fruits = ["apple", "banana", "orange", "grape"]
    for (let fruit of fruits) {
        console.log(fruit);
    }
}

/** for in */
const forInLoop = () => {
    let fruits = ["apple", "banana", "orange", "grape"];
    for (let fruit in fruits) {
        console.log(fruit);
    }
}
// forInLoop();
// forOfLoop();

/** forEach */
const forEachLoop = () => {
    
    let fruits = ["apple", "banana", "orange", "grape"];

    fruits.forEach(function(data, index, arr){
        console.log("data :", data);
        console.log("index :", index);
        console.log("arr :", arr);
    })

    fruits.forEach((data, index, arr) => {
        console.log("data :", data);
        console.log("index :", index);
        console.log("arr :", arr);
    })
}
