// Type Transformation & Mapped Types

interface User {
  id: number;
  name: string;
  active: boolean;
}

// 1) 매핑 기본: 기존 타입의 모든 키를 순회하며 속성 변형
type OptionalUser = { [K in keyof User]?: User[K] }; // 모든 속성 optional 처리

// 2) 응용: readonly / nullable 변형
type ReadonlyUser = { readonly [K in keyof User]: User[K] };      // 모든 속성 읽기 전용
type NullableUser = { [K in keyof User]: User[K] | null };        // 모든 속성 null 허용

// 3) Key Remapping: 키 이름을 변환(접두사 등)
type PrefixKeys<T> = { [K in keyof T as `app_${string & K}`]: T[K] }; // 키를 `app_` 접두사로 재작성
type PrefixedUser = PrefixKeys<User>; // { app_id: number; app_name: string; app_active: boolean }

// 4) 조건부 타입 + 분배 조건부: 유니언의 각 구성 요소에 조건 적용
type ExcludeNull<T> = T extends null | undefined ? never : T; // null/undefined 제거
type Clean = ExcludeNull<string | number | null>; // string | number

// 5) infer: 조건부 타입 내부에서 타입 변수 추론
type ReturnTypeOf<T> = T extends (...args: any[]) => infer R ? R : never; // 함수 반환 타입 추출
function getUser() { return { id: 1, name: "Ingeun" }; }
type UserReturn = ReturnTypeOf<typeof getUser>; // { id: number; name: string }

// 6) 조건부 키 필터링: 값의 타입 조건으로 키를 선택적으로 남김
type OnlyBoolean<T> = {
  [K in keyof T as T[K] extends boolean ? K : never]: T[K]
};
interface Setting { darkMode: boolean; volume: number; beta: boolean; }
type BooleanOnly = OnlyBoolean<Setting>; // { darkMode: boolean; beta: boolean }

// 7) Nested 변환: 재귀적으로 깊은 구조까지 변환
type DeepReadonly<T> = {
  readonly [K in keyof T]:
    T[K] extends object ? DeepReadonly<T[K]> : T[K]
};
interface Project { id: number; info: { title: string; owner: string } }
type ImmutableProject = DeepReadonly<Project>; // 내부 객체까지 모두 readonly

// 8) DTO 변환: 특정 필드(createdAt/updatedAt)를 제거하여 전송용 타입 생성
interface Entity { id: number; createdAt: string; updatedAt: string }
type DTO<T> = {
  [K in keyof T as Exclude<K, "createdAt" | "updatedAt">]: T[K]
};
type UserDTO = DTO<Entity>; // { id: number }
