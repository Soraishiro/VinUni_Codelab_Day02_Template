# 🏗️ Deliverable 2: Deep-Dive Report (Vin Smart Future)

> **Dự án:** Trợ lý Điều vận Thông minh Xanh SM — Hỗ trợ sự cố cạn pin xe điện thực địa  
> **Đơn vị công nghệ:** Vin Smart Future — Tập đoàn Vingroup  
> **Công ty thành viên đối tác:** GSM (Xanh SM)  

---

# 🏗️ Phase 3 — DEEP-DIVE: Phân tích Quy trình Chi tiết

## 3.1. Current-State Workflow Mapping
Quy trình thủ công hiện tại khi tài xế Xanh SM báo sự cố cạn kiệt pin giữa đường:

```text
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ Bước 1          │     │ Bước 2          │     │ Bước 3 🔴       │     │ Bước 4 🔴       │
│ Nhận cuộc gọi / │     │ Tra cứu định vị │     │ Tra cứu trạm    │     │ Soạn văn bản    │
│ tin báo cạn pin │ ──> │ GPS xe trên map │ ──> │ sạc VinFast     │ ──> │ hướng dẫn chỉ   │
│ từ tài xế       │     │ nội bộ          │     │ còn trụ trống   │     │ đường cho tx    │
│                 │     │                 │     │                 │     │                 │
│ Actor: Dispatch │     │ Actor: Dispatch │     │ Actor: Dispatch │     │ Actor: Dispatch │
│ ⏱ 2 phút        │     │ ⏱ 2 phút        │     │ ⏱ 5 phút 🔴     │     │ ⏱ 5 phút 🔴     │
│ In: Cuộc gọi tx │     │ In: Biển số xe  │     │ In: Vị trí GPS  │     │ In: Raw data    │
│ Out: Ticket sự cố│    │ Out: Tọa độ     │     │ Out: Địa chỉ trụ│     │ Out: SMS nháp   │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
                                                                                 │
                                                                                 ▼
                                                                        ┌─────────────────┐
                                                                        │ Bước 5 🔄       │
                                                                        │ Điều phối xe    │
                                                                        │ cứu hộ sạc pin  │
                                                                        │ lưu động        │
                                                                        │                 │
                                                                        │ Actor: Dispatch │
                                                                        │ ──> Đội cứu hộ  │
                                                                        │ ⏱ 1 phút        │
                                                                        │ In: Yêu cầu     │
                                                                        │ Out: Lệnh điều  │
                                                                        └─────────────────┘

🔴 = Bottleneck (Bước 3 & Bước 4: Mất 10 phút tra cứu đa màn hình, đối chiếu chuẩn sạc CCS2 và gõ văn bản thủ công)
🔄 = Handoff (Bước 5: Chuyển giao giữa Điều phối viên trung tâm và Đội cứu hộ lưu động qua Zalo/Điện thoại)
⏱ Tổng thời gian vận hành trung bình: **15 phút/lượt**.
```

---

## 3.2. Problem Statement (6-field Standard)

| Trường thông tin | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Điều phối viên (Dispatcher) tại Trung tâm Điều vận Xanh SM (GSM) & Kỹ thuật viên Đội cứu hộ sạc pin lưu động. |
| **2. Current Workflow** | Khi tài xế gọi điện/gửi tin báo pin nguy cấp (< 10%), điều phối viên mở bản đồ fleet nội bộ tra vị trí xe, mở tiếp dashboard trạm sạc VinFast đối chiếu thủ công trạm còn trụ trống tương thích (chuẩn CCS2), tự gõ tin nhắn chỉ dẫn gửi qua App tài xế, hoặc gọi đội sạc pin lưu động nếu pin dưới 5%. Toàn bộ 5 bước thủ công phân tán trên 3 màn hình riêng biệt. |
| **3. Bottleneck** | Bước 3 & Bước 4 (chiếm 10/15 phút): Rà soát thủ công trụ sạc trống theo bán kính an toàn và dòng xe (VF5/VF8), sau đó soạn thảo văn bản chỉ đường chi tiết bằng tiếng Việt trong lúc tài xế đang hoang mang vì xe sắp hết điện. |
| **4. Business Impact** | Toàn quốc có ~350 – 500 ca cạn pin khẩn cấp/ngày. Mỗi ca mất 15 phút xử lý gây quá tải tổng đài (~100 giờ công/ngày). Xe nằm bất động (idle) trung bình 45 phút làm mất 2-3 cuốc đón khách, gây rò rỉ doanh thu ước tính ~2.5 tỷ VNĐ/tháng. Nguy cơ xe chết máy chắn đường gây tắc nghẽn giao thông và ảnh hưởng nghiêm trọng uy tín dịch vụ taxi điện chuẩn 5 sao. |
| **5. Success Metric** | 1. **Hiệu suất:** Giảm tổng thời gian xử lý sự cố từ 15 phút xuống dưới 3 phút (giảm 80% thời gian thao tác).<br>2. **Độ an toàn:** 100% tin nhắn hướng dẫn tạo ra bởi AI đều có tiền tố `[DRAFT_ONLY]` để bảo đảm 100% qua Human-in-the-loop (HITL) phê duyệt trước khi gửi.<br>3. **Độ tin cậy ranh giới:** 0% trường hợp đề xuất trạm sạc cách xa > 5km khi pin dưới 5% (100% kích hoạt lệnh cứu hộ). |
| **6. Operational Boundary** | • **ĐƯỢC PHÉP:** Tự động lấy tọa độ GPS từ xe, truy vấn API danh sách trạm sạc trống VinFast, draft tin nhắn hướng dẫn và tạo sẵn JSON payload điều xe cứu hộ.<br>• **TUYỆT ĐỐI CẤM (Hard Boundary):**<br>  1. Không được tự động gửi tin nhắn trực tiếp đến tài xế khi chưa qua điều phối viên bấm duyệt.<br>  2. Không được đề xuất trạm sạc cách xa > 5km khi pin dưới 5% (phải chuyển sang lệnh `dispatch_mobile_charger`).<br>  3. Không can thiệp vào hệ thống lái hay điều khiển xe từ xa. |

---

## 3.3. Future-State Flow & AI Fit

* **AI-Fit Matrix:** Chọn **LLM Feature** (kết hợp Rule Guardrail). 
  * *Lý do loại trừ Rule-only:* Rule-only tạo tin nhắn máy móc, không linh hoạt theo ngữ cảnh thực địa của từng loại xe và không xử lý được biến thiên tin nhắn tài xế.
  * *Lý do loại trừ Agent tự trị:* Agent tự động hành động có nguy cơ hallucination gây nguy hiểm an toàn giao thông nghiêm trọng (ví dụ tự ra lệnh cho xe chạy trạm xa khi xe sắp hết pin).
* **Quy trình tương lai (Future-State Workflow):**

```text
┌─────────────────┐     ┌─────────────────────────┐     ┌─────────────────────────┐     ┌─────────────────┐
│ Bước 1          │     │ Bước 2 (🔵 AI Step)     │     │ Bước 3 (🔵 AI Step)     │     │ Bước 4 (🟢 HITL)│
│ Nhận tín hiệu   │     │ Auto-pull GPS & SoC pin │     │ LLM sinh văn bản hướng  │     │ Dispatcher kiểm │
│ cạn pin từ xe / │ ──> │ ──> Rule Check:         │ ──> │ dẫn kèm tag             │ ──> │ tra trong 10s   │
│ cuộc gọi tài xế │     │ SoC < 5% ──> Lệnh cứu hộ│     │ [DRAFT_ONLY] hoặc lệnh  │     │ & bấm Duyệt gửi │
│                 │     │ SoC >=5% ──> Query trạm │     │ JSON cứu hộ             │     │                 │
└─────────────────┘     └─────────────────────────┘     └─────────────────────────┘     └─────────────────┘
                                                                                                 │
                                                        ┌────────────────────────────────────────┘
                                                        ▼
                                                 ↩️ Fallback Plan:
                                                 Nếu LLM gặp lỗi (timeout, hallucination, thiếu tag),
                                                 hệ thống kích hoạt Fallback: tự động hiển thị template
                                                 tin nhắn tĩnh mặc định hoặc báo đỏ để Điều phối viên
                                                 chuyển sang xử lý thủ công bằng tay.
```

---

# 🏁 Phase 5 — EVALUATE: Đánh giá Dự án & Quyết định Ban Giám Đốc

### AI Readiness Checklist:
* [x] **Dữ liệu (Data Readiness):** Có sẵn dữ liệu telemetry xe VinFast thời gian thực (SoC pin, vị trí GPS) và API dashboard trạm sạc VinFast.
* [x] **Rủi ro (Risk Containment):** Rủi ro kiểm soát 100% thông qua chốt chặn Human-in-the-loop (tiền tố `[DRAFT_ONLY]`), Rule Guardrail cứng (`Battery < 5%`) và cơ chế Fallback template tĩnh.
* [x] **Con người (Stakeholder Readiness):** Đội ngũ Điều phối viên Xanh SM rất mong muốn áp dụng giải pháp để giảm tải áp lực trực tổng đài vào các khung giờ cao điểm.

### 🏛️ Quyết định của Ban Giám Đốc Vin Smart Future:
**[x] GO (Bắt đầu xây dựng Prototype)**

### 💡 Justification (Căn cứ kỹ thuật & Kinh tế):
1. **Khả thi kỹ thuật cao:** Kiến trúc Hybrid tận dụng Rule Engine để tính khoảng cách và bảo vệ pin khẩn cấp, kết hợp LLM Feature để tạo văn bản chỉ dẫn thân thiện. Độ trễ trung bình của Gemini Flash đạt dưới 1.8 giây.
2. **Hiệu quả kinh tế (ROI) rõ ràng:** Giảm 80% thời gian xử lý sự cố (từ 15 phút xuống dưới 3 phút), tiết kiệm ~100 giờ công lao động mỗi ngày. Giảm tỷ lệ xe nằm bất động (idle time), bảo vệ nguồn thu ước tính hơn 2.5 tỷ VNĐ/tháng.
3. **Chi phí đầu tư siêu thấp:** Chi phí token API ước tính chỉ ~5 – 8 triệu VNĐ/tháng cho toàn bộ 500 sự cố/ngày, đem lại tỷ suất lợi nhuận trên chi phí đầu tư (ROI) vượt mức 300x.
