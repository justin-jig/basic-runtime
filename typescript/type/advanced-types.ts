// Advanced Type Patterns

// 1) Conditional Types
type IsString<T> = T extends string ? true : false;
type A = IsString<"Hello">; // true
type B = IsString<number>;  // false

// 2) Distributive Conditional
type NonNull<T> = T extends null | undefined ? never : T;
type Clean = NonNull<string | null | number>; // string | number

// 3) infer — 함수 반환, Promise, Array
type Return<T> = T extends (...args: any[]) => infer R ? R : never;
function getUser() { return { id: 1, name: "Ingeun" }; }
type User = Return<typeof getUser>;

type Awaited<T> = T extends Promise<infer R> ? R : T;
type Elem<T> = T extends (infer U)[] ? U : never;

type A1 = Awaited<Promise<number>>; // number
type E1 = Elem<string[]>; // string

// 4) Mapped Constraints + as
type OnlyStringProps<T> = {
  [K in keyof T as T[K] extends string ? K : never]: T[K];
};
interface U { id: number; name: string; email: string; active: boolean; }
type UStrings = OnlyStringProps<U>; // { name: string; email: string }

// 5) Template Literal 결합
type EventName<T extends string> = `${T}_event`;
type ClickEv = EventName<"click">;

// 6) Variance (간단 시연)
type Fn<T> = (arg: T) => void;
let fnNumber: Fn<number> = (x) => void x;
let fnAny: Fn<any> = (x) => void x;
// fnAny를 fnNumber에 대입 가능(반공변 규칙에 유의: 입력은 더 넓은 타입 허용이 안전)

// 7) 깊은 변환
type Mutable<T> = {
  -readonly [K in keyof T]: T[K] extends object ? Mutable<T[K]> : T[K];
};
type DeepReadonly<T> = {
  readonly [K in keyof T]: T[K] extends object ? DeepReadonly<T[K]> : T[K];
};

interface Config { readonly env: { readonly mode: string } }
type M = Mutable<Config>;
type R = DeepReadonly<Config>;

// 8) Event 핸들러 자동 생성
type EventMap = {
  click: { x: number; y: number };
  scroll: { deltaY: number };
  keydown: { key: string };
};
type Handlers<T extends Record<string, any>> = {
  [K in keyof T as `on${Capitalize<string & K>}`]: (payload: T[K]) => void;
};
type H = Handlers<EventMap>;
