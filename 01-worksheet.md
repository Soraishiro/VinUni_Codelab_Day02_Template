# Lab 02 — Worksheet: AI Product Scoping (Vin Smart Future)

---

## 🏛️ 1. Bối cảnh thực tế: Vin Smart Future (Vingroup)

**Vingroup** — Tập đoàn tư nhân lớn nhất Việt Nam — vừa sáp nhập toàn bộ các phòng ban công nghệ thuộc các công ty thành viên thành một đơn vị công nghệ thống nhất mang tên **Vin Smart Future**. 

Nhiệm vụ của **Vin Smart Future** là xây dựng các giải pháp AI, số hóa, và tự động hóa cốt lõi để nâng cao hiệu suất vận hành và trải nghiệm khách hàng xuyên suốt các công ty thành viên:
* 🚗 **VinFast:** Hệ thống xe điện thông minh (EV), trợ lý AI ảo trong xe, dự đoán bảo trì pin, và quản lý chuỗi cung ứng sản xuất.
* 🚕 **Xanh SM (GSM):** Vận hành đội xe taxi/xe máy điện thông minh, điều vận thông minh (Smart Dispatching), tối ưu hóa lộ trình di chuyển.
* 🏢 **Vinhomes:** Quản lý đô thị thông minh (Smart Cities), trợ lý cư dân thông minh, tối ưu hóa mức tiêu thụ năng lượng.
* 🏥 **Vinmec:** Y tế thông minh, chẩn đoán hình ảnh bằng AI, tối ưu hóa quản lý hồ sơ bệnh án.
* 🎢 **Vinpearl / VinWonders:** Trải nghiệm du lịch số hóa, quản lý phòng và luồng khách thông minh tại các khu vui chơi.

Trong buổi Lab hôm nay, nhóm của bạn sẽ đóng vai trò là **AI Product Engineer** tại **Vin Smart Future**, tiến hành tìm kiếm, scoping, phân tích độ khả thi, thiết lập ranh giới vận hành, và xây dựng một **bản mẫu kỹ thuật (prompt prototype)** cho một bài toán cụ thể thuộc một trong những mảng kinh doanh trên.

---

## 📊 2. Cơ cấu tính điểm bài lab

### 👥 Điểm nhóm (60 điểm)

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| **G1. Workflow Mapping** | 20 | Problem Deep-Dive | Vẽ chi tiết quy trình hiện tại: các bước, handoff, thời gian, bottleneck |
| **G2. Problem Statement** | 20 | Problem Deep-Dive | Problem Statement 6-field bám sát thực tế, metric có số và ranh giới rõ ràng |
| **G3. AI Fit & Future Flow** | 10 | Problem Deep-Dive | So sánh Rule vs LLM vs Agent, future flow có bước AI, ranh giới và Fallback |
| **G4. Decision Quality** | 10 | Problem Deep-Dive | Quyết định Go/Not Yet/No-Go trung thực và có chứng cứ rõ ràng |

### 👤 Điểm cá nhân (40 điểm)

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| **I1. Scan & Cards** | 15 | Quick Cards | Liệt kê 5 problems sử dụng 3 lenses, hoàn thiện 3 quick cards chất lượng |
| **I2. Prototyping** | 10 | 02-lab/ | Chạy thử nghiệm programmatic prompt prototype thành công |
| **I3. AI Log & Reflection** | 15 | 03-ai-log.md | Phản ánh trung thực về việc dùng AI làm thought-partner (giúp gì, sai gì, sửa gì) |

---

# 🚀 Phase 0 — worked Example: Xanh SM Intelligent Dispatcher (15 min)

*Giảng viên walk-through ví dụ thực tế từ Vin Smart Future để bạn hiểu rõ cách scoping một bài toán AI.*
Đọc chi tiết worked example tại file [02-deliverable-example.md](02-deliverable-example.md).

---

# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).

> [!TIP]
> **🤖 AI Prompts — Partner brainstorm:**
> Hãy sử dụng prompt sau để brainstorm các bài toán thực tế nếu bạn chưa có ý tưởng:
> *"Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng [Chọn một: VinFast / Xanh SM / Vinhomes / Vinmec]. Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất."*

### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | **VinFast** | AI có thể tốt hơn | Sự cố ADAS trên xe VinFast chưa được thu thập có hệ thống — NHTSA triệu hồi 6.300 VF8 tại Mỹ do LKA kích hoạt bất ngờ khi vào cua (Recall 25V-559, 09/2025). Tại VN, người dùng phản ánh LKA giằng lái do vạch đường mờ, VinFast fix bằng OTA từng lần. Đội xe Xanh SM 100K+ là nguồn data thực địa lớn nhưng chưa được khai thác. |
| 2 | **Xanh SM** | Pain từ người khác | Hành vi dịch vụ tài xế kém chưa được giám sát chủ động — S2S (dashcam AI, 04/2025) chỉ giám sát an ninh khung giờ 22h-6h. Cảnh báo gian lận 4 cấp (10/2025) phát hiện gian lận cuốc xe. Hành vi dịch vụ (thái độ kém) vẫn phụ thuộc rating 5 sao thụ động từ khách, yêu cầu ≥ 4.85 sao để nhận thưởng. |
| 3 | **Xanh SM** | Tốn thời gian | Xử lý khiếu nại khách hàng qua tổng đài 1555 (24/7) và App — với ~1 triệu chuyến/ngày. Tính năng giải trình trực tuyến (12/2025) hỗ trợ tài xế giải trình cuốc bị cảnh báo Cao/Rất cao, nhưng phía khách hàng vẫn phản ánh khó kết nối tổng đài giờ cao điểm. |
| 4 | **Vinhomes** | Tốn thời gian | Phân loại & điều phối phản ánh sự cố kỹ thuật cư dân trên App Vinhomes Resident — Dù đã có Trợ lý ảo "Hey Vinhomes" (VinBigdata, 07/2022) hỗ trợ tra cứu tiện ích/hóa đơn, khâu tiếp nhận phản ánh sự cố kỹ thuật (thấm dột, thang máy, hỏng hóc tiện ích) phục vụ gần 650.000 cư dân tại 32 KĐT (cuối 2025) vẫn xử lý thủ công. Đánh giá trên App Store của cư dân phản ánh tình trạng ticket gửi qua App chỉ nhận phản hồi tự động "đã tiếp nhận", thời gian điều phối kỹ thuật BQL xử lý kéo dài do khâu đọc, phân loại và chuyển tiếp về từng phân khu toà nhà hoàn toàn thủ công. |
| 5 | **VinFast** | Tốn thời gian | Liên thông dữ liệu cọc xe & tư vấn bán hàng đa kênh chưa có bộ nhớ xuyên phiên — Dù tổng đài 1900 2323 89 (nhánh 1) đã tích hợp VinBase Callbot trả lời FAQ và ViVi hỗ trợ trên xe, khâu bán hàng đa kênh (Web - Hotline - Showroom) vẫn đứt gãy. Khi các đợt cọc xe điện bùng nổ (kỷ lục 27.649 đơn cọc VF 3 trong 66h, 05/2024), khách cọc online gọi tổng đài hỏi tiến độ giao xe/thủ tục vay, tổng đài không có dữ liệu thực tế tại showroom; khi chuyển máy sang tư vấn viên hoặc đại lý không có Handoff Brief, bắt khách lặp lại nhu cầu từ đầu. Chính sách ưu đãi pin/giá thay đổi liên tục theo tháng dẫn đến telesale tra cứu thủ công và rủi ro lệch kịch bản. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Thu thập, chẩn đoán & phân loại tự động sự cố     │
│ ADAS (LKA, ACC) từ log xe và phản ánh của người lái.        │
│ Công ty thành viên: [x] VinFast                             │
│                                                             │
│ Ai đang đau? Kỹ sư R&D ADAS (lọc thủ công hàng GB log),     │
│ Tài xế/Khách hàng (bất an khi LKA giằng lái, vạch mờ).      │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Xe gặp sự cố ADAS (LKA kích hoạt bất ngờ/cua gắt)      │
│   → 2. Kỹ thuật viên xưởng cắm cổng OBD kéo raw log xe      │
│   → 3. Gửi file log nặng kèm mô tả sơ sài về team R&D       │
│   → 4. Kỹ sư tua log, đối chiếu video tìm nguyên nhân       │
│                                                             │
│ Bước nào tốn nhất? Bước 3-4 (⏱ 2-3 ngày/ca, sót case ~30%)  │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3-4              │
│ (AI Event Extraction: Tự cắt snapshot 30s log sự cố →       │
│ trích xuất bối cảnh vạch đường/góc cua → auto-tag lỗi)      │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian khoanh vùng sự cố từ 3 ngày → dưới 15 phút.  │
│ Tỉ lệ phân loại đúng nhóm nguyên nhân sự cố đạt ≥ 90%.      │
│                                                             │
│ Quick Architecture: [x] AI Agent                            │
└─────────────────────────────────────────────────────────────┘
```

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Tự động phân loại khiếu nại, trích xuất sự vụ     │
│ & hỗ trợ giải trình trực tuyến cho tổng đài Xanh SM 1555.   │
│ Công ty thành viên: [x] Xanh SM                             │
│                                                             │
│ Ai đang đau? CSKH Tổng đài 1555 (quá tải ~1 triệu chuyến/ngày) │
│ Tài xế (bị trừ điểm thưởng/khóa cuốc, chờ duyệt giải trình). │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Khách gọi 1555 hoặc gửi khiếu nại qua App              │
│   → 2. CSKH nghe ghi âm/đọc text, tra cứu cuốc trên CRM     │
│   → 3. Gửi yêu cầu giải trình cho tài xế qua App Driver     │
│   → 4. CSKH đọc giải trình (tính năng 12/2025), đối soát    │
│        lộ trình GPS và ra quyết định xử lý                  │
│                                                             │
│ Bước nào tốn nhất? Bước 2 & 4 (⏱ 15-20 phút/vé khiếu nại)   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 4            │
│ (ASR/NLP phân tích cuộc gọi → tóm tắt sự vụ đối soát GPS    │
│ tự động → draft quyết định giải trình cho CSKH duyệt)       │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian xử lý khiếu nại từ 20 phút → dưới 3 phút/vé. │
│ Tỉ lệ phân loại đúng nguyên nhân khiếu nại đạt ≥ 92%.       │
│                                                             │
│ Quick Architecture: [x] LLM Feature                         │
└─────────────────────────────────────────────────────────────┘
```

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Phân loại & điều hướng tự động phản ánh sự cố kỹ  │
│ thuật từ App Vinhomes Resident đến đúng Ban Quản lý tòa nhà. │
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau? Ban Quản lý toà nhà (quá tải phân loại thủ     │
│ công), Cư dân (chờ xử lý lâu, nhận phản hồi rập khuôn).     │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi phản ánh sự cố kèm ảnh qua App Resident     │
│   → 2. CSKH BQL đọc mô tả, phân loại thủ công chuyên môn    │
│        (kỹ thuật điện nước / thang máy / vệ sinh)           │
│   → 3. Chuyển vé đến đúng tổ kỹ thuật trực ban toà nhà      │
│   → 4. Soạn phản hồi cập nhật trạng thái gửi lại cư dân     │
│                                                             │
│ Bước nào tốn nhất? Bước 2-3 (⏱ 10-12 phút/vé, sai toà ~15%) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3              │
│ (NLP phân loại mô tả sự cố & mức độ khẩn cấp → tự động      │
│ gán vé cho kỹ thuật viên phù hợp → draft phản hồi tiến độ)  │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian phân loại & điều phối từ 10 phút → dưới 1p.  │
│ Tỉ lệ điều hướng đúng tổ kỹ thuật toà nhà đạt ≥ 95%.        │
│                                                             │
│ Quick Architecture: [x] LLM Feature                         │
└─────────────────────────────────────────────────────────────┘
```

> [!TIP]
> **🤖 AI Prompts — Stress-Test thẻ bài toán:**
> Hãy dán nội dung thẻ bài toán của bạn vào LLM để nhận phản biện:
> *"Đây là một thẻ bài toán vận hành tôi đề xuất cho Vin Smart Future: [Dán nội dung]. Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI."*

---

# 🏗️ Phase 3 — DEEP-DIVE (Nhóm, 85 min)

## 3.1. Current-State Workflow Mapping (25 min)
**Vẽ quy trình hiện tại lên bảng/giấy A3.** Sử dụng các ký hiệu:
* 🔴 **Bottleneck:** Bước gây tắc nghẽn, tốn thời gian, hoặc sai sót nhiều nhất.
* 🔄 **Handoff:** Điểm chuyển giao thông tin giữa người và hệ thống, hoặc giữa các bộ phận.
* Ghi rõ thời gian vận hành trung bình: **Tổng cộng = ____ phút/lượt**.

## 3.2. Problem Statement (6-field) & Metrics (15 min)
Điền đầy đủ 6 trường thông tin của bài toán:

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Ai đang thực hiện tác vụ hằng ngày? |
| **2. Current Workflow** | Mô tả tóm tắt quy trình thủ công hiện tại và công cụ sử dụng. |
| **3. Bottleneck** | Bước nào chậm, lỗi, hoặc cần xử lý ngôn ngữ tự động nhiều nhất? |
| **4. Business Impact** | Tổn thất thực tế đo bằng thời gian, chi phí, hoặc SLA của Vingroup. |
| **5. Success Metric** | AI giải quyết được thì đạt ngưỡng số mấy? (Ví dụ: *"85% vé được phân loại dưới 10s"*). |
| **6. Operational Boundary** | AI được phép làm gì, TUYỆT ĐỐI không được làm gì, điểm nào cần duyệt? |

## 3.3. Future-State Flow & AI Fit (25 min)
* **Xác định mức AI Fit (AI-Fit Matrix):** Giải pháp thuộc nhóm nào? [ ] Rule / State-Machine [ ] LLM Feature [ ] Agentic Loop.
* **Vẽ Future-State Flow:** Đánh dấu rõ:
  * 🔵 **AI Step:** Tác vụ LLM xử lý.
  * 🟢 **Human Step (HITL):** Bước con người phê duyệt/review (Human-in-the-loop).
  * ↩️ **Fallback:** Kế hoạch dự phòng khi LLM trả về kết quả lỗi hoặc không tự tin.

---

# 💻 Phase 4 — TECHNICAL PROMPT PROTOTYPE (Nhóm, 30 min)

Để đảm bảo kỹ sư của Vin Smart Future luôn giữ vững năng lực lập trình, nhóm của bạn sẽ tiến hành **lập trình bản mẫu prompt** trực tiếp trên **Gemini 2.5 Flash** bằng Python để stress-test hệ thống.

### Hướng dẫn thực hiện:
1. Mở file [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py) bằng VS Code/Cursor.
2. Hoàn thiện các nội dung sau:
   * **System Prompt:** Viết chỉ thị cực kỳ nghiêm ngặt quy định vai trò, nhiệm vụ, định dạng output và **Operational Boundary (Ranh giới cấm)** của mô hình.
   * **Structured Output:** Định nghĩa định dạng JSON output rõ ràng.
   * **Adversarial Test Cases:** Viết ít nhất 3 prompts "tấn công" (Adversarial inputs) cố tình dụ AI vượt ranh giới hoặc đưa ra câu trả lời không được phép để kiểm tra xem ranh giới của bạn có thực sự vững chắc.
3. Chạy file python:
   ```bash
   python3 prompt_prototype.py
   ```
4. Kiểm tra xem các ranh giới an toàn có bị LLM phá vỡ hay không và ghi lại kết quả vào worksheet.

---

# 🏁 Phase 5 — EVALUATE (Nhóm, 20 min)

### AI Readiness Checklist:
1. [ ] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test?
2. [ ] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)?
3. [ ] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ?

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
[ ] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.
[ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Trì hoãn để chuẩn bị thêm.
[ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
> *Viết lý giải chi tiết tại đây*

---

# 📝 Phase 6 — REFLECTION (Cá nhân)
*Ghi nhận phản ánh của cá nhân bạn về việc phối hợp với AI trong buổi học hôm nay vào file `03-ai-log.md`.*
