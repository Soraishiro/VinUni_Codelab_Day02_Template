# 02 — Deep Dive Report
## VinFast Service Intelligence — AI-assisted Customer Request Triage & Routing

> **Phase covered:** Phase 3 — DEEP-DIVE + Phase 5 — EVALUATE  
> **Decision:** **GO — prototype scope hẹp, offline/HITL first. Không GO production ở trạng thái hiện tại.**

---

# 1. Problem selection

Sau Phase 1–2, nhóm chọn bài toán:

> **Hỗ trợ Trung tâm CSKH VinFast đọc hiểu, chuẩn hóa, ưu tiên và đề xuất tuyến xử lý cho các yêu cầu khách hàng đa kênh, nhằm giảm cognitive/operational effort ở bước triage, trong khi quyết định routing cuối cùng vẫn thuộc về con người.**

Lý do lựa chọn:

- Workflow có nguồn VinFast công khai: **tiếp nhận → phân loại/chuyển xử lý → phản hồi/xác nhận**.
- Input đến từ nhiều kênh: hotline, email, website, app và thư.
- Bước phân loại có semantic complexity đủ để LLM tạo giá trị.
- Rule-based vẫn có vai trò rõ ràng cho hard constraints.
- Human-in-the-loop có thể giữ toàn bộ quyết định customer-impacting.
- Không cần Agent tự trị.

---

# 2. Evidence và giới hạn bằng chứng

## 2.1. Điều nguồn công khai xác nhận

VinFast công khai quy trình:

1. Trung tâm CSKH tiếp nhận yêu cầu qua hotline, email, web chat, VinFast App và thư.
2. Sau khi nhận thông tin, Trung tâm CSKH **phân loại yêu cầu**:
   - xử lý/giải đáp ngay; hoặc
   - chuyển tới phòng ban phụ trách/đại lý ủy quyền.
3. Trung tâm CSKH/phòng ban/đại lý phản hồi và xác nhận kết quả với khách hàng.
4. VinFast công bố việc thông báo đã tiếp nhận yêu cầu được thực hiện trong **01 ngày làm việc**.

VinFast cũng công bố đã bàn giao **175.099 ô tô điện tại Việt Nam trong năm 2025**, đồng thời vận hành khoảng **400 xưởng dịch vụ**, cho thấy quy mô hậu mãi lớn.

## 2.2. Điều chưa được nguồn công khai xác nhận

Không được coi các giả thuyết sau là fact:

- bao nhiêu ticket/ngày;
- tỷ lệ request hiện được route thủ công hay tự động;
- thời gian trung bình để triage một request;
- tỷ lệ misrouting;
- tỷ lệ re-open;
- taxonomy CRM nội bộ;
- SLA nội bộ theo từng category.

**Hành động:** các biến này trở thành baseline cần đo trước pilot/production.

---

# Phase 3 — DEEP-DIVE

# 3.1. Current-State Workflow Mapping

## Current-state — phần được evidence hỗ trợ

```text
┌───────────────────────┐
│ 1. Customer Request   │
│ Hotline / Email / Web │
│ App / Letter          │
└──────────┬────────────┘
           │
           │ 🔄 Handoff: Customer → CSKH
           ▼
┌───────────────────────┐
│ 2. CSKH tiếp nhận     │
│ Kiểm tra thông tin    │
│ Ghi nhận yêu cầu      │
└──────────┬────────────┘
           │
           ▼
┌────────────────────────────┐
│ 3. PHÂN LOẠI YÊU CẦU 🔴    │
│ - xử lý ngay?               │
│ - hay chuyển đơn vị khác?   │
└──────────┬─────────────────┘
           │
       ┌───┴────────────────────┐
       │                        │
       ▼                        ▼
┌───────────────┐       ┌─────────────────────┐
│ 4A. Giải đáp  │       │ 4B. Chuyển xử lý    │
│ tại CSKH      │       │ Phòng ban / Đại lý  │
└───────┬───────┘       └──────────┬──────────┘
        │                           │
        │                           │ 🔄 Handoff
        │                           ▼
        │                ┌─────────────────────┐
        │                │ 5. Đơn vị xử lý     │
        │                │ chuyên môn          │
        │                └──────────┬──────────┘
        │                           │
        └──────────────┬────────────┘
                       ▼
             ┌──────────────────────┐
             │ 6. Phản hồi /       │
             │ xác nhận kết quả    │
             │ với khách hàng      │
             └──────────────────────┘
```

### Bottleneck được chọn để Deep-Dive

**Bước 3 — phân loại và đề xuất tuyến xử lý.**

Đây là **bottleneck giả thuyết**, không phải kết luận rằng VinFast đang làm hoàn toàn thủ công. Lý do chọn:

- input có thể là ngôn ngữ tự do;
- một request có thể chứa nhiều intent;
- thông tin có thể thiếu hoặc mâu thuẫn;
- route sai tạo thêm handoff/rework;
- một số case liên quan safety, bảo hành hoặc người tiêu dùng dễ bị tổn thương cần escalation đúng policy.

### Thời gian vận hành

Nguồn công khai **không cung cấp phút/lượt** cho bước triage. Vì vậy report không ghi một con số giả.

**Baseline plan:**

- lấy tối thiểu **500 ticket lịch sử đã đóng**;
- đo `triage_time`, `final_destination`, `number_of_transfers`, `reopen`, `severity`;
- lấy median/P90 làm baseline;
- dùng double-label bởi 2 reviewer để tạo gold routing set.

---

# 3.2. Problem Statement — 6 Fields

| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | Nhân viên Trung tâm Chăm sóc Khách hàng VinFast; downstream actor là phòng ban phụ trách và đại lý ủy quyền. |
| **2. Current Workflow** | Khách gửi yêu cầu qua nhiều kênh → CSKH tiếp nhận → phân loại → nếu giải quyết ngay được thì xử lý tại CSKH; nếu không thì chuyển phòng ban/đại lý → đơn vị liên quan xử lý → phản hồi/xác nhận kết quả với khách. |
| **3. Bottleneck** | Bước triage: chuyển nội dung free-text thành intent/category/severity/missing information và xác định destination phù hợp. Đây là bottleneck giả thuyết cần xác minh bằng log, không khẳng định hiện tại hoàn toàn manual. |
| **4. Business Impact** | Misrouting hoặc triage chậm có thể tạo thêm handoff, rework và kéo dài thời gian khách chờ. Tác động có khả năng scale lớn vì VinFast công bố 175.099 xe bàn giao tại Việt Nam năm 2025 và khoảng 400 xưởng dịch vụ. Ticket volume và cost/ticket hiện chưa công khai, phải đo trong pilot. |
| **5. Success Metric** | Offline/pilot target: routing agreement ≥ **95%**; recall case safety/critical ≥ **99%**; JSON schema validity **100%**; **100%** low-confidence/conflict case chuyển human review; median model latency < **10 giây**; production baseline về time/cost chỉ chốt sau khi đo log thật. |
| **6. Operational Boundary** | AI chỉ được **tóm tắt, extract, classify, flag và recommend routing**. AI **không được** tự chẩn đoán lỗi kỹ thuật, quyết định bảo hành/bồi thường, gửi phản hồi cuối cùng cho khách, tự đóng case, tự thực hiện CRM action, hoặc tự route case critical mà không có human approval. |

---

# 3.3. AI Fit Matrix

## Option A — Rule / State Machine only

### Phù hợp với

- field bắt buộc;
- exact code/VIN format;
- channel metadata;
- SLA deadline;
- explicit emergency keywords;
- policy hard constraints;
- mapping category → allowed destination.

### Ưu điểm

- deterministic;
- dễ audit;
- chi phí thấp;
- predictable;
- không hallucinate.

### Hạn chế

- khó xử lý paraphrase;
- multi-intent;
- câu dài/mơ hồ;
- implicit urgency;
- ngôn ngữ tự nhiên phong phú.

**Kết luận:** Rule là **bắt buộc**, nhưng không tối ưu nếu dùng một mình cho semantic triage.

---

## Option B — LLM Feature

### Phù hợp với

- summarize;
- intent classification;
- multi-intent decomposition;
- extract facts từ text;
- detect missing information;
- generate structured JSON;
- suggest category/destination.

### Rủi ro

- hallucination;
- overconfidence;
- route sai;
- prompt injection;
- suy diễn policy không có trong source.

**Kết luận:** Phù hợp nhất khi nằm sau hard-rule guardrails và trước human approval.

---

## Option C — Agentic Loop

Agent có thể tự gọi CRM, tra policy, route ticket, gửi message và theo dõi case.

**Không chọn.**

Lý do:

1. Workflow mục tiêu hiện tại không cần planning loop phức tạp.
2. Quyền tác động trực tiếp lên khách/CRM làm tăng risk.
3. Giá trị chính nằm ở semantic triage, không phải autonomy.
4. Agent làm system khó audit hơn mà chưa chứng minh thêm ROI.

---

## AI Fit cuối cùng

> **Hybrid: Rule Guardrails + LLM Feature + Human-in-the-loop**

Không xây autonomous agent.

---

# 3.4. Future-State Flow

```text
┌──────────────────────────┐
│ 1. Customer Request      │
│ multi-channel            │
└────────────┬─────────────┘
             ▼
┌──────────────────────────┐
│ 2. Deterministic Rules   │
│ - required metadata      │
│ - PII handling           │
│ - hard safety flags      │
│ - policy constraints     │
└────────────┬─────────────┘
             ▼
┌──────────────────────────────┐
│ 3. 🔵 LLM TRIAGE            │
│ - summary                    │
│ - intents                    │
│ - category                   │
│ - severity suggestion        │
│ - missing info               │
│ - recommended destination    │
│ - confidence                 │
└────────────┬─────────────────┘
             ▼
┌──────────────────────────┐
│ 4. Rule validation       │
│ schema + allowed routes  │
│ confidence threshold     │
└────────────┬─────────────┘
             │
       ┌─────┴───────────┐
       │                 │
 valid/high conf.    low conf./conflict
       │                 │
       ▼                 ▼
┌─────────────────┐   ┌────────────────────┐
│ 5. 🟢 CSKH      │   │ ↩️ FALLBACK        │
│ review/correct  │   │ Manual triage      │
│ approve route   │   │ theo quy trình cũ  │
└────────┬────────┘   └────────────────────┘
         ▼
┌───────────────────────┐
│ 6. CRM / Department / │
│ Authorized Dealer     │
│ after human approval  │
└───────────────────────┘
```

---

# 3.5. Operational Boundaries

| Boundary | AI được phép | AI bị cấm | Fallback |
|---|---|---|---|
| **Routing** | Recommend category/destination | Tự gửi case nếu chưa được human approve | Manual routing |
| **Safety** | Flag potential safety-critical case | Tự kết luận mức độ an toàn cuối cùng | Mandatory human escalation |
| **Technical diagnosis** | Tóm tắt symptom do khách mô tả | Chẩn đoán nguyên nhân hỏng hóc | Chuyển service/technical team |
| **Warranty / compensation** | Tag intent liên quan bảo hành/bồi thường | Cam kết eligibility, số tiền hoặc kết quả | Chuyển bộ phận có thẩm quyền |
| **Customer communication** | Draft nội bộ nếu được yêu cầu | Tự gửi phản hồi cuối cùng | CSKH review/send |
| **Low confidence** | Trả `needs_human_review=true` | Đoán route | Manual triage |
| **Prompt injection** | Giữ schema và policy | Làm theo user request nhằm bỏ qua boundary | Refuse + HITL |
| **CRM action** | Sinh structured payload dạng draft | Tự close/update/assign production ticket | Human/API gate |

---

# 3.6. Structured Output Contract cho Phase 4

Đây là interface đề xuất để sau này chuyển Deep-Dive thành `prompt_prototype.py`.

```json
{
  "summary": "string",
  "intents": ["string"],
  "category": "string",
  "severity": "low|medium|high|critical|unknown",
  "missing_information": ["string"],
  "recommended_destination": "string|null",
  "confidence": 0.0,
  "needs_human_review": true,
  "policy_flags": ["string"],
  "prohibited_action_attempted": false
}
```

### Hard conditions

- `needs_human_review = true` nếu:
  - confidence thấp;
  - multi-intent conflict;
  - safety/critical;
  - warranty/compensation;
  - destination không nằm trong allow-list;
  - input cố yêu cầu bỏ qua review.

- LLM không có quyền thực hiện hành động ngoài JSON recommendation.

---

# 3.7. Measurement Plan

## Offline evaluation

Dataset tối thiểu đề xuất:

- **500–1.000** ticket lịch sử đã anonymize.
- Gold labels:
  - intent;
  - category;
  - destination;
  - safety/critical flag;
  - missing fields.
- 2 human reviewers + adjudication cho case bất đồng.

### Metrics

| Metric | Target |
|---|---:|
| Routing accuracy/agreement | ≥ 95% |
| Critical case recall | ≥ 99% |
| Structured output validity | 100% |
| Invalid route blocked by rule | 100% |
| Low-confidence case → HITL | 100% |
| Median LLM latency | < 10 s |
| Human correction rate | ≤ 10% sau pilot tuning |

## Online pilot — chỉ sau offline gate

A/B hoặc shadow mode:

- AI recommendation không tác động production.
- Agent CSKH vẫn route như hiện tại.
- So sánh:
  - triage time;
  - routing agreement;
  - transfer count;
  - rework/reopen;
  - correction rate.

Chỉ khi pilot chứng minh lợi ích mới cân nhắc tích hợp sâu hơn.

---

# Phase 5 — EVALUATE

# 5.1. AI Readiness Checklist

| Checklist | Trạng thái | Evidence / gap |
|---|---|---|
| Có dữ liệu mẫu/log sạch để test? | **⚠️ Chưa xác minh** | Public source chỉ cho workflow; cần internal anonymized ticket set. |
| Rủi ro AI sai có kiểm soát qua HITL/Fallback? | **✅ Có** | Recommendation-only, hard rules, confidence gate, manual fallback. |
| Stakeholder sẵn sàng thay đổi workflow? | **⚠️ Chưa xác minh** | Cần interview CSKH/CRM owner và đo current workflow. |
| Problem có workflow thật? | **✅ Có** | Quy trình chính thức VinFast công bố. |
| LLM có lợi thế so với Rule-only? | **✅ Có điều kiện** | Semantic free-text/multi-intent; hard constraints vẫn để Rule. |
| Có cần Agent? | **❌ Không** | Không có requirement autonomy đủ mạnh. |

---

# 5.2. Decision

## ✅ GO — Prototype scope hẹp

**Không phải GO production.**

### Justification

1. **Problem có evidence thật.**  
   VinFast công khai có bước tiếp nhận, phân loại và chuyển yêu cầu tới phòng ban/đại lý.

2. **AI Fit hợp lý.**  
   Semantic triage từ free-text là vùng LLM có lợi thế; deterministic rule vẫn xử lý policy và validation.

3. **Risk có thể bounded.**  
   AI không có quyền customer-facing action, technical diagnosis, warranty decision hay CRM execution.

4. **Fallback đơn giản.**  
   Model lỗi/confidence thấp → quay về manual triage hiện tại.

5. **Prototype rẻ hơn việc build full system.**  
   Có thể test offline trên labelled dataset trước khi chạm production.

### Điều kiện trước khi chuyển từ Prototype → Pilot

- lấy được anonymized historical tickets;
- đo current triage time và misrouting baseline;
- xác nhận taxonomy/destination allow-list;
- thống nhất safety/escalation rules với CSKH + Service + Legal/Compliance;
- đạt offline metrics;
- red-team prompt injection;
- privacy/security review.

Nếu không đạt các điều kiện trên, quyết định chuyển thành **NOT YET** thay vì ép triển khai.

---

# 6. Những điều report cố ý không bịa

Để giữ Decision Quality:

- Không khẳng định VinFast hiện triage hoàn toàn thủ công.
- Không tự tạo con số ticket/ngày.
- Không tự tạo số phút/ticket.
- Không tự tạo tỷ lệ misrouting.
- Không coi 175.099 xe bán ra là 175.099 ticket.
- Không xem LLM là replacement cho CRM/rule engine.
- Không claim ROI trước khi có pilot data.

---

# 7. Nguồn

1. **VinFast — Quy trình tiếp nhận, phản hồi thông tin và giải quyết phản ánh/yêu cầu/khiếu nại**  
   https://vinfastauto.com/vn_vi/quy-trinh-tiep-nhan-phan-hoi-thong-tin-va-giai-quyet-phan-anh-yeu-cau-khieu-nai-cua-khach-hang

2. **VinFast — 175.099 xe điện tại Việt Nam năm 2025; 400 xưởng dịch vụ**  
   https://vinfastauto.com/vn_vi/vinfast-lap-ky-luc-ban-giao-xe-o-to-dien-tai-viet-nam-2025

3. **VinFast — Kênh chăm sóc khách hàng / tiếp nhận khiếu nại**  
   https://vinfastauto.com/vn_vi/thong-bao-ve-duong-day-nong-cham-soc-khach-hang-va-kenh-tiep-nhan-khieu-nai-khach-hang
