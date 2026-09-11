# 03 — AI Log & Reflection

> Phase 6 — Reflection cá nhân về việc dùng AI làm thought-partner trong Lab 02.

---

## 1. AI đã giúp gì?

* **Brainstorm SCAN nhanh:** Dùng prompt theo 4 lenses để liệt kê bottleneck tại Xanh SM, VinFast, Vinhomes, Vinmec — giúp đủ ≥ 5 bài toán trong thời gian ngắn.
* **Stress-test thẻ bài toán:** Nhờ AI đóng vai CFO / Trưởng vận hành “khắt khe” để chỉ ra metric mơ hồ và chỗ rule-based có thể đủ thay AI.
* **Soạn SYSTEM_PROMPT & ranh giới:** AI gợi ý cấu trúc rule `[DRAFT_ONLY]`, ngưỡng pin 5%, và format JSON `dispatch_mobile_charger` trước khi mình siết lại bằng lời văn vận hành thực tế.
* **Deep-Dive 6-field:** AI giúp điền khung Actor / Bottleneck / Metric / Boundary; mình chỉnh lại số liệu ước tính và ranh giới cấm cho khớp use case Xanh SM.

---

## 2. AI sai / hallucination ở đâu?

* **Số liệu bịa:** AI đưa “80 sự cố/ngày”, “rò rỉ doanh thu 15%” như thể đã đo — thực tế đây chỉ là giả định lab; cần gắn nhãn *ước tính*.
* **Đề xuất Agent quá mức:** Với bài toán có cấu trúc cố định, AI hay đẩy multi-agent trong khi **LLM Feature + rule ngưỡng pin** đã đủ và an toàn hơn.
* **Bỏ qua HITL:** Một số draft prompt ban đầu quên bắt buộc `[DRAFT_ONLY]`, dễ khiến hệ thống hiểu nhầm là được auto-send.
* **Địa chỉ trạm giả:** Khi thiếu GPS thật, AI vẫn “bịa” tên đường/trạm — vi phạm boundary “không bịa địa chỉ khi thiếu dữ liệu”.

---

## 3. Mình đã sửa prompt / ranh giới thế nào?

1. **Siết SYSTEM_PROMPT:** Nêu rõ Rule 1 (`[DRAFT_ONLY]` luôn ở đầu), Rule 2 (pin < 5% → cấm trạm > 5km → bắt buộc `dispatch_mobile_charger`), Rule 3 (format JSON/text).
2. **Thêm adversarial tests:** Không chỉ case pin 2% + trạm 8km, mà thêm case “ép bỏ thẻ nháp” và “VIP/supervisor pressure”.
3. **Temperature thấp (0.2):** Giảm sáng tạo lung tung khi stress-test boundary.
4. **Chọn GO scope hẹp:** Ghi rõ trong Evaluate: chỉ prototype draft sự cố pin, chưa auto-dispatch cuốc thường.

---

## 4. Bài học mang đi

AI hữu ích như **đối tác tư duy** để mở ý tưởng và kiểm tra lỗ hổng, nhưng **không thay** việc tự định nghĩa metric, ranh giới vận hành và kiểm thử adversarial. Trong sản phẩm Vin Smart Future, **Problem First + Boundary First** quan trọng hơn việc “dùng AI cho bằng được”.
