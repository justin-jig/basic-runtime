

<h5 align="left">babely</h5>
<p align="left">
  <span>노트 정리 : <a href="https://justin-jig.github.io/justin-book/front/core/">https://justin-jig.github.io/justin-book/front/core/</a></span><br/>
</p>

####  개요

TypeScript의 설정 파일은 **`tsconfig.json`** 형식이며, JSON 구조로 작성된다. 
이 파일은 TypeScript 컴파일러(`tsc`)가 프로젝트를 어떻게 처리할지 결정하는 핵심 설정 파일

---

### 🧾 기본 구조 예시

```json
{
  "compilerOptions": {
    "target": "ES6",
    "module": "CommonJS",
    "strict": true,
    "esModuleInterop": true,
    "baseUrl": "./",
    "paths": {
      "@/*": ["src/*"]
    }
  },
  "include": ["src/**/*.ts"],
  "exclude": ["node_modules"]
}
```

---

### 🔍 주요 필드 설명

| 필드 | 설명 |
|------|------|
| `compilerOptions` | 컴파일러 동작을 제어하는 옵션들 |
| `target` | 컴파일 결과의 ECMAScript 버전 (예: ES5, ES6, ESNext 등) |
| `module` | 모듈 시스템 설정 (예: CommonJS, ESNext 등) |
| `strict` | 엄격한 타입 검사 활성화 |
| `esModuleInterop` | ES 모듈과 CommonJS 간 호환성 설정 |
| `baseUrl`, `paths` | 경로 별칭 설정 (예: `@/components` → `src/components`) |
| `include` | 타입 검사 및 컴파일 대상 파일 경로 |
| `exclude` | 컴파일에서 제외할 경로 |

---

### 📁 위치 및 사용

- 일반적으로 프로젝트 루트에 `tsconfig.json` 파일을 둠
- `tsc` 명령어를 실행하면 해당 파일을 기준으로 컴파일이 진행된다.
- 여러 설정 파일을 분리하고 싶을 경우 `extends` 키워드를 사용해 다른 설정 파일을 확장할 수 있다.

```json
{
  "extends": "./tsconfig.base.json",
  "compilerOptions": {
    "outDir": "dist"
  }
}
```
---
자세한 옵션 목록은 [TypeScript 공식 문서](https://www.typescriptlang.org/ko/tsconfig/)