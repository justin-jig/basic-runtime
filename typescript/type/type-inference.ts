// Type Inference Examples in TypeScript

// 1) 초기값 기반 추론
let count = 10;           // number
let message = "Hi";       // string
let isActive = true;      // boolean
const ok = "OK";          // "OK" (리터럴 타입 유지)
const flag = true;        // true (리터럴 타입 유지)

// 객체/배열
let user = { id: 1, name: "Ingeun" };       // { id: number; name: string }
let list = [0, 1, null];                    // (number | null)[]

// 2) 함수 반환 타입 추론
function add(a: number, b: number) {
  return a + b; // number
}
function greet(name: string) {
  return `Hello, ${name}`; // string
}
function logNoReturn(msg: string) {
  console.log(msg); // void
}

// 3) 컨텍스트 기반 추론 (contextual typing)
// DOM 예시: 아래 코드는 브라우저 환경에서 의미가 있습니다.
// window.onmousedown = (event) => {
//   console.log(event.button); // MouseEvent로 추론
// };

// 콜백 문맥
[1, 2, 3].map((v) => v * 2); // v: number로 추론

// 4) 제네릭 추론
function identity<T>(value: T): T {
  return value;
}
const i1 = identity("Hello"); // T=string
const i2 = identity(123);     // T=number

// 5) 기본값과 추론
function log(value = "Default") {
  // value: string으로 추론
  console.log(value.toUpperCase());
}
log();
log("Custom");

// 6) 제어 흐름 기반 좁히기
function toFixedIfNumber(x: string | number) {
  if (typeof x === "number") {
    return x.toFixed(2); // x: number
  }
  return x.toUpperCase(); // x: string
}

// 7) 공통 타입(best common type)
let mixed = [1, "hello", true]; // (number | string | boolean)[]

// 8) noImplicitAny 체크가 없다면 악취 코드가 생길 수 있음
// 아래 함수는 명시적 타입이 없을 때 any로 추론될 수 있음
// tsconfig에서 "noImplicitAny": true 설정을 권장
// function sum(a, b) {
//   return a + b;
// }

// 9) 추론 vs 명시 — 공용 API에는 명시적 타입을 권장
export interface ApiResult<T> {
  code: number;
  data: T;
}
export function fetchOk(): ApiResult<string> {
  return { code: 200, data: "OK" };
}

// 테스트 출력
console.log({
  count,
  message,
  isActive,
  ok,
  flag,
  user,
  list,
  add: add(1, 2),
  greet: greet("TS"),
  i1,
  i2,
  mixed,
  api: fetchOk(),
});