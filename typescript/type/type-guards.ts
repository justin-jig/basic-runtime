// Type Guards Examples in TypeScript

// 1. typeof 연산자 기반 타입 가드
// 원시 타입(string, number, boolean 등)을 구분할 때 사용
function printValue(value: string | number) {
  if (typeof value === "string") {
    console.log(value.toUpperCase()); // value가 string으로 좁혀짐
  } else {
    console.log(value.toFixed(2)); // value가 number로 좁혀짐
  }
}

// 2. instanceof 기반 타입 가드
// 클래스나 생성자 함수를 이용한 인스턴스 구분에 사용
class Dog {
  bark() {
    console.log("멍멍");
  }
}
class Cat {
  meow() {
    console.log("야옹");
  }
}

function makeSound(animal: Dog | Cat) {
  if (animal instanceof Dog) animal.bark(); // Dog 인스턴스일 경우
  else animal.meow();                        // Cat 인스턴스일 경우
}

// 3. 'in' 연산자 기반 타입 가드
// 객체에 특정 속성이 존재하는지 검사하여 타입을 좁힘
interface Admin {
  role: "admin";
  permission: string[];
}
interface Guest {
  role: "guest";
  access: boolean;
}

function getAccess(user: Admin | Guest) {
  if ("permission" in user) {
    // permission 속성이 있으면 Admin 타입으로 좁혀짐
    return `관리자 권한: ${user.permission.join(",")}`;
  }
  // Guest 타입으로 좁혀짐
  return user.access ? "게스트 접근 허용" : "접근 제한";
}

// 4. 사용자 정의 타입 가드 (User-Defined Type Guard)
// 반환 타입을 person is SuperAdmin 형태로 지정하면
// 조건문 내에서 해당 타입으로 좁혀짐
interface User {
  role: "user";
  name: string;
}
interface SuperAdmin {
  role: "admin";
  level: number;
}

function isSuperAdmin(person: User | SuperAdmin): person is SuperAdmin {
  return (person as SuperAdmin).level !== undefined; // level 속성이 존재하는지 확인
}

function printRole(person: User | SuperAdmin) {
  if (isSuperAdmin(person)) {
    console.log(`관리자 레벨: ${person.level}`); // SuperAdmin 타입
  } else {
    console.log(`일반 사용자: ${person.name}`);   // User 타입
  }
}

// 5. 제어 흐름 기반 타입 좁히기 (Control Flow Narrowing)
// null, undefined 등을 조건문으로 걸러 타입을 좁힘
function example(x: string | null) {
  if (!x) return;                // null 체크 후 제거
  console.log(x.toUpperCase());  // x는 string으로 추론됨
}

// 6. Discriminated Union (태그 기반 타입 구분)
// 공통된 속성(kind 등)을 기준으로 타입을 자동으로 좁힘
interface Circle {
  kind: "circle";
  radius: number;
}
interface Rectangle {
  kind: "rectangle";
  width: number;
  height: number;
}
type Shape = Circle | Rectangle;

function getArea(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;       // Circle 타입으로 좁혀짐
    case "rectangle":
      return shape.width * shape.height;        // Rectangle 타입으로 좁혀짐
    default:
      return exhaustiveCheck(shape);            // 모든 분기를 처리했는지 검사
  }
}

// 7. 논리 연산 기반 타입 가드
// &&, ||, ?. 등을 활용한 간단한 타입 필터링
function printLength(value?: string | null) {
  if (value && value.length > 0) {
    console.log(`길이: ${value.length}`); // value가 string으로 좁혀짐
  } else {
    console.log("빈 값");
  }
}

// 8. never 타입 (Exhaustive Check)
// switch-case 등에서 모든 경우를 처리했는지 검증할 때 사용
function exhaustiveCheck(param: never): never {
  throw new Error(`Unhandled case: ${param}`);
}

// 테스트 실행 예시
printValue("hello");                                       // typeof 기반
makeSound(new Dog());                                      // instanceof 기반
console.log(getAccess({ role: "admin", permission: ["read", "write"] })); // 'in' 기반
printRole({ role: "admin", level: 5 });                    // 사용자 정의 가드
printLength("typescript");                                 // 논리 연산 기반
console.log(getArea({ kind: "circle", radius: 5 }));       // Discriminated Union
