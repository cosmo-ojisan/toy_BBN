# BBN 토이 모델 시뮬레이션 과제

빅뱅 핵합성(Big Bang Nucleosynthesis) 토이 모델을 통해 초기 우주의 원소 생성 과정을 이해합니다.

## 시작하기

### Google Colab (권장)

1. 이 폴더를 Google Drive에 업로드하거나 GitHub에서 클론
2. 원하는 노트북 파일을 Colab에서 열기
3. 첫 번째 셀을 실행하여 otter-grader 설치
4. 위에서부터 순서대로 셀 실행

### 로컬 실행

```bash
pip install otter-grader numpy matplotlib
jupyter notebook
```

---

## 과제 구성

### 1차시: H-He-4 토이 BBN — 동결과 헬륨 비율

**파일:** `dist/student/bbn_toy_assignment.ipynb`

| Part | 내용 | 문항 |
|------|------|------|
| Part A | 개념 이해 (플라즈마, 비율, 보존법칙 등) | A0-A11 (12개) |
| Part B | 미니 코딩 (시간-온도, 반응률, 붕괴 함수) | B0-B7 (8개) |
| Part C | BBN 시뮬레이션 완성 | C1-C9 (9개) |

**핵심 질문:**
1. 왜 고온에서는 n/p가 "평형"을 따라가나?
2. 왜 어떤 시점부터 평형이 깨지고 "동결(freeze-out)"되나?
3. 왜 마지막에 $Y_p \approx 2X_n$이 되는가?

---

### 2차시: 중수소 병목 — 핵합성 시작 스위치 ★NEW★

**파일:** `dist/student/bbn_toy_lesson2.ipynb`

| Part | 내용 | 문항 |
|------|------|------|
| Part D | 개념 이해 (가역 반응, 병목, 스위치) | D0-D5 (6개) |
| Part E | 미니 코딩 (스위치 함수 구현) | E0-E3 (4개) |
| Part F | 모형 비교 시뮬레이션 | F0-F3 (4개) |

**핵심 질문:**
1. 왜 온도가 충분히 내려가도 중수소(D)가 바로 쌓이지 않는가?
2. "가역 반응" 관점에서 $p+n \rightleftarrows D+\gamma$를 어떻게 이해할 수 있는가?
3. '핵합성 시작 온도' $T_{\text{nuc}}$는 무엇을 의미하는가?

---

### 3차시: 최소 핵반응 네트워크 — He-4까지 만들기 ★NEW★

**파일:** `dist/student/bbn_toy_lesson3.ipynb`

| Part | 내용 | 문항 |
|------|------|------|
| Part G | 개념 이해 (보존법칙, 네트워크) | G0-G5 (6개) |
| Part H | 미니 코딩 (반응 데이터 구조) | H0-H4 (5개) |
| Part I | 네트워크 시뮬레이션 | I0-I4 (5개) |

**핵심 질문:**
1. 병목이 풀린 뒤 He-4가 "빠르게" 만들어지는 이유는 무엇인가?
2. 핵반응에서도 무엇이 반드시 보존되는가?
3. 여러 반응이 얽힌 네트워크에서 "어느 길이 주요 경로인가"를 어떻게 판단하는가?

---

## 채점 방법

각 문항별로 즉시 채점:
```python
grader.check('qA0')   # A0 문항 채점
grader.check('qD1')   # D1 문항 채점
```

전체 채점:
```python
grader.check_all()
```

---

## 파일 구조

```
toy_bbn/
├── README.md                          # 이 파일
├── docs/
│   ├── explanation.md                 # 1차시 해설서
│   ├── explanation_lesson2.md         # 2차시 해설서
│   └── explanation_lesson3.md         # 3차시 해설서
├── dist/
│   ├── student/
│   │   ├── bbn_toy_assignment.ipynb   # 1차시 학생용 노트북
│   │   ├── bbn_toy_lesson2.ipynb      # 2차시 학생용 노트북
│   │   ├── bbn_toy_lesson3.ipynb      # 3차시 학생용 노트북
│   │   └── tests/                     # 채점용 테스트 파일
│   ├── bbn_toy_lesson2_master.ipynb   # 2차시 강사용 노트북
│   └── bbn_toy_lesson3_master.ipynb   # 3차시 강사용 노트북
└── *_강의계획서_*.md                   # 차시별 강의계획서
```

---

## 주의사항

- `tests/` 폴더는 채점에 필요하므로 삭제하지 마세요
- 빈칸(`...`)을 채우고 셀을 실행하세요
- 답은 O/X, A/B/C, 또는 숫자 형식입니다
- 빈칸을 채우지 못해도 시뮬레이션은 참고 답안으로 실행됩니다

---

## 해설 문서

더 자세한 설명이 필요하면 `docs/` 폴더의 해설서를 참고하세요:

- [1차시 해설서](docs/explanation.md): 동결, Γ/H, Yp = 2Xn
- [2차시 해설서](docs/explanation_lesson2.md): 가역 반응, 중수소 병목, 스위치 함수
- [3차시 해설서](docs/explanation_lesson3.md): 보존법칙, 반응 네트워크, He-4 생성
