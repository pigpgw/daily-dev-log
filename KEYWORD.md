# 참고 학습 목록

> 프론트엔드 개발자로서 실무에 필요한 지식과 사고방식을 체계적으로 학습하기 위한 목록입니다.

---

## JavaScript (심화 · 내부 동작 중심)

### 엔진 & 실행

- [ ] 자바스크립트 공식문서 읽기 (MDN → TC39 흐름 이해)
- [ ] JS 엔진 구조
  - [ ] V8
  - [ ] SpiderMonkey
- [ ] 인터프리터 vs 컴파일러
- [ ] JIT 컴파일러 (Just-In-Time Compiler)
- [ ] 바이트코드 개념
- [ ] 가비지 컬렉션 (Mark & Sweep 개념)

### 실행 흐름

- [ ] 이벤트 루프
- [ ] Call Stack
- [ ] Task Queue
- [ ] Microtask Queue
- [ ] Promise 내부 동작
- [ ] async / await 트랜스파일 결과

### 메모리 & 성능

- [ ] 메모리 누수 패턴
- [ ] 클로저로 인한 참조 유지
- [ ] 성능 측정 기초 (Performance 탭)

---

## React (실무 감각 & 구조 설계)

### 렌더링 & 성능

- [ ] 리액트 컴포넌트 렌더링 원리
- [ ] React DevTools를 통한 렌더링 분석
- [ ] 왜 리렌더링이 발생하는가
- [ ] useMemo / useCallback 실제 기준
- [ ] React Strict Mode의 의미

### 컴포넌트 설계

- [ ] 공통 컴포넌트 설계 원칙
- [ ] 공통 버튼 컴포넌트 설계
- [ ] 역할 분리 (UI / Logic)
- [ ] props 설계 기준
- [ ] variant / size / disabled 패턴
- [ ] Compound Component 패턴 (개념)
- [ ] Presentational / Container 패턴

### 아키텍처 & 원칙

- [ ] 리액트에서의 단일 책임 원칙
- [ ] 컴포넌트 책임 범위 나누기
- [ ] 폴더 구조 설계 기준
- [ ] 재사용과 결합도의 트레이드오프

### 데이터 & 비동기

- [ ] React Query 사람답게 쓰기
  - [ ] staleTime / cacheTime
  - [ ] enabled 옵션
  - [ ] refetch 전략
- [ ] Suspense 개념과 한계
- [ ] Error Boundary
- [ ] 무한 스크롤
  - [ ] cursor 기반
  - [ ] page 기반
- [ ] Optimistic Update

### 도구

- [ ] Storybook
  - [ ] 디자인 시스템 기초
  - [ ] 테스트 가능한 컴포넌트 설계

---

## 네트워크 & API 사고방식

### REST & 통신

- [ ] REST API 설계 개념
- [ ] HTTP 상태 코드 설계 의도
- [ ] API 응답 구조 통일
- [ ] Pagination / Cursor
- [ ] 에러 응답 스펙

### 타입 & 계약

- [ ] 기본 타입 확장
- [ ] API Response 타입 공통화
- [ ] 서버 ↔ 프론트 계약 개념
- [ ] DTO 개념 재정리

---

## 에러 처리 (실무에서 제일 중요)

### 에러 분류 사고

- [ ] 예측 가능한 에러
  - [ ] 데이터 없음
  - [ ] API 실패
  - [ ] 네트워크 끊김
  - [ ] 네트워크 지연
- [ ] 예측 불가능한 에러
  - [ ] 런타임 에러
  - [ ] 예상 못한 응답 구조

### 처리 전략

- [ ] UI 레벨 에러 처리
- [ ] Global Error Handler
- [ ] Error Boundary 활용
- [ ] 사용자 메시지 설계
- [ ] 로그 vs 사용자 피드백 분리

---

## 프론트엔드 사고력

### UX & 사용자 관점

- [ ] 로딩 전략
- [ ] Skeleton UI
- [ ] Empty State 설계
- [ ] 실패했을 때의 UX

### 유지보수 관점

- [ ] 코드 읽기 쉬운 구조
- [ ] 네이밍 전략
- [ ] 주석 vs 코드로 설명
- [ ] 리팩토링 기준

---
