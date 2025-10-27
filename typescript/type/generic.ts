// Generics Examples in TypeScript

// 1. 기본 제네릭 함수
// 타입 매개변수 <T>를 받아 동일한 타입으로 반환하는 함수
function identity<T>(value: T): T {
  return value;
}
const num = identity<number>(42);                // number 타입 전달
const str = identity<string>("Hello TypeScript"); // string 타입 전달

// 2. 제네릭 함수 (다중 타입 매개변수)
// 서로 다른 타입 T, U를 받아 합쳐진 객체를 반환
function merge<T, U>(a: T, b: U): T & U {
  return { ...a, ...b };
}
const merged = merge({ name: "Ingeun" }, { age: 32 }); // { name: string; age: number }

// 3. 제네릭 인터페이스
// API 응답의 data 필드를 제네릭으로 선언
interface ApiResponse<T> {
  status: number;
  data: T;
}
const userResponse: ApiResponse<{ name: string; age: number }> = {
  status: 200,
  data: { name: "Ingeun", age: 32 },
};

// 4. 제네릭 클래스
// 스택(Stack) 자료구조: push/pop에 들어가는 타입을 제네릭으로 처리
class Stack<T> {
  private items: T[] = [];

  push(item: T) {
    this.items.push(item);
  }

  pop(): T | undefined {
    return this.items.pop();
  }
}

const numberStack = new Stack<number>(); // number 전용 스택
numberStack.push(10);
numberStack.push(20);
numberStack.pop(); // number 반환

// 5. 제네릭 제약 (Constraints)
// extends를 이용해 특정 속성을 가진 타입만 허용
function getLength<T extends { length: number }>(value: T): number {
  return value.length; // length 속성이 보장됨
}

getLength("Hello");   // 문자열 OK
getLength([1, 2, 3]); // 배열 OK
// getLength(100);    // Error: number에는 length 없음

// 6. 다중 타입 매개변수
// K와 V를 받아 [K, V] 형태의 튜플 반환
function mapPair<K, V>(key: K, value: V): [K, V] {
  return [key, value];
}
const entry = mapPair("id", 123); // [string, number]

// 7. 제네릭 타입 별칭
// 특정 타입에 null 또는 undefined를 허용하는 Nullable 유틸 타입
type Nullable<T> = T | null | undefined;
type StringOrNull = Nullable<string>; // string | null | undefined

// 8. 제네릭 기본값 (Default Type)
// 타입 매개변수를 생략하면 기본값으로 any 사용
interface SimpleResponse<T = any> {
  code: number;
  data: T;
}
const defaultResponse: SimpleResponse = { code: 200, data: "OK" };

// 9. React 제네릭 훅 (예시)
// boolean 전용 토글 훅, 제네릭으로 타입 확장 가능
/*
import React, { useState } from "react";

function useToggle<T extends boolean>(initial: T): [T, () => void] {
  const [state, setState] = useState<T>(initial);
  const toggle = () => setState((prev) => !prev as T);
  return [state, toggle];
}
const [isOpen, toggleOpen] = useToggle(false);
*/

// 10. 제네릭 유틸리티 패턴
// 전달받은 값을 { value: T } 형태로 감싸 반환
function wrapValue<T>(value: T): { value: T } {
  return { value };
}
const wrapped = wrapValue("hello"); // { value: "hello" }

console.log({
  num,
  str,
  merged,
  userResponse,
  numberStack,
  entry,
  defaultResponse,
});
