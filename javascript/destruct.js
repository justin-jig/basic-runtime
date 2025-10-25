
/** 배열 구조분해 */
const list = ['apple', 'grape'];
console.log(list[0], list[1]);
[item1, item2 = 'peach'] = list;
console.log(item1, item2);
item1 = 'peach';

console.log(item1, item2);
// 교환
let x = 1, y = 3;
[x, y] = [y,x]


/** 객체 구조분해 */
const Person = {
    name : 'justin',
    age : 19,
    gender : 'M',
    friends : ['Alex', 'Kevin'],
    hello : function() {
        console.log('hello');
    },
    'kdt-9' : 'codingOn KTD 9기'
}
console.log(Person.name);
Person.age = 29;
console.log(Person.age);
console.log(Person['kdt-9']);
Person.city = 'seoul';
console.log(Person);

const {name,age,gender,friends, key='hi', age:myAge} = Person;
console.log(key)
console.log(myAge);