# BBN 시뮬레이션 과제 (학생용)

## 시작하기

### Google Colab (권장)

1. 이 폴더(`student/`)를 Google Drive에 업로드하거나 GitHub에서 클론
2. `bbn_toy_assignment.ipynb` 파일을 Colab에서 열기
3. 첫 번째 셀을 실행하여 otter-grader 설치
4. 위에서부터 순서대로 셀 실행

### 로컬 실행

```bash
pip install otter-grader numpy matplotlib
jupyter notebook bbn_toy_assignment.ipynb
```

---

## 과제 구조

| Part | 내용 | 문항 수 |
|------|------|--------|
| Part A | 개념 이해 | A0-A10 (11개) |
| Part B | 미니 코딩 실습 | B0-B6 (7개) |
| Part C | BBN 시뮬레이션 완성 | C0-C9 (10개) |

---

## 채점 방법

각 문항별로 즉시 채점:
```python
grader.check('qA0')  # A0 문항 채점
grader.check('qB1')  # B1 문항 채점
```

전체 채점:
```python
grader.check_all()
```

---

## 주의사항

- `tests/` 폴더는 채점에 필요하므로 삭제하지 마세요
- 빈칸(`...`)을 채우고 셀을 실행하세요
- 답은 O/X, A/B/C, 또는 숫자 형식입니다

---

## 오늘의 질문

시뮬레이션을 완성하면 다음 질문에 답할 수 있어야 합니다:

1. 왜 고온에서는 n/p가 "평형"을 따라가나?
2. 왜 어떤 시점부터 평형이 깨지고 "동결(freeze-out)"되나?
3. 왜 마지막에 Yp ≈ 2Xn이 되는가?
