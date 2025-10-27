// Utility Types Examples — with detailed comments

// 기본 인터페이스 정의
interface User2 {
  id: number;       // 사용자 ID
  name: string;     // 사용자 이름
  email?: string;   // 이메일 (선택적 속성)
}

// 1. Partial<T> — 모든 속성을 선택적(optional)으로 바꾼다.
type PUser = Partial<User2>; // { id?: number; name?: string; email?: string }

// 2. Required<T> — 모든 속성을 필수(required)로 바꾼다.
type RUser = Required<User2>; // { id: number; name: string; email: string }

// 3. Readonly<T> — 모든 속성을 읽기 전용(readonly)으로 바꾼다.
type ROUser = Readonly<User2>; // { readonly id: number; readonly name: string; readonly email?: string }

// 4. Pick<T, K> — T에서 일부 속성만 "선택"하여 새 타입을 만든다.
type UserPreview = Pick<User2, "id" | "name">; // { id: number; name: string }

// 5. Omit<T, K> — T에서 특정 속성을 "제외"하여 새 타입을 만든다.
type UserWithoutEmail = Omit<User2, "email">; // { id: number; name: string }

// 6. Record<K, T> — 주어진 key 집합(K)에 대해 value 타입(T)을 할당한 객체 타입을 만든다.
type Role2 = "admin" | "user" | "guest";         // 역할(role) 문자열 리터럴 집합
type RoleAccess = Record<Role2, boolean>;        // { admin: boolean; user: boolean; guest: boolean }

// 7. Exclude<T, U> — T에서 U 타입을 제외한다.
type Status = "success" | "error" | "loading";   // 상태 타입
type FinalStatus = Exclude<Status, "loading">;   // "success" | "error"

// 8. Extract<T, U> — T 중에서 U 타입만 추출한다.
type OnlyString = Extract<string | number | boolean, string>; // string

// 9. ReturnType<T> — 함수의 반환(return) 타입을 추출한다.
function getUser() {
  return { id: 1, name: "Ingeun" }; // 반환 타입: { id: number; name: string }
}
type UserReturn = ReturnType<typeof getUser>; // { id: number; name: string }

// 10. Parameters<T> — 함수의 매개변수(parameter) 타입을 튜플(tuple) 형태로 추출한다.
function sum(a: number, b: number) { return a + b; } // (a,b): number → number
type SumParams = Parameters<typeof sum>; // [number, number]

// 11. NonNullable<T> — null과 undefined를 제거한 타입을 만든다.
type Value = string | null | undefined;
type DefinedValue = NonNullable<Value>; // string

// 12. Custom Utility — DeepReadonly<T>
// 재귀적으로 모든 속성을 readonly 처리 (객체 내부까지 변경 불가)
type DeepReadonly<T> = { readonly [K in keyof T]: DeepReadonly<T[K]> };

// (Optional) Nullable<T> — 모든 속성을 null 허용으로 바꾸는 유틸
// type Nullable<T> = { [K in keyof T]: T[K] | null };

// 13. Record 타입 사용 예시
const access: RoleAccess = { admin: true, user: true, guest: false }; // 역할별 접근권한 테이블

// 14. Pick / Omit 타입 객체 생성
const preview: UserPreview = { id: 1, name: "Ingeun" }; // 일부 필드만 포함
const dto: UserWithoutEmail = { id: 2, name: "Kim" };   // email 제외

// 15. 콘솔 출력 — 모든 결과 확인
console.log({ access, preview, dto });

/*
출력 예시:
{
  access: { admin: true, user: true, guest: false },
  preview: { id: 1, name: "Ingeun" },
  dto: { id: 2, name: "Kim" }
}
*/
