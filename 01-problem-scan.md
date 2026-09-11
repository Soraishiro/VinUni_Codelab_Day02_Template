# 🔍 Deliverable 1: Problem Scan & Quick Cards (Vin Smart Future)

> **Dự án:** Trợ lý Điều vận Thông minh Xanh SM (Intelligent Dispatcher Co-Pilot)  
> **Đơn vị công nghệ:** Vin Smart Future — Tập đoàn Vingroup  
> **Công ty thành viên:** GSM (Xanh SM)  

---

# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội tối ưu hóa bằng AI

Áp dụng **4 Lenses** quét qua toàn bộ hoạt động vận hành của các công ty thành viên Vingroup, nhóm đã ghi nhận 5 bài toán/bottleneck thực tế:

### 📝 Bảng danh mục bài toán (SCAN):

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | **Xanh SM** | Tốn thời gian | Điều phối viên xử lý thủ công sự cố xe điện khẩn cấp/hết pin giữa đường: tra cứu trạm sạc trống và gọi xe cứu hộ (12-18 min/lượt). |
| 2 | **Xanh SM** | Pain từ người khác | Giải tỏa điểm nghẽn đón khách tại sảnh tòa nhà đại đô thị/sân bay do GPS drift khiến tài xế - khách lệch vị trí và hủy cuốc (chiếm 20% cuốc hủy). |
| 3 | **Xanh SM** | Lặp lại | Phân loại & gắn thẻ lý do hủy chuyến tự động từ hội thoại ghi âm tổng đài CSKH và ghi chú text của tài xế (hiện chỉ audit thủ công được <3%). |
| 4 | **Xanh SM** | AI-upgrade | Tự động ghép nối và điều phối xe cho cuốc đặt trước sân bay/đường dài dựa trên mức pin thực tế (SoC), lịch trình sạc và xác suất đúng giờ. |
| 5 | **Xanh SM** | Lặp lại | Tự động đối soát và thẩm định khiếu nại cước phí phát sinh (vé BOT, sai lệch lộ trình GPS) giữa tài xế và hành khách (8-12 min/ticket). |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Chọn **top 3 bài toán** tiềm năng nhất từ danh sách SCAN để hoàn thiện 3 Quick Problem Cards:

### 📇 Thẻ bài toán #1 (Lựa chọn ưu tiên — Primary Focus)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Hỗ trợ điều phối viên xử lý sự cố xe taxi │
│ điện cạn pin (< 10%) giữa đường: tìm trạm sạc / điều cứu hộ.│
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Tài xế (hoang mang), Điều phối viên     │
│ (quá tải tra cứu đa hệ thống), Khách hàng (bị trễ chuyến).   │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Tài xế gọi hotline ──> 2. ĐPV tra cứu vị trí xe trên map│
│   ──> 3. Tra cứu dashboard trạm sạc VinFast xem trụ trống   │
│   ──> 4. Soạn tin nhắn hướng dẫn hoặc gọi xe sạc lưu động    │
│   ──> 5. Cập nhật mã sự cố lên CRM nội bộ.                   │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3-4 (⏱ 12 phút/lượt)  │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3-4               │
│ (Tổng hợp SoC + tọa độ -> Query trạm khả dụng -> Draft tin   │
│ hướng dẫn chuẩn mẫu / lệnh gọi xe cứu hộ cho ĐPV duyệt).    │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   - Giảm thời gian xử lý sự cố từ 15 min ──> dưới 3 min.    │
│   - 100% chỉ dẫn gửi đi đều có tiền tố [DRAFT_ONLY] qua HITL.│
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

### 📇 Thẻ bài toán #2

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Chuẩn hóa điểm đón cho tài xế và khách tại│
│ các khu vực phức tạp (sảnh Vinhomes, ga sân bay) bị lệch GPS│
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Tài xế & Hành khách (lạc nhau, hủy cuốc)│
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Khách đặt xe, ghim vị trí trên app                      │
│   ──> 2. GPS drift lệch sang sảnh đối diện/tầng khác         │
│   ──> 3. Tài xế & khách gọi điện 3-4 cuộc mô tả mốc đón      │
│   ──> 4. Không tìm thấy nhau ──> Khách/tài xế bấm hủy chuyến.│
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 (⏱ 7 phút/lượt)      │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3               │
│ (Trích xuất landmark từ tin nhắn chat của khách -> Khớp với │
│ danh mục sảnh/cột chuẩn -> Gợi ý điểm đón chính xác cho cả 2)│
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   - Giảm tỉ lệ hủy chuyến tại đại đô thị từ 20% ──> dưới 8%  │
│   - Rút ngắn thời gian đón xe thực tế từ 8 min ──> < 3 min. │
│                                                             │
│ Quick Architecture: [ ] No AI  [x] Rule  [ ] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

### 📇 Thẻ bài toán #3

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Phân tích & gắn nhãn tự động lý do hủy    │
│ chuyến từ ghi âm tổng đài CSKH và ghi chú ngắn của tài xế.   │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Đội ngũ QA/Vận hành (quá tải nghe thủ   │
│ công), Giám đốc Vận hành (thiếu insight dữ liệu thực địa).   │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Xuất file ghi âm cuộc gọi hủy & ghi chú của tài xế      │
│   ──> 2. Nhân viên QA nghe băng ghi âm (3-5 min/cuộc)        │
│   ──> 3. Đọc ghi chú viết tắt/không dấu của tài xế           │
│   ──> 4. Gắn nhãn phân loại thủ công vào bảng tính CRM.      │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ 5 phút/ca)      │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3-4             │
│ (Speech-to-Text chuyển băng -> LLM trích xuất lý do chính    │
│ theo chuẩn taxonomy 10 danh mục -> Tự động ghi vào DB).      │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   - Tăng tỷ lệ audit cuộc gọi hủy từ 3% ──> 100% toàn hệ thống│
│   - Độ chính xác phân loại theo taxonomy chuẩn đạt >= 90%.   │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```
