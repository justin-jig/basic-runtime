/** spread 연산자 */
const a = [1, 2, 3];
const b = [4, 5, 6];

// 기존 방식
const con = a.concat(b);

const c = [...a];
c[1] = 10;
console.log(a,b, con, c);


const Person = {
    name: 'justin',
    age : 29
}
console.log({...Person});
const d = 'Hello';
console.log([...d]);