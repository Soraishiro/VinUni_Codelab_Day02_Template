# 01 — Problem Scan
## Lab 02: AI Product Scoping — Vin Smart Future

> **Mục tiêu:** Thực hiện Phase 1 (SCAN) và Phase 2 (QUICK-ASSESS) theo worksheet.  
> **Nguyên tắc:** Problem First, AI Second. Không giả định một workflow là thủ công nếu nguồn công khai không chứng minh điều đó; không tự bịa baseline thời gian, volume ticket hoặc tỷ lệ lỗi.

---

## 0. Lọc ảo — Reality Check trước khi SCAN

Inspiration Kit chỉ là nguồn gợi ý. Trước khi đưa một ý tưởng vào SCAN, nhóm kiểm tra xem problem có thật, solution tương tự đã tồn tại chưa, và phần nào chỉ là giả định cần xác minh.

### 0.1. Ba ý tưởng loại bỏ ngay

| Ý tưởng ban đầu | Reality Check | Quyết định |
|---|---|---|
| **Vinmec — AI tóm tắt hồ sơ bệnh án** | Vinmec đã tích hợp DrAid vào quản lý hồ sơ bệnh án. Vinmec công bố thời gian tóm tắt giảm từ khoảng 5 phút xuống 1 phút, tiết kiệm đến 80%. | **Loại** — solution tương tự đã được triển khai. |
| **Vinhomes — Trợ lý cư dân ảo** | Vinhomes đã ra mắt Trợ lý ảo trên Vinhomes Resident và Vinhomes Online từ 2022, hỗ trợ tra cứu thông tin, hóa đơn, tiện ích và thủ tục. | **Loại** — product đã tồn tại. |
| **Vinhomes — Tự động route phản ánh cư dân** | Báo cáo thường niên Vinhomes cho biết VPMS đã được triển khai trên các khu đô thị, tự động giao việc, theo dõi tiến độ và tích hợp Resident App/Salesforce/CSM để xử lý phản ánh theo quy trình. | **Loại ở dạng gốc** — không nên đề xuất lại một automation đã tồn tại. |

**Kết luận Lọc ảo:** SCAN chỉ giữ các problem có workflow công khai đủ rõ hoặc có evidence trực tiếp từ mô tả công việc/quy trình chính thức. Với những phần chưa có số liệu nội bộ, nhóm đánh dấu là **baseline cần đo**, thay vì biến ước lượng thành fact.

---

# Phase 1 — SCAN

Worksheet yêu cầu tối thiểu 5 problems. Dù rubric ghi “3 lenses”, worksheet định nghĩa 4 lenses; bảng dưới sử dụng đủ các lens: **Repetitive, Time-consuming, AI-upgrade, Stakeholder Pain**.

## 1.1. Bảng quét cơ hội

| # | Subsidiary / Department | Lens | Problem thực tế sau Reality Check | Evidence / lý do giữ |
|---:|---|---|---|---|
| **1** | **VinFast — Customer Service / Aftersales** | Repetitive + Time-consuming | **Triage và routing yêu cầu khách hàng đa kênh:** đọc hiểu yêu cầu, chuẩn hóa thông tin, xác định yêu cầu có thể xử lý ngay hay phải chuyển phòng ban/đại lý. | Quy trình VinFast công khai xác nhận CSKH nhận yêu cầu từ hotline, email, website, app và thư; sau đó có bước **phân loại và chuyển xử lý**. |
| **2** | **Vinpearl — Reservation / Customer Service** | Repetitive + Time-consuming | **Pre-process yêu cầu booking không cấu trúc:** trích xuất ngày, số khách, loại dịch vụ, thay đổi/hủy, yêu cầu đặc biệt trước khi nhân viên thao tác B2B/OTA/booking system. | JD Vinpearl công khai cho thấy nhân viên tiếp nhận yêu cầu đặt vé/phòng/dịch vụ và thực hiện đặt/xuất/hủy/thay đổi qua B2B/OTA hoặc đối tác. |
| **3** | **Vinhomes — CRM / Quality Control** | Repetitive | **Phát hiện vi phạm SOP và lỗi dữ liệu CRM:** lead quá hạn, sai thao tác, thiếu cập nhật, bỏ sót bước, lỗi nhập liệu. | JD QC Vinhomes yêu cầu kiểm tra SOP, thao tác CRM, phát hiện lỗi nhập liệu, sử dụng sai chức năng hoặc không cập nhật dữ liệu đúng thời gian. |
| **4** | **VinBus — Customer Service / Operations** | Time-consuming + Stakeholder Pain | **Chuẩn hóa phản ánh hành khách thành incident ticket có cấu trúc:** sự việc, thời gian, biển số, tuyến, hướng xe, điểm dừng và bằng chứng liên quan. | VinBus công khai yêu cầu khách cung cấp chính các trường thông tin này khi phản ánh để CSKH xác minh. |
| **5** | **VinBus — Operations / ETA Quality** | AI-upgrade + Stakeholder Pain | **Phát hiện ETA bất thường khi dữ liệu xe mất kết nối:** đánh dấu trường hợp ước tính thời gian đến trạm có độ tin cậy thấp và chuyển sang fallback. | FAQ VinBus thừa nhận một số trường hợp ETA không chính xác khi xe mất kết nối nên hệ thống không nhận được vị trí/vận tốc chính xác. |

---

## 1.2. Đánh giá nhanh 5 problems

| Problem | Evidence của workflow | Giá trị tiềm năng | AI có cần thiết? | Rủi ro | Quyết định |
|---|---:|---:|---:|---:|---|
| VinFast CS triage & routing | **Cao** | **Cao** | **Cao với text tự do; Rule vẫn cần cho hard constraints** | Trung bình | **Top 3** |
| Vinpearl booking pre-processing | **Cao** | Cao | **Cao cho extraction từ text; transaction phải deterministic** | Trung bình | **Top 3** |
| Vinhomes CRM/SOP QC | **Cao** | Cao | Trung bình — phần lớn có thể Rule/SQL | Thấp | **Top 3** |
| VinBus complaint → incident ticket | Cao | Trung bình | Cao cho text structuring | Thấp | Reserve |
| VinBus ETA confidence/anomaly | Trung bình | Cao | Có thể ML/rule hơn LLM | Trung bình | Reserve |

### Vì sao chọn Top 3?

Ba problem được chọn đại diện cho ba kiểu quyết định AI Fit khác nhau:

1. **VinFast:** text đa kênh + semantic routing → có lý do mạnh để dùng **LLM Feature + Rule + HITL**.
2. **Vinpearl:** extraction từ yêu cầu tự do → **LLM Feature**, nhưng booking transaction phải deterministic.
3. **Vinhomes:** phần lớn constraint đã có cấu trúc → **Rule-first**, giúp kiểm tra xem nhóm có biết từ chối dùng LLM khi không cần thiết hay không.

---

# Phase 2 — QUICK-ASSESS

## Quick Problem Card #1 — VinFast Service Request Triage & Routing

**Bài toán (1 câu):**  
Hỗ trợ Trung tâm CSKH VinFast đọc hiểu, chuẩn hóa, ưu tiên và đề xuất tuyến xử lý cho các yêu cầu khách hàng đa kênh, trong khi quyết định chuyển xử lý cuối cùng vẫn thuộc về nhân viên CSKH.

**Công ty thành viên:** VinFast  
**Actor đang đau:** Nhân viên Trung tâm Chăm sóc Khách hàng; phòng ban phụ trách/đại lý nhận handoff; khách hàng chờ xử lý.

### Current workflow

1. Khách hàng gửi yêu cầu qua hotline/email/web chat/app/thư.
2. Trung tâm CSKH tiếp nhận và kiểm tra thông tin.
3. CSKH **phân loại yêu cầu**.
4. Nếu xử lý ngay được → tư vấn và đóng sự vụ; nếu không → chuyển phòng ban/đại lý ủy quyền.
5. Đơn vị liên quan xử lý; CSKH/phòng ban/đại lý phản hồi và xác nhận kết quả với khách hàng.

**Bottleneck giả thuyết:** Bước 2–4: hiểu nội dung tự do, nhận diện intent/mức độ ưu tiên, kiểm tra thiếu thông tin và đề xuất destination đúng.

**Thời gian hiện tại:** Chưa có baseline phút/lượt trong nguồn công khai. Đây là biến bắt buộc phải đo trên log/pilot, không tự giả định.

### AI có thể hỗ trợ ở đâu?

AI chỉ hỗ trợ **Understand → Structure → Triage → Recommend Route**:

- tóm tắt yêu cầu;
- trích xuất intent và thông tin cần thiết;
- phát hiện multi-intent / missing fields;
- gợi ý category, severity và destination;
- sinh JSON có cấu trúc cho CRM.

### Success Metrics — mục tiêu prototype/pilot

- Routing agreement với nhãn human: **≥ 95%**.
- Recall đối với case safety/critical: **≥ 99%**.
- Structured JSON hợp lệ: **100%**.
- Case confidence thấp hoặc xung đột rule được đưa sang HITL: **100%**.
- Median model inference cho một ticket: **< 10 giây**.

### Quick Architecture

**[x] Hybrid: Rule + LLM Feature + HITL**  
**[ ] Agent**

**Lý do:** Rule xử lý hard constraints, mandatory fields và safety flags; LLM xử lý semantic text; con người giữ quyền route cuối cùng.

### Stress-test nhanh

- **Điểm yếu 1:** Chưa biết tỷ lệ thao tác hiện tại đã tự động hóa đến đâu.
- **Điểm yếu 2:** Chưa có baseline ticket volume, triage time và misrouting rate.
- **Điểm yếu 3:** Sai routing ở case liên quan an toàn/bảo hành có thể gây hậu quả lớn.

**Cách khống chế:** prototype offline trước; dùng labelled dataset; mọi route chỉ là recommendation; confidence thấp bắt buộc human review.

---

## Quick Problem Card #2 — Vinpearl Reservation Request Pre-processing

**Bài toán (1 câu):**  
Tự động chuyển yêu cầu đặt/hủy/thay đổi phòng và dịch vụ từ ngôn ngữ tự do thành booking request có cấu trúc để nhân viên Reservation kiểm tra và thao tác trên hệ thống.

**Công ty thành viên:** Vinpearl  
**Actor đang đau:** Nhân viên Reservation / Customer Service.

### Current workflow

1. Khách gửi yêu cầu đặt phòng/vé/dịch vụ.
2. Nhân viên đọc và làm rõ nhu cầu.
3. Nhân viên xác định các field: ngày, số khách, loại dịch vụ, yêu cầu đặc biệt, thay đổi/hủy.
4. Nhân viên thao tác trên B2B/OTA/booking system hoặc làm việc với đối tác.
5. Theo dõi đến khi dịch vụ hoàn tất, xử lý thay đổi/khiếu nại nếu phát sinh.

**Bottleneck giả thuyết:** Bước 2–3 với input không cấu trúc hoặc chứa nhiều yêu cầu trong cùng một message.

**Thời gian hiện tại:** Không có baseline công khai; cần đo trên sample request thật.

### AI có thể hỗ trợ ở đâu?

LLM chỉ làm **information extraction + normalization**, ví dụ:

```json
{
  "check_in": "YYYY-MM-DD",
  "check_out": "YYYY-MM-DD",
  "adults": 2,
  "children": 1,
  "rooms": 1,
  "request_type": "new_booking",
  "special_requests": [],
  "missing_fields": []
}
```

### Success Metrics — mục tiêu prototype/pilot

- Exact match/F1 các mandatory booking fields: **≥ 98%**.
- JSON schema validity: **100%**.
- Yêu cầu thiếu field được flag: **≥ 99% recall**.
- Processing latency: **< 10 giây/request**.
- Autonomous booking/price confirmation: **0 trường hợp**.

### Quick Architecture

**[x] LLM Feature + Rule validation + HITL**  
**[ ] Agent**

### Stress-test nhanh

- Inventory, giá và chính sách hủy là dữ liệu động → LLM không được tự đoán.
- Extraction sai ngày/số khách có thể tạo booking sai.
- Do đó AI chỉ tạo structured draft; nhân viên và booking system giữ quyền transaction.

---

## Quick Problem Card #3 — Vinhomes CRM/SOP Quality Assurance

**Bài toán (1 câu):**  
Tự động phát hiện record CRM vi phạm SOP hoặc có lỗi dữ liệu để QC tập trung review các trường hợp bất thường thay vì kiểm tra đồng đều mọi record.

**Công ty thành viên:** Vinhomes  
**Actor đang đau:** Chuyên viên Quản lý Chất lượng (QC), Sales Ops/Marketing Ops.

### Current workflow

1. QC kiểm tra việc thực hiện SOP và các điểm chạm Sale–Marketing.
2. Kiểm tra thao tác CRM/listing/dashboard theo checklist.
3. Phát hiện lỗi nhập liệu, dùng sai chức năng, không cập nhật đúng hạn hoặc bỏ sót bước.
4. Phân loại lỗi theo mức độ.
5. Tổng hợp và báo cáo trưởng nhóm.

**Bottleneck giả thuyết:** khối lượng kiểm tra lặp lại và việc tổng hợp exception.

**Thời gian hiện tại:** Chưa có số công khai.

### AI có thể hỗ trợ ở đâu?

Phần lớn problem **không cần LLM**:

- quá hạn → SQL/Rule;
- field bắt buộc trống → Rule;
- trạng thái sai sequence → State machine;
- phân phối sai region → Rule.

LLM chỉ đáng dùng cho phần unstructured như audit note/listing description nếu có.

### Success Metrics — mục tiêu prototype/pilot

- Recall đối với seeded SOP violations: **≥ 95%**.
- False-positive rate: **≤ 5%**.
- Hard-rule checks có kết quả deterministic/reproducible: **100%**.
- Không tự sanction/khóa record: **0 trường hợp**.

### Quick Architecture

**[x] Rule / State Machine first**  
**[ ] LLM là core solution**  
**[ ] Agent**

### Stress-test nhanh

Đây là candidate tốt về business nhưng AI Fit thấp hơn hai problem trên. Nếu workflow chủ yếu là structured data + fixed SOP, Rule/SQL rẻ hơn, dễ audit hơn và ít hallucination hơn.

---

# 2. Quyết định sau QUICK-ASSESS

## Chọn bài toán cuối cùng

**VinFast Service Intelligence — AI-assisted Customer Request Triage & Routing**

### Vì sao chọn?

| Tiêu chí | VinFast Triage | Vinpearl Reservation | Vinhomes QC |
|---|---:|---:|---:|
| Workflow có evidence trực tiếp | 5/5 | 5/5 | 5/5 |
| Semantic complexity phù hợp LLM | **5/5** | 4/5 | 2/5 |
| Có chỗ rõ ràng cho Rule vs LLM | **5/5** | 4/5 | 5/5 |
| HITL / Boundary thiết kế rõ | **5/5** | 5/5 | 5/5 |
| Dễ tạo prompt prototype | **5/5** | 5/5 | 3/5 |
| Business scale | **5/5** | 4/5 | 4/5 |
| Tổng | **30/30** | **27/30** | **24/30** |

### Scope cuối cùng

**IN SCOPE**

- Understand customer free-text.
- Extract structured fields.
- Summarize.
- Classify intent/category.
- Flag safety/critical or missing information.
- Recommend responsible team/dealer.
- Return confidence + rationale for human review.

**OUT OF SCOPE**

- Không tự trả lời khiếu nại cuối cùng.
- Không chẩn đoán lỗi kỹ thuật xe.
- Không quyết định bảo hành/bồi thường.
- Không tự gửi case/đóng case nếu chưa có human approval.
- Không tự thực hiện hành động trong CRM/dealer system.
- Không thay thế escalation policy hiện hành.

---

# 3. Nguồn kiểm chứng

1. **VinFast — Quy trình tiếp nhận, phản hồi và giải quyết yêu cầu/khiếu nại khách hàng**  
   https://vinfastauto.com/vn_vi/quy-trinh-tiep-nhan-phan-hoi-thong-tin-va-giai-quyet-phan-anh-yeu-cau-khieu-nai-cua-khach-hang

2. **VinFast — 175.099 xe điện bàn giao tại Việt Nam năm 2025; 400 xưởng dịch vụ**  
   https://vinfastauto.com/vn_vi/vinfast-lap-ky-luc-ban-giao-xe-o-to-dien-tai-viet-nam-2025

3. **Vinpearl Careers — Chuyên viên Kinh doanh & CSKH (vé máy bay & khách sạn quốc tế)**  
   https://careers.vinpearl.com/job/vinpearl-head-office-chuyen-vien-kinh-doanh-cham-soc-khach-hang-ve-may-bay-khach-san-quoc-te-10386

4. **Vinhomes Careers — Chuyên viên Quản lý Chất lượng (QC)**  
   https://careers.vinhomes.vn/job/chuyen-vien-quan-ly-chat-luong-qc-10681

5. **VinBus — Liên hệ / thông tin cần cung cấp khi phản ánh**  
   https://vinbus.vn/lien-he

6. **Vinhomes Annual Report 2024 — VPMS**  
   https://vinhomes.vn/vi/bao-cao-thuong-nien

7. **Vinmec — DrAid tiết kiệm 80% thời gian xử lý hồ sơ y tế**  
   https://www.vinmec.com/vie/bai-viet/dot-pha-cong-nghe-ai-tai-vinmec-tiet-kiem-80-thoi-gian-xu-ly-ho-so-y-te

8. **Vinhomes — Trợ lý ảo trên Vinhomes Resident / Vinhomes Online**  
   https://market.vinhomes.vn/blog/ra-mat-tro-ly-ao-tren-ung-dung-vinhomes-resident-va-vinhomes-online
