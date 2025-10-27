// 기본 타입 예시

// 문자열, 숫자, 불리언 타입 선언
let username: string = "Ingeun";   // 문자열(string)
let age: number = 32;              // 숫자(number)
let isAdmin: boolean = true;       // 불리언(boolean)

// 타입 추론 (Inference): 초기값을 기준으로 타입을 자동 결정
let score = 100;       // number로 추론됨
let message = "Welcome!"; // string으로 추론됨

// 배열 (Array)
let fruits: string[] = ["apple", "banana", "cherry"]; // 문자열 배열
let scores: Array<number> = [98, 87, 92];             // 숫자 배열 (제네릭 문법)

// 튜플 (Tuple): 요소의 개수와 타입이 고정된 배열
let user: [string, number] = ["Ingeun", 32];
const [yourname, years] = user; // 구조 분해 할당

// null, undefined 타입
let n: null = null;
let u: undefined = undefined;

// void: 반환값이 없는 함수
function logMessage(msg: string): void {
  console.log(msg);
}

// never: 결코 반환되지 않는 함수 (예: 오류 발생, 무한루프)
function throwError(errorMsg: string): never {
  throw new Error(errorMsg);
}

// unknown: 타입이 미정인 값. 사용 전 타입 검증이 필요함
function processValue(value: unknown) {
  if (typeof value === "string") console.log(value.toUpperCase()); // 타입 가드
}

// 리터럴 타입: 특정 값만 허용하는 타입
type Direction = "up" | "down" | "left" | "right";
let move: Direction = "up"; // 지정된 값 중 하나만 가능

// enum: 열거형 (상수 집합)
enum Role {
  ADMIN = "ADMIN",
  USER = "USER",
  GUEST = "GUEST",
}
const currentRole: Role = Role.ADMIN; // Role 열거형 중 ADMIN 값

// 타입 단언 (Type Assertion): 개발자가 직접 타입을 명시
let value: unknown = "typescript";
let stringLength = (value as string).length; // string으로 단언 후 length 접근

// symbol: 고유한 식별자를 만드는 타입
// bigint: 매우 큰 정수를 표현하는 타입
const sym = Symbol("id");
const big: bigint = 9007199254740991n;

// 콘솔 출력 예시
console.log({
  username,
  age,
  isAdmin,
  score,
  fruits,
  user,
  currentRole,
  stringLength,
  sym,
  big,
});

/*
출력 예시:
{
  username: 'Ingeun',
  age: 32,
  isAdmin: true,
  score: 100,
  fruits: [ 'apple', 'banana', 'cherry' ],
  user: [ 'Ingeun', 32 ],
  currentRole: 'ADMIN',
  stringLength: 10,
  sym: Symbol(id),
  big: 9007199254740991n
}
*/
