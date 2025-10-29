

<h1 align="center">back/nodejs Repository</h1>
<p align="center">
  <span>노트 정리 : <a href="https://justin-jig.github.io/justin-book/runtime/">https://[justin-jig.github.io/justin-book/runtime](https://justin-jig.github.io/justin-book/runtime/</a></span><br/>
</p>


- AUTO_INCREMENT → SERIAL
- CONCAT → ||
- LIMIT offset,count → LIMIT count OFFSET offset
- NOW() 그대로 사용 가능
- GROUP BY 표준 준수 (모든 비집계 컬럼 명시)
- MySQL의 비표준 문법(암시적 GROUP BY, 허용되지 않은 SELECT)은 PostgreSQL에서 오류
- PostgreSQL은 MVCC 기반 트랜잭션 모델로 동시성 제어가 안정적
