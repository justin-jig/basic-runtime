

<h5 align="left">React </h5>
<p align="left">
  <span>노트 정리 : <a href="https://justin-jig.github.io/justin-book/runtime">https://justin-jig.github.io/justin-book/runtime</a></span><br/>
</p>

## React 주요 변경사항 정리 

#### basic-types 요약 표

| 구분 | 타입명 | 설명 |
|------|--------|------|
| 기본 | `string`, `number`, `boolean` | 문자열, 숫자, 불리언 값 |
| 배열 | `string[]`, `Array<number>` | 동일한 타입의 집합 |
| 튜플 | `[string, number]` | 고정된 길이의 타입 집합 |
| 특수 | `void`, `never`, `unknown`, `null`, `undefined` | 반환 없음 / 도달 불가 / 미확정 타입 |
| 리터럴 | `"ON" | "OFF"`, `1 | 0`, `'admin' | 'user'` | 값 자체를 타입으로 제한 |
| 열거형 | `enum Role { ADMIN, USER, GUEST }` | 명시적 상수 집합 |
| 객체형 | `{ name: string; age: number }` | 구조 기반 타입 |
| 기타 | `symbol`, `bigint` | 고유 식별자 및 대규모 정수 |

---

#### generics 요약 표

| 구분 | 항목 | 설명 |
|------|------|------|
| 1 | `function identity<T>(value: T): T` | 기본 제네릭 함수 |
| 2 | `merge<T, U>(a: T, b: U): T & U` | 다중 제네릭 함수 |
| 3 | `interface ApiResponse<T>` | 제네릭 인터페이스 |
| 4 | `class Stack<T>` | 제네릭 클래스 |
| 5 | `T extends {...}` | 제네릭 제약 (Constraints) |
| 6 | `<K, V>` | 다중 타입 매개변수 |
| 7 | `type Nullable<T>` | 제네릭 타입 별칭 |
| 8 | `interface Response<T = any>` | 제네릭 기본값 (Default) |
| 9 | `useState<T>()`, `useToggle<T>()` | React 제네릭 훅 |
| 10 | `wrapValue<T>()` | 제네릭 유틸리티 패턴 |

---
#### type-guards 요약 표

| 구분 | 타입 가드 종류 | 설명 |
|------|----------------|------|
| 1 | `typeof` | 기본 타입 구분 (string, number 등) |
| 2 | `instanceof` | 클래스 인스턴스 판별 |
| 3 | `'in'` | 속성 존재 여부 기반 판별 |
| 4 | 사용자 정의 타입 가드 | `value is Type` 형태의 함수 |
| 5 | 제어 흐름 기반 좁히기 | Control Flow Narrowing |
| 6 | Discriminated Union | 공통 속성(kind 등)을 통한 자동 분기 |
| 7 | 논리 연산 기반 | `&&`, `||`, `?.` 기반 타입 제거 |
| 8 | `never` | 불가능한 케이스 검사(Exhaustive Check) |

---

#### type-inference
| # | 주제 | 핵심 포인트 |
|---|-----|-------------|
| 1 | 초기값 기반 추론 | `let a = 1` → `number`, `const s = "OK"` → 리터럴 유지 |
| 2 | 함수 반환 타입 추론 | `return` 식을 따라 자동 결정 |
| 3 | 컨텍스트 기반 추론 | DOM/콜백/JSX 문맥으로 매개변수 타입 추론 |
| 4 | 제네릭 추론 | 인수 타입으로 타입 매개변수(`T`) 유추 |
| 5 | 기본값과 추론 | 기본값 타입으로 파라미터 타입 추론 |
| 6 | 제어 흐름 기반 좁히기 | `typeof` / 분기문을 따라 타입 축소 |
| 7 | 공통 타입(best common type) | 혼합 배열의 상위 공통 타입 산출 |
| 8 | `noImplicitAny` | 암시적 `any` 차단으로 안전성 강화 |
| 9 | 추론 vs 명시 | 공용 API는 명시, 내부 로직은 추론 균형 |

---

#### utility-types

- `Partial<T>` / `Required<T>` / `Readonly<T>`
- `Pick<T, K>` / `Omit<T, K>`
- `Record<K, T>`
- `Exclude<T, U>` / `Extract<T, U>`
- `ReturnType<T>` / `Parameters<T>`
- `NonNullable<T>`
- 커스텀: `DeepReadonly<T>`, `Nullable<T>`


#### Type-Safe Interoperability
- `unknown`으로 시작하는 입력 처리 + 타입 가드
- JSON 파싱: `zod`로 런타임 검증 + `z.infer`
- `ApiResponse<T>` 응답 모델
- 외부 SDK 보강: `declare module`
- 환경 변수 타입화 (`ProcessEnv`)
- 브라우저 전역 확장 (`declare global`)
- 타입 안전 `fetch` 래퍼
- 점진적 JS→TS 마이그레이션 단계


#### type-transformation
- 매핑 기본: `keyof` + `in` + `T[K]`
- Readonly/Nullable/Optional 변형
- Key Remapping(`as`) 및 접두사/변환
- 조건부 타입·분배 조건부 타입
- `infer` 로 반환/요소 타입 추출
- 조건부 키 필터링
- Nested(재귀) 변환
- DTO 변환 예시

#### template-literal-types
- 기본 조합: `${Type}` / `${A}${B}`
- 대소문자 변환: `Uppercase` / `Lowercase` / `Capitalize` / `Uncapitalize`
- 유니언 문자열 패턴 생성
- 조건부 조합 + 제네릭
- Mapped Type과 결합해 키 자동 생성


# Advanced Type Patterns
- Conditional Types / Distributive Conditional
- `infer` 기반 타입 추출 (함수/Promise/Array)
- Mapped Constraints (`as`, `keyof`, `Extract`/`Exclude`)
- Variance(공변/반공변/불변/이변)
- Template Literal Types 결합
- DeepReadonly / Mutable 재귀 매핑
- 이벤트 핸들러 타입 자동 생성
