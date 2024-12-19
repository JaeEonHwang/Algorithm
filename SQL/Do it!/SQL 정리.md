```SQL
WITH RECURSIVE EmployeeHierarchy AS (
    SELECT employee_id, manager_id, name
    FROM employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, e.manager_id, e.name
    FROM employees e
    JOIN EmployeeHierarchy eh ON e.manager_id = eh.employee_id
)

SELECT * FROM TABLE1 T1
    INNER JOIN TABLE2 T2 WHERE T1.A = T2.A  
WHERE A = 1 AND B LIKE '%#%_[A, B][A - C][^A][A, C-E][^A-C]' ESCAPE '#'
GROUP BY C
HAVING D IS NOT NULL
ORDER BY E ASC
LIMIT 5 OFFSET 3;
```


### 논리 연산자
|연산자|설명|
|-|-|
|ALL|모든 비교 집합이 TURE면 TRUE|
|AND|두 부울 표현식이 모두 TURE이면 TRUE|
|ANY|비교 집합 중 하나라도 TRUE이면 TRUE|
|BETWEEN|피연산자가 범위 내에 있으면 TRUE|
|EXISTS|하위 쿼리에 행이 포함되면 TRUE|
|IN|피연산자가 리스트 중 하나라도 포함되면 TRUE|
|LIKE|피연산자가 패턴과 일치하면 TRUE|
|NOT|부울 연산자를 반대로 실행|
|OR|하나의 부울식이 TRUE이면 TRUE|
|SOME|비교 집합 중 일부가 TRUE이면 TRUE|

</br>

* 쿼리 짤 때는 항상 NULL도 유의하기

</br>

### 와일드카드
|와일드카드|설명|
|-|-|
|%|0개 이상의 문자열과 대치|
|_|1개의 문자열과 대치|
|[A, B, C]|범위 지정|
|[A-C]|범위 지정|
|[^A]|특정 문자 제외|

</br>

### 집계 함수
|함수|설명|
|-|-|
|COUNT([DISTINCT])|그룹 내 행의 수|
|SUM()|그룹 내 특정 열 값의 합계|
|AVG()|그룹 내 특정 열 값의 평균|
|MIN()|그룹 내 특정 열 값의 최소값|
|MAX()|그룹 내 특정 열 값의 최대값|
|GROUP_CONCAT([DISTINCT] NAME [ORDER BY expression] [SEPARATOR separator])|그룹 내 특정 열 값을 하나의 문자열로 연결|
|STD() / STDDEV()|그룹 내 데이터의 표준 편차|
|VARIANCE() / VAR_POP()| 그룹 내 데이터의 분산|

</br>

### 집합 연산자
|함수|설명|
|-|-|
|UNION|합집합|
|INTERSECT|교집찹|
|EXCEPT|차집합|

</br>

### 순위 함수
```SQL
RANK() OVER (PARTITION BY A ORDER BY B ASC)
DENSE_RANK() OVER () -- 공동순위 무시 EX) 1, 1, 2, 3
NTILE(5) OVER ()
```

</br>

### 제어 흐름 함수
```SQL
SELECT IF(1 > 2, 'True', 'False');  -- 'False'
SELECT CASE
         WHEN age >= 18 THEN 'Adult'
         ELSE 'Minor'
       END AS age_group
FROM users;
SELECT IFNULL(NULL, 'Default');  -- 'Default', 첫번째 매개변수가 NULL이면 2번째 매개변수 반환, 아니면 첫번째 매개변수 반환
SELECT NULLIF(10, 10);  -- NULL, 매개변수들이 같으면 NULL, 아니면 첫번째 매개변수 반환
SELECT COALESCE(NULL, NULL, 'First Non-Null');  -- 'First Non-Null', 처음으로 NULL이 아닌 것 반환




```