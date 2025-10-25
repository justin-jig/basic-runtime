 //class
 class Cat {
    //생성자
    constructor(name, age) {
        //속성
        this.name = name;
        this.age = age;
    }
    //메소드
    mew() {
        console.log('야옹');
    }
    eat() {
        console.log('먹이를 먹습니다');
    }
}
const cat1 = new Cat('나비', 1);
const cat2 = new Cat('냥이', 2);
cat1.mew();
cat1.eat();
cat2.mew();