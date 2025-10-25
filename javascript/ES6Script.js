

/**
   0. class
    let justin = class {} //class 표현식
 */
// class 선언식
class justin {

    constructor(postion){
        /*
         유의할점
         1.class는 hoisting 영향을 받지 않음. class를 먼저 선언해야한다.
         2.class란 단순히 Syntax적인 표현일 뿐
        */
        console.log(postion);
    }


    ECMAScript(){
        /**
         1.let const 
        */
        var GrobalVariable = undefined; // 전역변수  mutability
        if(ES6){
            let LocalVariable = null; // 지역변수 : BLOCK SCOPE , mutability
            const blockConstant = 0; // 상수변수 : BLOCK SCOPE, Immutability
        }
        /**
         2.Default Parameter , Rest Parameter
        */
        //Default Parameter
        function dfaultParameter(GrobalVariable){ }
        if(ES6){
            function dfaultParameter( es6 = true){ }
        }
        //Rest Parameter
        function foo(...rest){
            /**
             - ex : parameter (1,2,3,4,5)
             - 주의할점 : Rest parameter는 항상 제일 마지막 parameter로 있어야 한다.
            */
            console.log(Array.isArray(rest)) //true
        }   

        /**
         3. Spread Operator
            iterable : Array,String,Map,Set ,Dom 구조이며 iterator를 생성해서, next()로
            순회할 수 잇는 자료구조가 이터러블이라고 생각하면 된다.
         */
         var arr = [1,2,3];
         var o1 ={x:1, y:2};
         var o2 = {z:3};
         console.log(arr.concat([4,5,6]), object.assign(o1,o2));
         if(ES6){
            // 객체 복제로 인해 Immutability 할수 있음
            let arr = [1,2,3];
            let o1 ={x:1, y:2};
            let o2 = {...o1,z:3};
            console.log([...arr,4,5], o2);
         }

         /**
           4.Arrow Function ( lamda )
         */
        function ES5function(){return;}
        // 1. 항상 익명이다. 2. 메소드 함수가 아닌 곳에서 적합 3.자기 자신 바인딩(This) X
        const ES6function = () =>{}

        /**
          5. Template String (``) 
         */
         var name = 'justin'
         console.log('my name' + name);
         if(ES6){
             const name = 'justin'
             console.log(`my name ${name}`)
        }

        /**
          7. generator( yield || next(), symbol.for() )
           * yaield와 next()를 통해 사용자 요구에 따라 일시적으로 정지 할 수 있다.
         */
            // yield next()
            function* generatorFunction(){
                yield console.log(1);
                yield console.log(2);
                yield console.log(3);
            }
            let iteratort = generatorFunction()
            iteratort.next(); //1
            iteratort.next(); //2
            iteratort.next(); //3
            
        
        /**
            8. 구조할당 destructuring
            *배열이나 객체의 데이터를 해체하여 다른 변수로 추ㅜㄹ할 수 있다.
        */    

    }

}


const callClass = new justin('Front-End'); // 생성자
callClass.ECMAScript(); // 내부 함수 호출

/** module, module loder */
export default justin;
//import justin '경로'
//import {justin} '경로'


/** objcet,array 관련 추가된 기능  */
//reflect

/**map,set */

/** promises */

