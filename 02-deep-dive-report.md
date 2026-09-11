# 02 — Deep Dive Report

## VinFast Service Intelligence — Hỗ trợ phân loại và chuyển xử lý yêu cầu khách hàng

> **Phạm vi của đề xuất:** hỗ trợ Trung tâm Chăm sóc Khách hàng VinFast ở bước đọc hiểu, chuẩn hóa, phân loại và đề xuất nơi xử lý yêu cầu.  
> **Không phải mục tiêu:** xây chatbot thay thế CSKH, tự chẩn đoán xe, tự quyết định bảo hành/bồi thường, hoặc tự thao tác CRM.

---

# 0. Tổng quan về bài toán

## 0.1. Câu chuyện thực tế: bài toán xuất hiện ở đâu?

Trong năm 2025, VinFast bàn giao **175.099 ô tô điện tại Việt Nam**. Đến đầu năm 2026, hãng cho biết hệ thống hậu mãi trong nước đã đạt **400 xưởng dịch vụ**. Quy mô xe đang vận hành và mạng lưới hậu mãi tăng nhanh làm cho chất lượng phối hợp giữa Trung tâm Chăm sóc Khách hàng, phòng ban chuyên môn và các đại lý/xưởng dịch vụ trở thành một phần quan trọng của trải nghiệm sau bán hàng.

Nguồn: [VinFast lập kỷ lục bàn giao 175.099 xe ô tô điện tại Việt Nam năm 2025](https://vinfastauto.com/vn_vi/vinfast-lap-ky-luc-ban-giao-xe-o-to-dien-tai-viet-nam-2025).

Bản thân VinFast cũng đang đầu tư mạnh vào việc lắng nghe và chuẩn hóa dịch vụ hậu mãi. Tháng 10/2025, hãng thực hiện khảo sát gần **300.000 khách hàng**, tập trung vào tác phong phục vụ, tốc độ và thời gian sửa chữa, chất lượng sửa chữa và các góp ý về trải nghiệm sử dụng xe. Sang năm 2026, chương trình **“Kiến tạo dịch vụ 5 sao”** tiếp tục thu thập các phản ánh liên quan trực tiếp đến các khâu đặt hẹn, tiếp đón, tiếp nhận xe, tư vấn dịch vụ và bàn giao xe; các phản hồi hợp lệ được bộ phận chuyên trách phân tích để cải tiến dịch vụ.

Nguồn:

- [VinFast khảo sát ý kiến khách hàng — nâng cao chất lượng dịch vụ](https://vinfastauto.com/vn_vi/vinfast-khao-sat-y-kien-khach-hang-nang-cao-chat-luong-dich-vu)
- [Chương trình Kiến tạo dịch vụ 5 sao cùng VinFast](https://vinfastauto.com/vn_vi/chuong-trinh-kien-tao-dich-vu-5-sao-cung-vinfast)
- [Giai đoạn 2 chương trình Kiến tạo dịch vụ 5 sao](https://vinfastauto.com/vn_vi/vinfast-tiep-tuc-trien-khai-chuong-trinh-kien-tao-dich-vu-5-sao-dong-nhat-chuan-dich-vu-nang-tam-trai-nghiem-khach-hang)

Điểm quan trọng hơn nằm ở **quy trình chính thức xử lý yêu cầu và khiếu nại**. VinFast công khai rằng khách hàng có thể liên hệ qua hotline, email, website, ứng dụng VinFast hoặc thư. Sau khi tiếp nhận, Trung tâm Chăm sóc Khách hàng thực hiện một bước nghiệp vụ rất rõ: **phân loại yêu cầu**. Yêu cầu nào có thể giải đáp ngay sẽ được xử lý tại CSKH; yêu cầu chưa thể xử lý ngay sẽ được chuyển tới **phòng ban phụ trách hoặc đại lý ủy quyền**. Sau đó, CSKH và đơn vị liên quan tiếp tục phản hồi, xác nhận phương án và kết quả xử lý với khách hàng.

Nguồn: [Quy trình tiếp nhận, phản hồi thông tin và giải quyết phản ánh, yêu cầu, khiếu nại của khách hàng — VinFast](https://vinfastauto.com/vn_vi/quy-trinh-tiep-nhan-phan-hoi-thong-tin-va-giai-quyet-phan-anh-yeu-cau-khieu-nai-cua-khach-hang). Nội dung được VinFast cập nhật bổ sung ngày 27/01/2026.

Quy trình dịch vụ sửa chữa còn đặt ra yêu cầu vận hành chặt hơn: sau khi xe ra xưởng, khách hàng được gọi để ghi nhận phản hồi trong vòng 2 ngày; với phản ánh hoặc khiếu nại liên quan dịch vụ sửa chữa, VinFast nêu mục tiêu **phản hồi về giải pháp muộn nhất trong ngày T+1**.

Nguồn: [Quy trình dịch vụ sửa chữa VinFast](https://vinfastauto.com/vn_vi/dich-vu-sua-chua).

Từ các nguồn trên, vấn đề đáng nghiên cứu không phải là “VinFast chưa có hệ thống CSKH” hay “nhân viên đang phân loại hoàn toàn thủ công”. Không có dữ liệu công khai nào cho phép kết luận như vậy.

**Vấn đề thực sự là:** bước phân loại và chuyển xử lý là một **điểm ra quyết định** nằm giữa nhiều kênh khách hàng và nhiều đơn vị hậu mãi. Khi quy mô khách hàng và mạng lưới dịch vụ tăng, chất lượng của bước này ảnh hưởng trực tiếp đến việc yêu cầu có đi đúng nơi, có được ưu tiên đúng trường hợp, có đủ thông tin để đơn vị sau xử lý, và có giữ được cam kết phản hồi hay không.

Đây là nơi nhóm đặt giả thuyết:

> **Có thể dùng AI như một lớp hỗ trợ cho nhân viên CSKH để đọc hiểu, chuẩn hóa và đề xuất hướng phân loại yêu cầu nhanh và nhất quán hơn, nhưng vẫn giữ quyền quyết định cuối cùng ở con người hay không?**

---

## 0.2. Điều đã biết và điều chưa biết

Để tránh biến giả thuyết thành “sự thật”, báo cáo phân biệt rõ hai lớp thông tin.

**Đã có căn cứ công khai:** VinFast tiếp nhận yêu cầu đa kênh; Trung tâm CSKH thực hiện bước phân loại; có nhánh xử lý ngay và nhánh chuyển tới phòng ban/đại lý; một số trường hợp cần ưu tiên; hoạt động hậu mãi có yêu cầu phản hồi theo thời hạn; quy mô khách hàng và mạng lưới dịch vụ đang tăng nhanh.

**Chưa có dữ liệu công khai:** số yêu cầu mỗi ngày, tỷ lệ từng kênh, thời gian trung bình để phân loại một yêu cầu, tỷ lệ chuyển sai đơn vị, tỷ lệ yêu cầu phải chuyển lại lần hai, công cụ CRM hiện tại, mức độ tự động hóa đã có, hay chi phí vận hành của bước phân loại.

Vì vậy, các con số về hiệu quả trong báo cáo dưới đây được ghi là **mục tiêu thử nghiệm**, không phải số liệu hiện trạng của VinFast.

---

# 1. Phát biểu bài toán — 6 trường

| Field                       | Nội dung                                                                                                                                                                                                                                                                                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1. Actor / Operator**     | Nhân viên tuyến đầu của Trung tâm Chăm sóc Khách hàng VinFast, là người tiếp nhận yêu cầu và quyết định xử lý ngay hay chuyển tới phòng ban/đại lý phù hợp. Các đơn vị hậu mãi và đại lý là bên nhận handoff.                                                                                                                              |
| **2. Current Workflow**     | Khách hàng gửi yêu cầu qua hotline, email, website, VinFast App hoặc thư → CSKH tiếp nhận và kiểm tra thông tin → phân loại → xử lý ngay hoặc chuyển tới phòng ban/đại lý → đơn vị liên quan xử lý → phản hồi/xác nhận kết quả với khách hàng.                                                                                             |
| **3. Bottleneck**           | Điểm cần nghiên cứu là bước biến một nội dung khách hàng không theo mẫu thành một “case” đủ rõ để xử lý: vấn đề gì, thiếu thông tin gì, mức độ ưu tiên ra sao, có rơi vào nhóm cần xử lý đặc biệt hay không, và nên chuyển cho ai. Đây là **bottleneck giả thuyết**, cần xác nhận bằng dữ liệu nội bộ.                                     |
| **4. Business Impact**      | Nếu phân loại hoặc handoff không tốt, hậu quả có thể là chuyển vòng, phải đọc và giải thích lại, tăng thời gian xử lý và gây áp lực lên SLA. Tác động đặc biệt đáng quan tâm trong bối cảnh 175.099 xe được bàn giao trong 2025, mạng lưới 400 xưởng dịch vụ và các cam kết phản hồi hậu mãi.                                              |
| **5. Success Metric**       | Prototype chỉ đạt yêu cầu nếu: đề xuất đúng nơi xử lý **≥95%** trên tập dữ liệu có nhãn; phát hiện case cần ưu tiên/an toàn **≥99% recall**; **100%** case không chắc chắn được đẩy sang người xử lý; đầu ra hợp lệ **100%**; pilot phải giảm **≥30%** thời gian phân loại trung vị mà không làm xấu SLA hoặc tăng tỷ lệ chuyển lại.       |
| **6. Operational Boundary** | AI chỉ được tóm tắt, trích xuất thông tin, phân loại, phát hiện thiếu dữ liệu, gợi ý mức ưu tiên và nơi xử lý. AI không được tự gửi phản hồi cuối cùng cho khách, tự chẩn đoán xe, quyết định bảo hành/bồi thường, tự xác định tư cách pháp lý của khách, tự đóng case hoặc tự thay đổi/chuyển case trên hệ thống nếu chưa có người duyệt. |

---

# 2. Actor / Operator — từ “người phân loại” sang “người xử lý ngoại lệ”

Ở **quy trình hiện tại**, actor chính vẫn là nhân viên Trung tâm Chăm sóc Khách hàng VinFast. Họ là người đứng tại điểm vào của quy trình: tiếp nhận yêu cầu, hiểu vấn đề, xác định cần hỏi thêm gì, quyết định có thể xử lý ngay hay phải chuyển sang phòng ban/đại lý.

Nhưng nếu Future-State vẫn bắt nhân viên **đọc lại và bấm duyệt 100% case**, AI chỉ giúp “soạn hộ vài dòng” và giá trị kinh doanh sẽ rất hạn chế. Đó không phải đích đến của đề xuất này.

Mục tiêu của Future-State là thay đổi **vai trò vận hành**:

> **Con người không còn là “routing engine” cho mọi yêu cầu. AI xử lý thẳng các case thường gặp, ít rủi ro và đủ chắc chắn; con người tập trung vào ngoại lệ, case nhạy cảm và quyết định chuyên môn.**

Nói cách khác, AI không thay CSKH; nó thay phần công việc **chuẩn bị và điều phối lặp lại** mà CSKH hiện phải thực hiện trước khi đi tới phần cần judgment.

## 2.1. Ba loại công việc cần tách ra

### A. Công việc có thể tự động hóa gần như hoàn toàn

Đây là các tác vụ có cấu trúc và rủi ro thấp:

- đọc nội dung khách gửi từ email/chat/app;
- nhận diện loại vấn đề;
- trích xuất VIN, dòng xe, thời gian, địa điểm, xưởng liên quan nếu khách đã cung cấp;
- kiểm tra trường thông tin bắt buộc;
- hỏi lại khách các thông tin còn thiếu theo mẫu đã được phê duyệt;
- gắn category/subcategory;
- đối chiếu destination với bảng phân công trách nhiệm;
- tạo case hoàn chỉnh;
- chuyển vào đúng hàng đợi xử lý nếu case nằm trong danh sách được phép tự động.

Với nhóm này, **không cần con người duyệt từng case**. Con người chỉ giám sát qua sampling, dashboard và audit.

### B. Công việc AI chuẩn bị, con người quyết định

Ví dụ:

- một yêu cầu chứa nhiều vấn đề cùng lúc;
- AI xác định được 2 destination có khả năng ngang nhau;
- khách đang rất bức xúc và có nguy cơ escalation;
- thông tin đủ để phân loại nhưng chưa đủ để ra quyết định về bảo hành/chính sách;
- case có dấu hiệu bất thường nhưng chưa tới mức critical.

AI vẫn phải đọc, tóm tắt, trích xuất và đề xuất trước. Nhân viên chỉ xử lý **điểm quyết định còn lại**, thay vì bắt đầu từ một email thô.

### C. Công việc phải giữ ở con người/chuyên gia

Các trường hợp liên quan tới:

- an toàn xe;
- chẩn đoán kỹ thuật;
- bảo hành, bồi thường, hoàn tiền;
- tranh chấp/khiếu nại phức tạp;
- quyết định pháp lý;
- trường hợp khách hàng thuộc nhóm cần ưu tiên đặc biệt;
- case ngoài taxonomy hoặc AI không đủ căn cứ.

Với nhóm này, AI chỉ đóng vai trò **chuẩn bị hồ sơ và chuyển đúng chuyên gia**, không được ra quyết định cuối cùng.

## 2.2. Actor trong Future-State

Future-State có ba actor rõ ràng:

1. **AI Triage Agent** — xử lý các bước chuẩn hóa, hỏi bổ sung, phân loại, tạo case và tự route đối với nhóm low-risk được phép.
2. **Policy / Rule Layer** — kiểm soát các điều kiện cứng: loại case nào được auto-route, trường nào bắt buộc, ngưỡng tin cậy, SLA, escalation.
3. **CSKH / Specialist** — xử lý exception, case rủi ro và quyết định chuyên môn.

Đây mới là mô hình tạo ra ROI: **human effort được chuyển từ triage sang resolution**.

Một benchmark bên ngoài cho thấy mô hình này có thể tạo ra giá trị đáng kể khi dữ liệu và workflow đủ trưởng thành. ServiceNow công bố case C Spire, nơi hơn 70% email case được agentic AI xử lý qua triage/routing, thời gian triage giảm 44% và khoảng 280 giờ lao động mỗi tháng được giải phóng. Một case khác tại Rossmann báo cáo 89% ticket được tự động phân loại/ưu tiên, routing accuracy 98% và chi phí lao động trên các case do AI xử lý giảm 50%. Đây là **benchmark tham khảo từ vendor case study, không phải dự báo cho VinFast**, nhưng nó chứng minh rằng “exception-based human review” là một mô hình vận hành có thật chứ không chỉ là demo AI.

Nguồn tham khảo benchmark:

- https://www.servicenow.com/au/customers/cspire.html
- https://www.servicenow.com/customers/rossmann.html

# 3. Current Workflow — quy trình hiện tại cần hiểu như thế nào?

## 3.1. Luồng chính đã được VinFast công khai

```text
Khách hàng
Hotline / Email / Website / App / Thư
        │
        ▼
Trung tâm CSKH tiếp nhận
- ghi nhận yêu cầu
- yêu cầu bổ sung thông tin/tài liệu nếu cần
        │
        ▼
PHÂN LOẠI
        │
        ├── Có thể giải đáp ngay
        │       └── CSKH tư vấn / giải đáp / đóng sự vụ
        │
        └── Chưa thể xử lý ngay
                └── chuyển Phòng ban phụ trách / Đại lý ủy quyền
                        │
                        ▼
                   Xử lý chuyên môn
                        │
                        ▼
           Phản hồi / xác nhận kết quả với khách
```

Điểm đáng chú ý là VinFast không mô tả đây như một luồng “ticket tự chạy”. Họ mô tả nó như một **quy trình trách nhiệm**: ai tiếp nhận, khi nào chuyển, ai phản hồi và khi nào xác nhận kết quả.

Trong phạm vi dịch vụ sửa chữa, luồng này còn gắn với trải nghiệm thực địa: đặt hẹn, tiếp nhận xe, sửa chữa, bàn giao và chăm sóc sau sửa chữa. Phản ánh sau sửa chữa không phải một nội dung độc lập; nó có thể cần liên kết với lịch hẹn, xưởng đã phục vụ, hạng mục sửa chữa, phát sinh, báo giá và kết quả bàn giao.

Đó là lý do nếu làm sản phẩm thật, AI không thể chỉ nhìn một câu chat rồi “đoán phòng ban”. Nó cần được đánh giá trong bối cảnh **case management**.

---

## 3.2. Những nhánh nghiệp vụ quan trọng

### A. Case có thể trả lời ngay

Đây là các yêu cầu mà tuyến đầu có đủ căn cứ để tư vấn hoặc cung cấp thông tin. Nếu AI hỗ trợ, mục tiêu không phải sáng tạo câu trả lời mới mà là giúp nhân viên nhận biết đúng đây là loại case tuyến đầu được phép xử lý.

### B. Case cần chuyển chuyên môn

Đây là trọng tâm của đề xuất. AI phải giúp nhân viên trả lời được hai câu hỏi: “case này thuộc loại gì?” và “đơn vị nào là nơi xử lý đúng?”. Tuy nhiên, AI chỉ được **đề xuất**, không được tự chuyển.

### C. Case thiếu thông tin

Một case chưa đủ VIN, bằng chứng, địa điểm, mốc thời gian hoặc nội dung cần xác minh thì route ngay có thể chỉ chuyển phần thiếu dữ liệu sang cho người khác. Trong trường hợp này, AI nên ưu tiên phát hiện **missing information** trước khi nghĩ tới destination.

### D. Case nhạy cảm / cần ưu tiên

Quy trình VinFast dành riêng một phần cho người tiêu dùng dễ bị tổn thương và nêu rõ các trường hợp này được ưu tiên tiếp nhận/xử lý khi khách hàng cung cấp thông tin chứng minh phù hợp. Điều này làm thay đổi thiết kế: AI **không được tự suy đoán** khách thuộc nhóm dễ bị tổn thương dựa trên tên, tuổi đoán từ cách viết hoặc các thuộc tính nhạy cảm. Hệ thống chỉ được đánh dấu dựa trên thông tin khách đã khai báo hoặc dữ liệu nghiệp vụ đã được phép sử dụng.

Các vấn đề an toàn xe, khiếu nại nghiêm trọng, bảo hành/bồi thường cũng cần escalation thay vì để AI tự kết luận.

---

# 4. Bottleneck — điểm nghẽn thật sự nằm ở đâu?

Nếu chỉ nhìn bề mặt, ta có thể gọi đây là bài toán “phân loại ticket”. Cách gọi đó quá đơn giản và dễ dẫn tới một giải pháp sai.

Điểm khó thực sự là **chuẩn hóa một yêu cầu không có cấu trúc thành một case nghiệp vụ có thể hành động**.

Ví dụ giả định:

> “Xe em vừa lấy tuần trước, sáng nay báo lỗi pin, app cũng không cập nhật trạng thái. Em gọi xưởng gần nhà thì bảo chưa thấy lịch, trong khi mai em cần đi tỉnh. Trường hợp này bảo hành thế nào và giờ em phải làm gì?”

Một câu như vậy có ít nhất bốn lớp:

- triệu chứng kỹ thuật;
- vấn đề ứng dụng;
- vấn đề đặt/xác nhận lịch dịch vụ;
- câu hỏi về bảo hành.

Nếu hệ thống chỉ chọn một nhãn duy nhất, nó có thể làm mất thông tin. Nếu tự đưa ra kết luận bảo hành, nó vượt quyền. Nếu chuyển thẳng cho một xưởng mà chưa có đủ thông tin xe/lịch sử, nó có thể tạo thêm vòng trao đổi.

Vì vậy, bài toán nên được tách thành chuỗi quyết định:

```text
Đọc nội dung
    ↓
Nhận diện một hay nhiều ý định
    ↓
Trích xuất dữ kiện đã có
    ↓
Phát hiện dữ kiện còn thiếu
    ↓
Đánh dấu case cần ưu tiên / cần chuyên gia
    ↓
Đề xuất hướng xử lý
    ↓
Con người xác nhận
```

**Giả thuyết cần kiểm chứng bằng dữ liệu:** thời gian và lỗi không nhất thiết nằm ở “đọc câu chữ”, mà có thể nằm ở taxonomy chưa thống nhất, thông tin đầu vào thiếu, mapping trách nhiệm giữa các đơn vị, hoặc case nhiều ý định. Nếu nguyên nhân chính là mapping nghiệp vụ chưa rõ, thêm LLM sẽ không chữa được. Đây là một trong những câu hỏi phải trả lời trước pilot.

---

# 5. Business Impact — doanh nghiệp thực sự mất gì nếu bước này không tốt?

Không có dữ liệu nội bộ nên báo cáo không tự đặt ra con số “mỗi ngày mất X giờ” hoặc “tổn thất Y tỷ”.

Thay vào đó, Business Impact được đo bằng các biến vận hành có thể kiểm chứng.

## 5.1. Chi phí xử lý lại

Nếu một case bị chuyển sai, ít nhất một người ở đơn vị nhận phải đọc lại, xác định không thuộc phạm vi của mình và chuyển tiếp. CSKH hoặc khách hàng có thể phải bổ sung thông tin lần nữa.

Công thức cần đo khi có dữ liệu:

**Rework hours = số case × tỷ lệ chuyển lại × thời gian xử lý lại trung bình.**

Đây là chi phí vận hành trực tiếp và dễ đo hơn một con số doanh thu suy diễn.

## 5.2. Rủi ro SLA

VinFast cam kết thông báo đã tiếp nhận trong 01 ngày làm việc. Với dịch vụ sửa chữa, phản ánh/khiếu nại được phản hồi về giải pháp muộn nhất trong ngày T+1.

Do đó, nếu triage hoặc handoff chiếm quá nhiều thời gian, phần thời gian còn lại dành cho đơn vị chuyên môn sẽ bị thu hẹp. Chỉ số nên theo dõi là:

**% case chạm hoặc vượt SLA do thời gian nằm ở trạng thái “chờ phân loại/chờ chuyển đúng nơi”.**

## 5.3. Customer effort

Khách hàng thường không quan tâm nội bộ có bao nhiêu phòng ban. Họ cảm nhận chất lượng qua việc có phải gọi lại, kể lại, gửi lại bằng chứng hoặc bị chuyển nhiều lần hay không.

Các chỉ số phù hợp:

- số lần chuyển đơn vị trên một case;
- tỷ lệ khách phải cung cấp lại thông tin;
- tỷ lệ liên hệ lại trong X ngày cho cùng một vấn đề;
- tỷ lệ case mở lại.

## 5.4. Tính nhất quán khi quy mô tăng

Năm 2025 VinFast tăng mạnh doanh số, cuối năm đạt mạng lưới 400 xưởng dịch vụ; cùng lúc hãng mở rộng các chương trình khảo sát và tiêu chuẩn dịch vụ hậu mãi. Bài toán vì vậy không chỉ là tiết kiệm vài giây cho một ticket, mà là giữ cách hiểu và chuyển case **nhất quán** khi có nhiều kênh, nhiều đơn vị và nhiều loại yêu cầu.

---

# 6. Success Metric — đo giá trị đủ lớn để doanh nghiệp trả tiền

Nếu chỉ đo classification accuracy, proposal chưa chứng minh được business value. Hệ thống phải chứng minh **giảm human touch mà không làm xấu chất lượng dịch vụ**.

## 6.1. North-star metric

> **Straight-through triage rate:** tỷ lệ case đủ điều kiện được AI hoàn thiện và route đúng mà không cần con người chạm vào bước triage.

Mục tiêu pilot đề xuất:

- **≥60%** case thuộc nhóm low-risk đủ điều kiện được xử lý thẳng;
- trên các case auto-route, routing accuracy **≥97%**;
- case nhạy cảm/critical recall **≥99%**;
- **100%** case dưới ngưỡng confidence được chuyển sang human lane.

Mốc 60% là mục tiêu thử nghiệm cần hiệu chỉnh theo dữ liệu VinFast, không phải dự báo. Benchmark bên ngoài cho thấy C Spire đã tự động hóa hơn 70% email triage; Rossmann công bố 89% incoming ticket được tự động phân loại/ưu tiên. Các số này chỉ dùng để chứng minh mô hình vận hành có tính khả thi ở enterprise khác, không dùng để tính ROI VinFast.

## 6.2. Human effort returned

Đo trực tiếp:

**Hours returned = số case × (thời gian triage baseline − thời gian human touch sau AI).**

Mục tiêu pilot:

- giảm **≥50% human minutes** dành cho triage trên nhóm case đủ điều kiện;
- giảm **≥30% median triage latency** trên toàn bộ pilot.

## 6.3. Chất lượng handoff

- giảm **≥20%** reassignment/transfer rate so với baseline;
- giảm tỷ lệ case thiếu thông tin khi tới đơn vị xử lý;
- không tăng reopen rate;
- không làm xấu SLA.

## 6.4. Adoption của nhân viên

Với Lane B:

- tỷ lệ nhân viên chấp nhận đề xuất AI mà không sửa;
- loại chỉnh sửa thường gặp;
- thời gian từ lúc mở case tới quyết định;
- tỷ lệ “AI không giúp gì / phải đọc lại từ đầu”.

Nếu AI accuracy cao nhưng nhân viên vẫn mất gần như cùng thời gian, hệ thống không đạt mục tiêu.

## 6.5. Unit economics

Khi có dữ liệu thật, stakeholder cần thấy:

```text
Giá trị tiết kiệm
= human hours returned × fully-loaded labor cost
+ chi phí rework tránh được
+ giá trị SLA/customer-effort cải thiện

Chi phí hệ thống
= model usage + integration + operations + governance
```

Chỉ khi giá trị trên **vượt đáng kể** chi phí hệ thống ở volume thật mới có lý do mở rộng.

# 7. Operational Boundary — tự động hóa theo mức rủi ro, không duyệt tay 100%

Ranh giới của hệ thống không nên được thiết kế theo kiểu “AI làm gì cũng phải có người bấm OK”. Nếu làm vậy, doanh nghiệp vẫn phải trả chi phí con người cho hầu hết workflow và AI chỉ tạo thêm một màn hình trung gian.

Thiết kế phù hợp hơn là **risk-tiered autonomy**: mức tự động hóa tăng hoặc giảm theo loại case, độ chắc chắn và hậu quả nếu sai.

## 7.1. Lane A — Straight-through processing

**Mục tiêu:** xử lý tự động từ đầu tới bước route đối với case đơn giản, thường gặp và ít rủi ro.

Điều kiện ví dụ:

- category thuộc allow-list;
- intent rõ;
- đủ trường bắt buộc;
- destination duy nhất theo rule;
- không có cờ safety/legal/warranty/compensation;
- confidence vượt ngưỡng;
- không có xung đột giữa LLM và rule.

AI được phép:

1. đọc yêu cầu;
2. trích xuất thông tin;
3. hỏi bổ sung dữ liệu còn thiếu bằng mẫu cho phép;
4. tạo case;
5. gán category/subcategory;
6. route tới queue phù hợp;
7. gửi acknowledgement mang tính hành chính nếu template đã được duyệt.

**Không cần human approval từng case.**

Human kiểm soát thông qua audit sample, dashboard và ngưỡng tự động hóa.

## 7.2. Lane B — Assisted decision

Áp dụng khi case có độ phức tạp trung bình.

AI thực hiện toàn bộ phần chuẩn bị:

- summary;
- intents;
- facts;
- missing fields;
- customer history/context nếu được phép;
- suggested destination;
- lý do;
- policy flags.

Nhân viên chỉ cần kiểm tra điểm còn mơ hồ và chọn **Approve / Correct / Escalate**.

Mục tiêu của lane này là rút một workflow “đọc từ đầu và tự tìm hiểu” thành một quyết định ngắn.

## 7.3. Lane C — Mandatory human handling

Bắt buộc chuyển người khi:

- liên quan an toàn;
- bảo hành/bồi thường/hoàn tiền;
- tranh chấp;
- cần chẩn đoán kỹ thuật;
- khách hàng cần ưu tiên đặc biệt;
- destination không rõ;
- case ngoài taxonomy;
- confidence thấp;
- dữ liệu mâu thuẫn;
- prompt/user input cố tình yêu cầu bỏ qua policy.

AI vẫn được phép chuẩn bị hồ sơ, nhưng không được tự thực hiện quyết định có hậu quả.

## 7.4. Những quyền AI không bao giờ có trong scope đề xuất

Dù Lane A có tự động hóa cao, AI vẫn không được:

- kết luận xe hỏng vì nguyên nhân kỹ thuật cụ thể;
- quyết định bảo hành, đổi xe, hoàn tiền hoặc bồi thường;
- tạo kết luận pháp lý;
- thay đổi nội dung hồ sơ lịch sử để “khớp” với phán đoán của model;
- bỏ qua rule/allow-list;
- tự hạ mức độ nghiêm trọng để đạt ngưỡng auto-route.

Điểm mấu chốt là:

> **Tự động hóa workflow không đồng nghĩa với tự động hóa judgment.**

# 8. Phương pháp đề xuất

Nếu chỉ dùng LLM để “đề xuất một nhãn” rồi yêu cầu con người duyệt tất cả, lợi ích sẽ nhỏ. Bài toán có tiềm năng hơn khi nhìn nó như một **workflow orchestration problem**: hệ thống phải đi từ yêu cầu thô tới một case đủ dữ liệu, được phân loại và được đưa vào đúng luồng xử lý.

Vì vậy, AI Fit tốt nhất ở Future-State không còn là “LLM Feature đơn lẻ”, mà là:

> **Constrained Agentic Loop + Rule / State Machine + Human Exception Handling**

Từ “Agentic” ở đây không có nghĩa là trao toàn quyền cho AI. Nó có nghĩa AI được phép thực hiện **một chuỗi tác vụ nhiều bước có giới hạn**, gọi các công cụ đã được cấp quyền, tự kiểm tra trạng thái và dừng/escalate theo policy.

## 8.1. AI-Fit Matrix

| Thành phần nghiệp vụ                          |  Rule / State Machine |           LLM Feature |             Constrained Agentic Loop | Quyết định                 |
| --------------------------------------------- | --------------------: | --------------------: | -----------------------------------: | -------------------------- |
| Kiểm tra trường bắt buộc                      |       **Rất phù hợp** |             Không cần |                      Có thể gọi rule | **Rule**                   |
| Kiểm tra SLA / escalation policy              |       **Rất phù hợp** | Không nên tự suy diễn |                 Agent phải tuân theo | **Rule**                   |
| Hiểu nội dung tự do                           |                   Yếu |       **Rất phù hợp** |                      **Rất phù hợp** | **LLM trong Agent**        |
| Tách nhiều intent                             |           Khó mở rộng |       **Rất phù hợp** |                      **Rất phù hợp** | **LLM trong Agent**        |
| Tìm dữ liệu còn thiếu                         |  Có thể rule một phần |           **Phù hợp** |    **Rất phù hợp** vì có thể hỏi lại | **Agent**                  |
| Hỏi khách bổ sung thông tin                   | Cứng nếu chỉ template |             Soạn được | **Phù hợp nhất** vì có feedback loop | **Agent có template/rule** |
| Tra cứu knowledge / policy / customer context |         Rule không đủ |    Có thể đọc context |           **Phù hợp** qua tool calls | **Agent**                  |
| Tạo case và route low-risk                    |   Rule định tuyến tốt |           Chỉ đề xuất |        **Phù hợp** nếu có allow-list | **Agent + Rule gate**      |
| Case nhạy cảm                                 |     Rule phát hiện cờ |  LLM hỗ trợ nhận diện |                      Agent phải dừng | **Human**                  |
| Quyết định bảo hành/bồi thường                |                 Không |                 Không |                                Không | **Human / chuyên gia**     |

## 8.2. Vì sao không dừng ở LLM Feature?

Một LLM Feature có thể đọc email và trả về:

```json
{
  "category": "service_issue",
  "destination": "workshop_support"
}
```

Nhưng nếu sau đó nhân viên vẫn phải:

- đọc email gốc;
- tìm VIN;
- kiểm tra lịch sử;
- hỏi lại khách;
- bổ sung missing fields;
- chọn queue;
- tạo case;
- chuyển case;

thì AI chỉ giải được một lát rất nhỏ của quy trình.

Stakeholder khó có lý do bỏ tiền cho một hệ thống chỉ “gợi ý category”.

## 8.3. Giá trị của Agentic Loop nằm ở đâu?

Agent xử lý một vòng công việc hoàn chỉnh:

```text
Nhận yêu cầu
    ↓
Hiểu intent
    ↓
Kiểm tra dữ liệu đã đủ chưa?
    ├── Chưa → hỏi bổ sung / lấy dữ liệu được phép
    └── Đủ
          ↓
Tra policy + taxonomy + destination map
          ↓
Đánh giá risk + confidence
          ↓
Lane A: tự tạo & route case
Lane B: chuẩn bị đầy đủ → người duyệt
Lane C: chuyển chuyên gia ngay
          ↓
Theo dõi trạng thái handoff
          ↓
Nếu không được nhận / gần SLA → escalation theo rule
```

Đây mới là vòng lặp có khả năng loại bỏ phần lớn “triage work” khỏi con người.

## 8.4. Future-State Flow

Ký hiệu:

- 🔵 **AI Step**
- 🟢 **Human Step**
- ↩️ **Fallback**

```text
KHÁCH HÀNG
Hotline / Email / Web / App
        │
        ▼
[1] Chuẩn hóa đầu vào
        │
        ▼
🔵 [2] AI Agent hiểu yêu cầu
- intents
- facts
- missing information
- initial risk
        │
        ▼
[3] Rule Gate
- policy
- SLA
- allow-list
- forbidden actions
        │
        ▼
🔵 [4] Agent lấy thêm context nếu cần
- knowledge/policy
- customer/service context được phép
- hỏi khách bổ sung field thiếu
        │
        ▼
🔵 [5] Agent tạo case hoàn chỉnh
- summary
- category/subcategory
- priority
- destination
- confidence
        │
        ▼
        ┌─────────────────────────────────────┐
        │                                     │
        ▼                                     ▼
LANE A — LOW RISK                    LANE B/C — EXCEPTION
High confidence                      Ambiguous / sensitive
        │                                     │
        ▼                                     ▼
🔵 AUTO-ROUTE                       🟢 HUMAN REVIEW / SPECIALIST
Không cần duyệt tay từng case         AI đã chuẩn bị toàn bộ context
        │                                     │
        └────────────────┬────────────────────┘
                         ▼
                 ĐƠN VỊ XỬ LÝ
                         │
                         ▼
🔵 [6] Theo dõi handoff/SLA
                         │
              ┌──────────┴─────────┐
              │                    │
              ▼                    ▼
         Bình thường          Gần SLA / lỗi
                                  │
                                  ▼
                           ↩️ Escalation /
                           manual fallback
```

## 8.5. Human-in-the-loop được đặt ở đâu?

Human-in-the-loop không có nghĩa là “mọi case đều phải bấm duyệt”.

Trong proposal này:

- **Lane A:** không có human approval từng case; human-on-the-loop thông qua audit và monitoring.
- **Lane B:** human-in-the-loop ở điểm quyết định mơ hồ.
- **Lane C:** human bắt buộc vì nghiệp vụ/rủi ro.
- **Fallback:** human tiếp quản khi agent hoặc dependency lỗi.

Đây là thiết kế vừa đạt yêu cầu kiểm soát rủi ro, vừa cho phép automation tạo ROI.

Salesforce đã hỗ trợ mô hình case classification/routing theo confidence threshold: khi dự đoán vượt ngưỡng, hệ thống có thể tự cập nhật field rồi chạy assignment/routing rules; khi không đủ điều kiện có thể chuyển sang service rep. Điều này cho thấy pattern “confidence-gated automation + escalation” là một pattern vận hành phổ biến, không phải ý tưởng lý thuyết.

Nguồn:

- https://help.salesforce.com/s/articleView?id=service.cc_service_rules.htm
- https://help.salesforce.com/s/articleView?id=ai.service_agent_email_routing.htm

## 8.6. Fallback phải giữ dịch vụ chạy được

Fallback có bốn lớp:

1. **Agent unavailable / timeout:** đưa thẳng case vào queue hiện tại.
2. **Không đủ dữ liệu:** agent hỏi bổ sung; nếu không thu thập được → human queue.
3. **Không đủ confidence:** không auto-route.
4. **Case nhạy cảm:** bypass automation và chuyển specialist.

Điều này bảo đảm AI có thể bị tắt mà dịch vụ không dừng.

# 9. Kế hoạch kiểm chứng trước khi đề xuất triển khai thật

Nội dung này là phần nối giữa “ý tưởng hay” và “đề xuất có thể mang tới doanh nghiệp”.

## Giai đoạn A — Hiểu quy trình thật

Trước khi build sâu, cần phỏng vấn/quan sát CSKH và lấy một mẫu case đã ẩn dữ liệu cá nhân để trả lời:

- taxonomy thực tế là gì;
- destination thật gồm những đơn vị nào;
- một case có thể multi-label hay không;
- trường dữ liệu tối thiểu của từng loại case;
- SLA từng loại;
- case nào bắt buộc escalation;
- tool hiện tại đã tự động hóa những gì.

Nếu bước này cho thấy phần lớn routing đã được tự động hóa tốt, scope phải đổi. Không được xây thêm AI chỉ vì đã chọn đề tài.

## Giai đoạn B — Tạo tập đánh giá từ dữ liệu thật

Đề xuất lấy **500–1.000 case lịch sử** đã đóng, được ẩn dữ liệu nhạy cảm và lấy mẫu theo kênh/loại vấn đề.

Mỗi case cần có ground truth:

- destination cuối cùng;
- intent;
- các field bắt buộc;
- case có phải escalation không;
- lịch sử chuyển lại nếu có.

Các case mơ hồ nên được hai người nghiệp vụ gán nhãn độc lập. Nếu chính người nghiệp vụ cũng bất đồng cao, đó là dấu hiệu taxonomy cần sửa trước khi đổ lỗi cho AI.

## Giai đoạn C — So sánh ba baseline

Không chỉ chạy một LLM rồi báo accuracy.

Cần so:

1. **Rule-only baseline**
2. **LLM-only baseline**
3. **Hybrid Rule + LLM**

Nếu Rule-only đã gần bằng Hybrid, nên ưu tiên Rule vì dễ kiểm soát và rẻ hơn.

## Giai đoạn D — Shadow Mode

AI chạy trên case thật nhưng **không ảnh hưởng quyết định**. Nhân viên vẫn làm như bình thường.

Sau mỗi case, so đề xuất AI với quyết định thực tế:

- agreement;
- sai category;
- sai destination;
- bỏ sót missing field;
- bỏ sót escalation;
- confidence calibration.

Shadow Mode cho biết model có đủ tốt trước khi nhân viên nhìn thấy đề xuất của nó.

## Giai đoạn E — Pilot có Human-in-the-loop

Chỉ khi shadow đạt gate mới cho một nhóm nhỏ nhân viên sử dụng gợi ý AI.

Pilot phải đo đồng thời:

- thời gian xử lý;
- tỷ lệ nhân viên sửa AI;
- lý do sửa;
- số lần chuyển lại;
- SLA;
- case mở lại.

Nếu thời gian giảm nhưng tỷ lệ chuyển lại tăng, pilot thất bại.

---

# 10. Phase 5 — Evaluate

## AI Readiness Checklist

| Câu hỏi                                                | Trạng thái hiện tại | Nhận định                                                                                       |
| ------------------------------------------------------ | ------------------- | ----------------------------------------------------------------------------------------------- |
| Có dữ liệu mẫu/log sạch để test?                       | **Chưa xác minh**   | Cần dữ liệu nội bộ đã ẩn thông tin cá nhân. Đây là điều kiện tiên quyết để đánh giá nghiêm túc. |
| Rủi ro khi AI sai có thể kiểm soát bằng HITL/Fallback? | **Có**              | Scope chỉ là decision support; không cho model tự thực hiện action.                             |
| Stakeholder có sẵn sàng thay đổi quy trình?            | **Chưa xác minh**   | Cần làm việc với CSKH, chủ quy trình CRM, hậu mãi, Legal/Compliance.                            |
| Workflow có thật và có giá trị nghiệp vụ?              | **Có**              | Bước phân loại và chuyển xử lý được VinFast công khai trong quy trình chính thức.               |
| LLM có lý do tồn tại?                                  | **Có điều kiện**    | Có giá trị ở nội dung ngôn ngữ tự do và multi-intent; cần benchmark với Rule-only.              |
| Có cần Agent tự hành?                                  | **Không**           | Autonomy không giải quyết thêm phần khó chính nhưng làm tăng rủi ro.                            |

---

# 11. Quyết định đề xuất

## GO — cho Discovery + Offline Prototype

Nhóm đề xuất **GO**, nhưng chỉ cho giai đoạn **khảo sát quy trình, xây tập đánh giá và prototype offline**.

Đây **không phải GO production** và cũng chưa phải GO để AI tự động route case thật.

Lý do:

**Một, vấn đề có điểm neo nghiệp vụ rõ.** VinFast công khai có bước phân loại và chuyển xử lý; đây không phải workflow được tưởng tượng ra.

**Hai, có một phần công việc mà LLM thực sự phù hợp.** Đó là hiểu văn bản tự do, tách nhiều ý định, trích xuất facts và chỉ ra thông tin thiếu.

**Ba, có thể thiết kế hệ thống để AI sai mà không làm thay đổi case thật.** Shadow mode, human approval và fallback giữ rủi ro ở mức kiểm soát được.

**Bốn, giá trị có thể đo bằng số vận hành.** Không cần dựa vào nhận xét “AI trả lời hay”. Có thể đo triage time, transfer rate, correction rate và SLA.

**Năm, quyết định có thể đảo ngược.** Nếu data cho thấy bottleneck không nằm ở triage, hoặc Rule-only đủ tốt, dự án phải thu hẹp hoặc dừng.

### Gate để chuyển từ Prototype → Pilot

Chỉ chuyển sang pilot nếu:

- có taxonomy được nghiệp vụ phê duyệt;
- có tập dữ liệu đánh giá đủ đại diện;
- Hybrid vượt Rule-only một cách có ý nghĩa;
- đạt ≥95% routing accuracy;
- đạt ≥99% recall cho case cần ưu tiên;
- mọi nhóm rủi ro đều có rule + human owner rõ;
- dữ liệu cá nhân được xử lý theo chính sách phù hợp;
- stakeholder đồng ý workflow mới.

Nếu không đạt, quyết định phải là **NOT YET**, không “tune prompt đến khi đẹp”.

---

# 12. Điều báo cáo này cố ý không kết luận

Để tránh biến một proposal thành câu chuyện quảng cáo AI, báo cáo **không** khẳng định:

- VinFast hiện đang phân loại ticket hoàn toàn thủ công;
- CSKH đang quá tải;
- mỗi case đang mất X phút;
- VinFast đang có tỷ lệ chuyển sai cao;
- AI chắc chắn giảm chi phí;
- LLM chắc chắn tốt hơn hệ thống hiện có.

Các điểm trên chỉ có thể kết luận sau khi có dữ liệu nội bộ và baseline.

---

# 13. Nguồn tham khảo chính

### Nguồn nghiệp vụ VinFast

1. **Quy trình tiếp nhận, phản hồi thông tin và giải quyết phản ánh, yêu cầu, khiếu nại của khách hàng**  
   VinFast, cập nhật bổ sung 27/01/2026.  
   https://vinfastauto.com/vn_vi/quy-trinh-tiep-nhan-phan-hoi-thong-tin-va-giai-quyet-phan-anh-yeu-cau-khieu-nai-cua-khach-hang

2. **Dịch vụ sửa chữa — Quy trình dịch vụ 5 bước**  
   VinFast.  
   https://vinfastauto.com/vn_vi/dich-vu-sua-chua

3. **VinFast khảo sát ý kiến khách hàng — nâng cao chất lượng dịch vụ**  
   VinFast, 20/10/2025.  
   https://vinfastauto.com/vn_vi/vinfast-khao-sat-y-kien-khach-hang-nang-cao-chat-luong-dich-vu

4. **Chương trình Kiến tạo dịch vụ 5 sao cùng VinFast**  
   VinFast, 10/02/2026.  
   https://vinfastauto.com/vn_vi/chuong-trinh-kien-tao-dich-vu-5-sao-cung-vinfast

5. **VinFast tiếp tục triển khai chương trình Kiến tạo dịch vụ 5 sao — giai đoạn 2**  
   VinFast, 2026.  
   https://vinfastauto.com/vn_vi/vinfast-tiep-tuc-trien-khai-chuong-trinh-kien-tao-dich-vu-5-sao-dong-nhat-chuan-dich-vu-nang-tam-trai-nghiem-khach-hang

6. **VinFast lập kỷ lục bàn giao 175.099 xe ô tô điện tại Việt Nam năm 2025**  
   VinFast, 13/01/2026.  
   https://vinfastauto.com/vn_vi/vinfast-lap-ky-luc-ban-giao-xe-o-to-dien-tai-viet-nam-2025

### Nguồn tham khảo cho cách thiết kế AI có kiểm soát

7. **Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile**  
   NIST AI 600-1.  
   https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

8. **Continuous Improvement of Chatbots — Human in the Loop for Improving Modeling**  
   IBM Research.  
   https://research.ibm.com/projects/continuous-improvement-of-chatbots

---

# 14. Một câu chốt proposal

> **Đề xuất này không nhằm “tự động hóa CSKH bằng AI”. Nó nhằm kiểm chứng xem một lớp trợ lý phân loại có thể giúp nhân viên CSKH đưa mỗi yêu cầu vào đúng luồng xử lý nhanh và nhất quán hơn hay không — trong khi quyền quyết định, trách nhiệm nghiệp vụ và các case nhạy cảm vẫn nằm ở con người.**
