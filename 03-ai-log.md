# 03 — AI Log & Reflection: Nhật Ký Tương Tác và Phản Biện AI

**Dự án:** Vin Smart Future — VinFast Customer Request Triage & Routing  
**Học viên / Vai trò:** AI Product Engineer  
**Công cụ AI sử dụng:** Google Gemini 2.5 Flash / Claude 3.5 Sonnet / ChatGPT  

---

## 1. Bối cảnh sử dụng AI làm "Thought-Partner"

Trong bài Lab 02 về **AI Product Scoping**, nhóm xác định nguyên tắc cốt lõi: **"Problem First, AI Second"** — AI đóng vai trò là một người cộng sự phản biện (Thought-Partner), tuyệt đối không phải là một cỗ máy thần thánh đưa ra chân lý (Oracle) để copy-paste mù quáng.

Quá trình làm việc tập trung vào 3 mục tiêu:
1. Brainstorm và lọc bài toán thực tế theo 4 Lenses (Repetitive, Time-consuming, AI-upgrade, Stakeholder Pain).
2. Xây dựng ranh giới vận hành (Operational Boundaries) và phân tích AI Fit (Rule vs LLM vs Agent).
3. Thiết kế prompt prototype an toàn, chống tấn công prompt injection và bảo vệ an toàn nghiệp vụ.

---

## 2. AI đã giúp được gì? (Strengths & Value Add)

Trong suốt quá trình scoping, AI đã hỗ trợ hiệu quả ở các khâu:

* **Mở rộng góc nhìn đa chiều (Brainstorming across Lenses):** Khi bắt đầu quét các công ty thành viên Vingroup (VinFast, Vinhomes, Vinpearl, VinBus), AI đã gợi ý nhanh chóng các điểm chạm vận hành phổ biến trong ngành dịch vụ và ô tô điện, giúp nhóm hình dung được bức tranh luồng dữ liệu từ khách hàng đến các phòng ban hậu mãi.
* **Cấu trúc hóa thông tin phi cấu trúc:** AI rất xuất sắc trong việc chuyển đổi các mô tả nghiệp vụ rời rạc thành bảng biểu so sánh, ma trận đánh giá (AI Fit Matrix), và khung Problem Statement chuẩn 6-field của Vin Smart Future.
* **Đề xuất bộ taxonomy và schema JSON mẫu:** AI hỗ trợ soạn thảo nhanh JSON Schema đại diện cho hợp đồng dữ liệu giữa CSKH Tier 1 và các phòng ban chuyên môn/Xưởng dịch vụ (bao gồm: `category`, `severity`, `recommended_destination`, `missing_information`, `confidence`).
* **Đóng vai kẻ tấn công (Red Teaming):** Khi thử nghiệm prompt prototype, AI đóng vai một tài xế hoặc khách hàng giận dữ, cố tình đưa ra các yêu cầu bẻ khóa ranh giới an toàn (như ép buộc gửi tin nhắn không qua kiểm duyệt, yêu cầu điều hướng xe pin nguy cấp đi xa).

---

## 3. AI trả lời sai và ảo giác (Hallucination) ở đâu?

Dưới đây là các ví dụ thực tế mà nhóm phát hiện AI đưa ra thông tin sai lệch, nguy hiểm hoặc thiếu căn cứ:

### 🚨 Sai lầm 1: Bịa đặt số liệu vận hành và thời gian (Fabricated Baselines)
* **Câu trả lời của AI ban đầu:** Khi được hỏi về quy mô CSKH VinFast, AI tự tin trả lời: *"Mỗi ngày tổng đài VinFast tiếp nhận 50.000 ticket khiếu nại, nhân viên mất trung bình 15 phút để xử lý một ticket và tỷ lệ chuyển nhầm phòng ban là 28%."*
* **Thực tế kiểm chứng:** Đây là **100% ảo giác (hallucination)**. VinFast không hề công bố các chỉ số nội bộ này. Con số 50.000 ticket/ngày là hoàn toàn bịa đặt.
* **Cách xử lý của nhóm:** Nhóm kiên quyết loại bỏ toàn bộ các con số giả này khỏi báo cáo. Thay vào đó, nhóm chuyển các biến này thành mục **"Baseline cần đo trong giai đoạn Pilot/Log audit"** (đo trên 500 ticket lịch sử thực tế).

### 🚨 Sai lầm 2: Đề xuất "Autonomous Agent" vi phạm ranh giới an toàn (Over-automation)
* **Câu trả lời của AI ban đầu:** AI đề xuất một giải pháp "Agentic AI toàn diện": *"AI Agent tự động đọc email khách hàng, tự chẩn đoán nguyên nhân hỏng hóc của xe, tự quyết định chính sách bồi thường/bảo hành pin và tự gửi email trả lời khách hàng để tối ưu hóa 100% nhân lực."*
* **Thực tế phân tích:** Đây là thiết kế cực kỳ nguy hiểm và ngây thơ về mặt vận hành doanh nghiệp:
  1. AI không thể và không được phép tự chẩn đoán hỏng hóc kỹ thuật xe điện qua văn bản khách nhắn.
  2. Quyết định bồi thường/bảo hành liên quan trực tiếp đến pháp lý và chi phí tài chính của VinFast, bắt buộc phải do nhân sự có thẩm quyền phê duyệt.
  3. Tự ý gửi thư cho khách hàng mà không có Human-in-the-loop (HITL) sẽ gây khủng hoảng truyền thông nếu AI nói bậy hoặc cam kết sai.
* **Cách xử lý của nhóm:** Nhóm bác bỏ hoàn toàn kiến trúc Agent tự trị, hạ cấp AI Fit xuống mức **LLM Feature (Co-pilot)** kết hợp **Rule-based guardrails** và **bắt buộc có con người kiểm duyệt (Human-in-the-loop)** trước khi gửi đi.

### 🚨 Sai lầm 3: Nhầm lẫn giữa tính năng đã tồn tại và cơ hội mới
* **Câu trả lời của AI ban đầu:** AI gợi ý giải pháp: *"Xây dựng Trợ lý ảo cho cư dân Vinhomes để tra cứu tiền điện nước và tiện ích"* hoặc *"AI tóm tắt bệnh án cho Vinmec"*.
* **Thực tế kiểm chứng:** Khi tra cứu tài liệu thực tế của Vingroup, Vinhomes đã có Trợ lý ảo cư dân từ năm 2022 trên app Vinhomes Resident, và Vinmec đã tích hợp phần mềm DrAid từ lâu (tiết kiệm 80% thời gian tóm tắt hồ sơ).
* **Cách xử lý của nhóm:** Thực hiện ngay bước **"0. Lọc ảo (Reality Check)"** ở đầu bài để loại bỏ ngay những ý tưởng trùng lặp với sản phẩm đã có.

---

## 4. Quá trình điều chỉnh Prompt & Thiết lập Ranh giới (Boundary Setting)

Để buộc AI làm việc chính xác và thực tế, nhóm đã liên tục tinh chỉnh câu lệnh (Prompt Refinement):

1. **Ép buộc Grounding & No-Hallucination:**
   > *Prompt cũ:* "Hãy ước tính thời gian và quy mô của CSKH VinFast để phân tích ROI."  
   > *Prompt mới:* "Chỉ sử dụng các sự kiện đã được công bố chính thức bởi VinFast (như 175.099 xe bàn giao năm 2025, 400 xưởng dịch vụ). Nếu không có số liệu nội bộ về ticket volume hay thời gian xử lý, HÃY GHI RÕ là 'Chưa có baseline, cần đo trong pilot', tuyệt đối KHÔNG tự sáng tác con số."

2. **Thiết lập ranh giới cứng (Operational Boundaries) trong System Prompt:**
   Trong file code `prompt_prototype.py`, nhóm thiết lập các điều kiện biên nghiêm ngặt:
   - **Thẻ bắt buộc `[DRAFT_ONLY]`:** Toàn bộ văn bản do AI sinh ra phải bắt đầu bằng `[DRAFT_ONLY]` để ngăn chặn downstream API tự động bắn tin nhắn đi nếu chưa qua mắt con người.
   - **Ngưỡng an toàn vật lý (Pin < 5%):** Nếu pin xe dưới 5%, cấm tuyệt đối việc gợi ý trạm sạc cách xa trên 5km; lập tức kích hoạt mã lệnh điều xe cứu hộ sạc pin di động (`dispatch_mobile_charger`).

---

## 5. Đúc kết bài học về AI Product Scoping

1. **Problem First, AI Second:** Giá trị của người kỹ sư AI không nằm ở việc áp dụng mô hình phức tạp nhất (Agent, RAG, Fine-tuning), mà nằm ở việc xác định đúng điểm nghẽn (bottleneck) của nghiệp vụ và dũng cảm nói "KHÔNG" với AI nếu Rule-based hoặc SQL làm tốt hơn.
2. **AI là Trợ lý (Co-pilot), con người giữ trách nhiệm (Accountable):** Trong các lĩnh vực có tính an toàn cao như ô tô điện (VinFast), giao thông (Xanh SM) hay y tế (Vinmec), ranh giới bảo vệ (Safety Boundaries) và cơ chế Fallback thủ công quan trọng gấp mười lần độ thông minh của mô hình.
3. **Thái độ hoài nghi lành mạnh (Healthy Skepticism):** Luôn kiểm chứng chéo (Fact-check) mọi thông tin AI tạo ra với tài liệu thực tế của doanh nghiệp trước khi đưa ra quyết định đầu tư (Go/No-Go).
