# 01 — Problem Scan & Quick Cards (Vin Smart Future)

> Bài nộp cá nhân / nhóm — Phase 1 (SCAN) + Phase 2 (QUICK-ASSESS)  
> Vai trò: AI Product Engineer tại **Vin Smart Future**

---

## 🔍 Phase 1 — SCAN: Bảng quét cơ hội (≥ 5 bài toán)

Dùng **4 Lenses** (Lặp lại / Tốn thời gian / AI-upgrade / Stakeholder Pain) quét vận hành các công ty thành viên Vingroup.

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **Xanh SM** | Tốn thời gian | Điều phối viên xử lý thủ công sự cố hết pin thực địa: tra cứu GPS + trạm sạc trống + soạn tin chỉ dẫn (mất ~15 phút/lượt). |
| 2 | **Xanh SM** | Pain từ người khác | Tài xế phản ánh điểm đón gợi ý sai / khó tìm, dẫn đến hủy chuyến và khiếu nàn trên App. |
| 3 | **VinFast** | Lặp lại | So khớp hóa đơn sạc điện từ mạng lưới trạm đối tác với dữ liệu tài chính nội bộ hằng tuần. |
| 4 | **Vinhomes** | AI-upgrade | Phân loại & route khiếu nại cư dân trên App Vinhomes Resident (phản hồi chậm, rập khuôn, SLA kéo dài). |
| 5 | **Vinmec** | Tốn thời gian | Bác sĩ mất 20–30 phút/bệnh nhân để soạn tóm tắt xuất viện từ bệnh án điện tử + xét nghiệm. |
| 6 | **Vinpearl** | Pain từ người khác | Quét review trên OTA (Agoda/Booking) để lọc phàn nàn khẩn cấp gửi Manager trước khi lan rộng. |

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Chọn top 3 từ SCAN: **#1 (Xanh SM sự cố pin)**, **#4 (Vinhomes CSKH)**, **#5 (Vinmec Discharge Summary)**.

### Card #1 — Xanh SM: Xử lý sự cố hết pin thực địa

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Tài xế Xanh SM báo hết pin giữa đường; điều phối │
│ cần tìm trạm sạc / cứu hộ và soạn hướng dẫn nhanh.          │
│ Công ty thành viên: [x] Xanh SM                             │
│                                                             │
│ Ai đang đau? Tài xế (chờ), Dispatcher (quá tải giờ cao điểm)│
│                                                             │
│ Workflow thủ công hiện tại:                                 │
│   1. Nhận cuộc gọi/log sự cố                                │
│   → 2. Tra cứu GPS xe trên bản đồ điều vận                  │
│   → 3. Tìm trạm sạc VinFast còn trụ trống                   │
│   → 4. Soạn tin chỉ dẫn gửi App tài xế                      │
│   → 5. Gọi cứu hộ nếu pin cực thấp                          │
│                                                             │
│ Bước tốn nhất? Bước 3–4 (⏱ ~10–12 phút/lượt)                │
│ AI hỗ trợ ở đâu? Bước 3–4 (gợi ý trạm + draft tin nhắn)     │
│                                                             │
│ Metric: Giảm thời gian xử lý từ ~15 phút → dưới 3 phút.     │
│                                                             │
│ Quick Architecture: [x] LLM Feature                         │
└─────────────────────────────────────────────────────────────┘
```

### Card #2 — Vinhomes: Phân loại & route khiếu nại cư dân

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Ticket khiếu nại trên App bị phân loại sai/chậm,  │
│ CSKH phản hồi rập khuôn, cư dân chờ lâu.                    │
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau? Cư dân (SLA), CSKH & Ban quản lý tòa           │
│                                                             │
│ Workflow thủ công hiện tại:                                 │
│   1. Cư dân gửi ticket trên App                             │
│   → 2. CSKH đọc & phân loại thủ công                        │
│   → 3. Forward sang BQL đúng tòa                            │
│   → 4. Soạn phản hồi / cập nhật trạng thái                  │
│                                                             │
│ Bước tốn nhất? Bước 2–4 (⏱ ~30–60 phút đến phản hồi đầu)    │
│ AI hỗ trợ ở đâu? Phân loại intent + draft phản hồi chuẩn    │
│                                                             │
│ Metric: ≥85% ticket route đúng phòng trong < 5 phút;        │
│         giảm thời gian phản hồi đầu từ 12h → dưới 2h.       │
│                                                             │
│ Quick Architecture: [x] LLM Feature (+ Rule router)         │
└─────────────────────────────────────────────────────────────┘
```

### Card #3 — Vinmec: Tóm tắt hồ sơ xuất viện

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Bác sĩ mất nhiều thời gian soạn Discharge Summary │
│ từ EMR + xét nghiệm + ghi chú lâm sàng.                     │
│ Công ty thành viên: [x] Vinmec                              │
│                                                             │
│ Ai đang đau? Bác sĩ (quá tải), bệnh nhân (chờ giấy tờ)      │
│                                                             │
│ Workflow thủ công hiện tại:                                 │
│   1. Mở EMR / kết quả xét nghiệm                            │
│   → 2. Đọc ghi chú điều trị                                 │
│   → 3. Viết tóm tắt bằng ngôn ngữ dễ hiểu                   │
│   → 4. In / ký / giao bệnh nhân                             │
│                                                             │
│ Bước tốn nhất? Bước 2–3 (⏱ 20–30 phút/bệnh nhân)            │
│ AI hỗ trợ ở đâu? Draft tóm tắt có cấu trúc; bác sĩ duyệt    │
│                                                             │
│ Metric: Giảm thời gian soạn từ 25 phút → dưới 8 phút;       │
│         100% bản nháp phải có bác sĩ phê duyệt (HITL).      │
│                                                             │
│ Quick Architecture: [x] LLM Feature (bắt buộc HITL)         │
└─────────────────────────────────────────────────────────────┘
```

---

## 🗳️ Quyết định lựa chọn (nhóm)

Nhóm chọn **Card #1 — Xanh SM xử lý sự cố hết pin thực địa** để Deep-Dive vì:

* **Tác động real-time rõ:** ảnh hưởng trực tiếp tài xế và doanh thu cuốc xe.
* **Metric đo được:** thời gian xử lý/lượt, tỉ lệ hướng dẫn đúng loại trụ.
* **Ranh giới an toàn khớp prototype:** `[DRAFT_ONLY]` + pin < 5% → `dispatch_mobile_charger`.
* **Card #2** rủi ro pháp lý / tranh chấp phí cao hơn → cần baseline dữ liệu thêm.
* **Card #3** nhạy cảm y tế → phù hợp hơn sau khi đã có quy trình HITL & audit chặt.
