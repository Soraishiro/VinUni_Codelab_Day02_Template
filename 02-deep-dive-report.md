# 02 — Deep-Dive Report (Vin Smart Future)

> Phase 3 (DEEP-DIVE) + Phase 5 (EVALUATE)  
> Bài toán chọn: **Xanh SM — Xử lý sự cố hết pin thực địa**

---

## 3.1. Current-State Workflow Mapping

Quy trình thủ công hiện tại tại Trung tâm Điều vận Xanh SM:

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận cuộc    │     │ Tra cứu định │     │ Tra cứu trạm │     │ Soạn văn bản │
│ gọi / log    │ ──→ │ vị GPS xe    │ ──→ │ sạc VinFast  │ ──→ │ hướng dẫn    │
│ sự cố        │     │              │     │ còn trụ trống│     │ gửi tài xế   │
│              │     │              │     │              │     │              │
│ Ai: Dispatch │     │ Ai: Dispatch │     │ Ai: Dispatch │     │ Ai: Dispatch │
│ ⏱ ~2 phút    │     │ ⏱ ~2 phút    │     │ ⏱ ~5 phút 🔴 │     │ ⏱ ~5 phút 🔴 │
│ In: Điện thoại│    │ In: Biển số  │     │ In: GPS      │     │ In: Raw data │
│ Out: Log     │     │ Out: Toạ độ  │     │ Out: Địa chỉ │     │ Out: SMS/App │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                         🔄 Handoff   ▼
                                                               ┌──────────────┐
                                                               │ Bước 5       │
                                                               │ Gọi xe cứu   │
                                                               │ hộ (nếu cần) │
                                                               │ Ai: Dispatch │
                                                               │ ⏱ ~1 phút    │
                                                               └──────────────┘

🔴 Bottleneck: Bước 3–4 (tra cứu trạm + soạn tin)
🔄 Handoff: Dispatch → App tài xế; Dispatch → Đội cứu hộ
⏱ Tổng thời gian xử lý thủ công: ~15 phút/lượt
```

*(Sơ đồ trực quan xem thêm file `04-workflow-diagram.png`.)*

---

## 3.2. Problem Statement (6-field)

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Điều phối viên (Dispatcher) tại Trung tâm Điều vận Xanh SM (GSM). |
| **2. Current Workflow** | Tài xế báo hết pin → dispatcher tra GPS trên bản đồ nội bộ → mở dashboard trạm sạc VinFast tìm trụ trống phù hợp dòng xe → soạn tin chỉ dẫn gửi App → gọi cứu hộ nếu pin cực thấp. ~5 bước, thủ công, ~15 phút/lượt. |
| **3. Bottleneck** | Bước 3–4 (~10 phút): tìm trụ đúng loại cổng (CCS2/GBT) + soạn tin tiếng Việt rõ ràng dưới áp lực giờ cao điểm. |
| **4. Business Impact** | Ước tính ~80 sự cố pin/ngày tại Hà Nội → ~20 giờ công điều vận/ngày; xe offline làm rò rỉ cuốc và tăng stress tài xế. |
| **5. Success Metric** | (1) Thời gian xử lý trung bình: 15 phút → **dưới 3 phút**. (2) Tỉ lệ hướng dẫn đúng địa điểm & đúng loại trụ: **≥ 98%**. |
| **6. Operational Boundary** | **Được phép:** đọc GPS/API trạm trống, soạn **bản nháp** chỉ dẫn. **Cấm:** tự gửi tin không có HITL; đề xuất trạm > 5km khi pin < 5% (phải `dispatch_mobile_charger`); bịa địa chỉ trạm khi thiếu dữ liệu. |

---

## 3.3. Future-State Flow & AI Fit

### AI-Fit Matrix

| Phương án | Đánh giá | Kết luận |
|---|---|---|
| Rule / State-Machine | Tốt cho ngưỡng pin, khoảng cách, loại cổng — nhưng kém khi soạn tin đa ngữ cảnh | Dùng bổ trợ |
| **LLM Feature** | Phù hợp draft tin + giải thích lý do cứu hộ; quy trình có cấu trúc | **Chọn** |
| Agentic Loop | Tự trị điều xe/gửi tin quá rủi ro khi sai trạm | Không chọn giai đoạn này |

### Future-State Flow

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận sự cố   │ ──→ │ 🔵 Auto-pull │ ──→ │ 🔵 AI draft  │ ──→ │ 🟢 Dispatch  │
│ (App/call)   │     │ GPS + trạm   │     │ SMS/App +    │     │ duyệt HITL & │
│              │     │ trống        │     │ kiểm tra pin │     │ gửi tài xế   │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                         ↩️ Fallback:
                                                         Nếu AI lỗi / không tự tin
                                                         → Dispatcher viết tay như cũ
                                                         Nếu pin < 5% & trạm > 5km
                                                         → bắt buộc dispatch_mobile_charger
```

* 🔵 **AI Step:** lấy ngữ cảnh + draft / quyết định cứu hộ theo ranh giới.  
* 🟢 **HITL:** dispatcher click duyệt trước khi gửi.  
* ↩️ **Fallback:** quy trình thủ công cũ hoặc điều xe sạc di động.

### Prototype ranh giới (Phase 4)

Đã triển khai trong `starter-code/prompt_prototype.py` với Gemini 2.5 Flash:

1. Mọi tin nhắn nháp bắt đầu bằng `[DRAFT_ONLY]`.
2. Pin < 5% → không chỉ đường trạm > 5km → trả `{"action":"dispatch_mobile_charger", ...}`.
3. Có adversarial tests cố tình ép gửi thẳng / bỏ thẻ / VIP pressure.

---

## 🏁 Phase 5 — EVALUATE

### AI Readiness Checklist

1. [x] Có kịch bản test / adversarial inputs để stress-test ranh giới (logs GPS & % pin có thể mock ở giai đoạn prototype).
2. [x] Rủi ro khi AI sai được kiểm soát bằng HITL (`[DRAFT_ONLY]`) và Fallback (thủ công / mobile charger).
3. [x] Stakeholders điều vận sẵn sàng thử scope hẹp (chỉ draft tin sự cố pin, chưa auto-send).

### Quyết định Ban Giám Đốc Vin Smart Future

- [x] **GO (Bắt đầu xây dựng Prototype):** Scope hẹp — LLM Feature soạn nháp + rule pin cực thấp.
- [ ] NOT YET
- [ ] NO-GO

### Justification

Bài toán có **actor rõ**, **bottleneck đo được bằng phút**, và **metric số**. Giải pháp LLM Feature + rule ngưỡng pin đơn giản hơn Agent, rủi ro được khóa bằng HITL và `dispatch_mobile_charger`. Prototype programmatic đã định nghĩa adversarial tests khớp ranh giới vận hành → đủ điều kiện **GO** với scope hẹp (chỉ sự cố pin, chưa mở rộng sang dispatch cuốc thường).
