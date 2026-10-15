# Kimi K3 · Claude Opus 5 · Opus 5.5: Effort별 성능·비용 비교

![기존 성능·비용 산점도 — 아래 정정사항 확인 필요](kimi_opus_effort_cost_performance_dotted_labels.png)

> **원본 대조 후 정정:** 위 PNG는 사용자 업로드 원본을 보존한 상태이며, **Kimi K3 Low 및 Opus 5 Low의 점수는 현재 공식 원본과 일치하지 않습니다.** 정정값은 아래 및 CSV를 기준으로 확인하세요.

## 그래프 출처 / 기준

- **출처:** [Artificial Analysis](https://artificialanalysis.ai/)
- **성능:** Artificial Analysis Intelligence Index v4.3.2
- **벤치마크:** AI 에이전트(30%)·코딩(20%)·과학적 추론(20%)·일반 지능(30%)의 **10개 평가** 종합.
- **비용:** 동일 벤치마크 작업당 가중평균 비용(USD). **OpenRouter 청구액이 아님.**
- **토큰:** 벤치마크 작업당 출력 토큰과 그중 추론 토큰. 추론 토큰을 출력 토큰에 다시 더하지 않음.
- **Effort:** 공개된 Low / Medium / High / XHigh / Max 등 모델별 추론 강도. 같은 이름이라도 모델 간 계산량이 동일하다는 뜻은 아님.
- **주의:** KIMI 비용은 문 샷 공식 api 기준이며 OpenRouter 실제 청구 비용과는 다르다. OpenRouter는 open weight model을 사설로 서빙하는 다수 업체들을 연결하여 서비스 하며 이 사설 업체들 중에는 현재 43%까지 공격적으로 할인하는 업체도 존재한다.
- **조회 기준:** 2026-10-15

## Kimi 비용 출처 교차검증

- [Moonshot 공식 API 가격표](https://platform.kimi.ai/zh-hans): K3 입력 **$3.00/100만 토큰**, 출력 **$15.00/100만 토큰**, 캐시 적중 **$0.30/100만 토큰**.
- [Artificial Analysis Kimi K3 Max](https://artificialanalysis.ai/models/kimi-k3/): **“based on Kimi's API”**라고 명시하고 동일한 **$3/$15** 단가 및 **작업당 $2.00**를 제시한다. 따라서 그래프의 Kimi 비용은 Moonshot 공식 API 단가에 기반한 Artificial Analysis 작업당 비용이라는 점이 확인된다.
- [Artificial Analysis Kimi K3 Low/Max 비교](https://artificialanalysis.ai/models/comparisons/kimi-k3-low-vs-kimi-k3): Low **$1.15**, Max **$2.00** 작업당 비용을 제시한다.
- [OpenRouter Kimi K3](https://openrouter.ai/moonshotai/kimi-k3): 특정 공급자 기준 입력 **$1.70**, 출력 **$8.50**, 캐시 읽기 **$0.17**이 표시된 사례는 Moonshot 공식 단가 대비 **43.3% 저렴**하다. 이는 모든 공급자에 대한 일률적 할인이나 실제 청구액 보장이 아니다.

## 원본 데이터 일대일 검증 (2026-10-15)

12개 행의 Intelligence Index·작업당 비용·작업당 출력 토큰·추론 토큰을 Artificial Analysis 모델 비교표와 대조했다. **10개 행은 기존 값과 일치했고, 2개 행은 정정했다.**

| 모델 / Effort | 검증 결과 | 원본 근거 |
|---|---|---|
| Kimi K3 Low | **정정:** 점수 30 → **34 (추정치)**. 현재 작업당 비용·출력/추론 토큰은 **N/A**. 기존 $1.15·12k·6k는 현재 공식 표에서 확인 불가 | [모델 페이지](https://artificialanalysis.ai/models/kimi-k3-low) |
| Kimi K3 Max | **일치:** 44 / $2.00 / 48k / 32k | [비교](https://artificialanalysis.ai/models/comparisons/kimi-k3-vs-claude-opus-5) |
| Opus 5 Low | **정정:** 점수 40 → **39**. $1.10 / 15k / 7k는 일치 | [비교](https://artificialanalysis.ai/models/comparisons/claude-opus-5-5-low-vs-claude-opus-5-low) |
| Opus 5 Medium | **일치:** 45 / $2.19 / 29k / 15k | [비교](https://artificialanalysis.ai/models/comparisons/claude-opus-5-vs-claude-opus-5-medium) |
| Opus 5 High | **일치:** 48 / $3.61 / 46k / 25k | [비교](https://artificialanalysis.ai/models/comparisons/step-5-vs-claude-opus-5-high) |
| Opus 5 XHigh | **일치:** 50 / $4.88 / 61k / 35k | [비교](https://artificialanalysis.ai/models/comparisons/claude-opus-5-vs-claude-opus-5-xhigh) |
| Opus 5 Max | **일치:** 51 / $5.86 / 73k / 43k | [비교](https://artificialanalysis.ai/models/comparisons/kimi-k3-vs-claude-opus-5) |
| Opus 5.5 Low | **일치:** 42 / $0.55 / 10k / 3k | [릴리스 비교](https://artificialanalysis.ai/models/releases/comparisons/claude-opus-5-5-vs-kimi-k3) |
| Opus 5.5 Medium | **일치:** 51 / $1.34 / 26k / 12k | [릴리스 비교](https://artificialanalysis.ai/models/releases/comparisons/claude-opus-5-5-vs-kimi-k3) |
| Opus 5.5 High | **일치:** 54 / $1.82 / 36k / 18k | [릴리스 비교](https://artificialanalysis.ai/models/releases/comparisons/claude-opus-5-5-vs-kimi-k3) |
| Opus 5.5 XHigh | **일치:** 56 / $3.46 / 66k / 40k | [릴리스 비교](https://artificialanalysis.ai/models/releases/comparisons/claude-opus-5-5-vs-kimi-k3) |
| Opus 5.5 Max | **일치:** 58 / $5.98 / 119k / 84k | [릴리스 비교](https://artificialanalysis.ai/models/releases/comparisons/claude-opus-5-5-vs-kimi-k3) |

**표기:** 점수 / 작업당 비용(USD) / 작업당 출력 토큰 / 작업당 추론 토큰. Kimi Low의 34점은 원본에서 독립 평가 예정인 추정치로 표시한다. 현재 수치와 2026-10-15 당시 수치가 달랐을 가능성이 있으나, 당시 원본 스냅샷은 확보되지 않았다.

## 원본

- [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [Artificial Analysis 평가 방법론](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- [OpenRouter Kimi K3 공급자·가격](https://openrouter.ai/moonshotai/kimi-k3)
