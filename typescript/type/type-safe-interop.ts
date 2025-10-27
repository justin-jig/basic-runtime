// Type-Safe Interoperability Examples
// 외부 데이터(JSON, API, 환경 변수 등)와의 타입 안전한 상호작용 예제

// 1) unknown 시작
// - 외부 입력값(data)의 타입이 확실하지 않을 때 unknown 사용
// - 조건문으로 타입 검증을 수행 후 안전하게 변환
export function parseData(data: unknown) {
  if (typeof data === "object" && data !== null && "id" in data) {
    // data가 객체이고 id 속성이 존재할 경우
    return (data as { id: number }).id; // 타입 단언 후 반환
  }
  throw new Error("Invalid data format"); // 검증 실패 시 예외 발생
}

// 2) ApiResponse 모델
// - 공통 API 응답 구조 정의
// - data는 성공 시 타입 T로, 실패 시 error 객체로 표현
export type ApiResponse<T> = {
  success: boolean;                             // 요청 성공 여부
  data?: T;                                     // 성공 시 데이터
  error?: { code: string; message: string };    // 실패 시 에러 정보
};

// 3) 타입 안전 fetch
// - fetch 호출 결과를 ApiResponse<T> 형태로 감싼 안전한 래퍼 함수
// - 제네릭 T로 응답 데이터 타입을 호출 시 지정 가능
export async function safeFetch<T>(url: string): Promise<ApiResponse<T>> {
  try {
    const res = await fetch(url);       // HTTP 요청
    const json: T = await res.json();   // JSON 응답을 제네릭 타입으로 변환
    return { success: true, data: json }; // 성공 시 ApiResponse<T> 반환
  } catch (err: any) {
    // 오류 발생 시 표준화된 에러 구조로 반환
    return { success: false, error: { code: "FETCH_ERR", message: err.message } };
  }
}

// 4) 환경 변수 타입 확장 (예시용 선언)
// - Node.js 환경에서 process.env의 타입을 명시적으로 지정하고 싶을 때 사용
// - 실제 코드에서는 주석 해제하여 적용 가능
/*
declare namespace NodeJS {
  interface ProcessEnv {
    NODE_ENV: "development" | "production" | "test"; // 환경 구분
    PORT?: string;                                   // 포트 번호
    DATABASE_URL: string;                            // DB 연결 URL
  }
}
*/

// 5) 브라우저 전역 확장 (예시용 선언)
// - window 객체에 커스텀 전역 변수를 안전하게 추가하고자 할 때 사용
/*
declare global {
  interface Window {
    __APP_VERSION__: string;                      // 앱 버전 정보
    currentUser?: { id: number; name: string };   // 로그인된 사용자 정보
  }
}
*/

// 사용 예시 (비동기 함수 내부)
/*
(async () => {
  const response = await safeFetch<{ id: number; name: string }>("https://api.example.com/user");
  if (response.success && response.data) {
    console.log(response.data.name); // 타입 안전하게 접근 가능
  } else {
    console.error(response.error?.message);
  }
})();
*/
