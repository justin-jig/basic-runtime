// Template Literal Types Examples

// 1) 기본
// 문자열 리터럴을 조합하여 새로운 문자열 타입을 생성
type Direction = "up" | "down";
type Action = `${Direction}_move`; // "up_move" | "down_move"

// 2) 조합 예
// 여러 유니언 타입을 결합해 가능한 모든 조합을 자동 생성
type Lang = "ko" | "en";
type Platform = "web" | "mobile";
type LocaleKey = `${Lang}_${Platform}`; // "ko_web" | "ko_mobile" | "en_web" | "en_mobile"

// 3) 변환 유틸
// 문자열 리터럴 타입에 내장 변환 유틸리티 적용
type Brand = "apple" | "samsung";
type BrandUpper = Uppercase<Brand>;   // "APPLE" | "SAMSUNG"
type BrandDisplay = Capitalize<Brand>; // "Apple" | "Samsung"

// 4) 조건부 조합
// 조건부 타입을 함께 사용하여 환경에 따라 문자열 패턴 결정
type Env = "dev" | "prod";
type Path<T extends Env> = T extends "dev" ? `/dev/api` : `/api`;
type DevPath = Path<"dev">;   // "/dev/api"
type ProdPath = Path<"prod">; // "/api"

// 5) 실무 예 — Redux 액션 타입 정의
// 액션 이름과 상태를 조합하여 자동으로 문자열 리터럴 생성
type ActionType = "FETCH" | "CREATE" | "UPDATE";
type Status = "REQUEST" | "SUCCESS" | "FAILURE";
type ApiAction = `${ActionType}_${Status}`;
// "FETCH_REQUEST" | "FETCH_SUCCESS" | "FETCH_FAILURE" |
// "CREATE_REQUEST" | "CREATE_SUCCESS" | ... 등

// 6) API 경로 패턴
// 버전과 리소스를 결합해 타입 안전한 API 엔드포인트 문자열 생성
type Version = "v1" | "v2";
type Resource = "users" | "products";
type ApiPath = `/api/${Version}/${Resource}`; // "/api/v1/users" 등

// 7) i18n 키 패턴
// 다국어 번역 키를 섹션.필드 형식으로 자동 생성
type Section = "home" | "profile";
type Key = "title" | "description";
type I18nKey = `${Section}.${Key}`; // "home.title" | "profile.description"

// 8) 매핑 타입과 결합
// 문자열 리터럴을 이용해 동적으로 키 이름을 생성
type EventMap<T extends string> = {
  [K in T as `${K}_event`]: () => void;
};
type Events = EventMap<"click" | "hover">;
// { click_event: () => void; hover_event: () => void }
