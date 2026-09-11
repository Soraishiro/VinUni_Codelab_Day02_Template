# 01 — Problem Scan
## Lab 02: AI Product Scoping — Vin Smart Future

## Mục tiêu

Phần này thực hiện **Phase 1 — SCAN** và **Phase 2 — QUICK-ASSESS** của bài lab.

Tôi không bắt đầu bằng việc chọn một công nghệ AI rồi tìm chỗ để áp dụng. Trước tiên, tôi tìm các vấn đề vận hành có thật, kiểm tra xem vấn đề đó còn tồn tại hay đã được doanh nghiệp giải quyết, sau đó mới đánh giá AI có phù hợp hay không.

---

# 0. Lọc ảo — kiểm tra ý tưởng trước khi đưa vào SCAN

File `03-inspiration-kit.md` cung cấp nhiều ý tưởng để bắt đầu. Tuy nhiên, đây chỉ là **gợi ý**, không phải bằng chứng rằng doanh nghiệp hiện vẫn gặp đúng vấn đề được mô tả.

Vì vậy, trước Phase 1 tôi thực hiện một bước “Lọc ảo”:

1. Lấy từng ý tưởng trong Inspiration Kit làm giả thuyết ban đầu.
2. Tìm nguồn công khai đáng tin cậy của chính doanh nghiệp: quy trình vận hành, báo cáo thường niên, trang sản phẩm, tin tuyển dụng hoặc FAQ chính thức.
3. Kiểm tra xem:
   - quy trình đó có thực sự tồn tại không;
   - doanh nghiệp đã có sản phẩm hoặc hệ thống giải quyết vấn đề đó chưa;
   - phần nào là thông tin đã được xác nhận, phần nào chỉ là suy luận.
4. Chỉ giữ lại các vấn đề còn hợp lý để phân tích tiếp.

Một số ý tưởng bị loại ngay sau bước này. Ví dụ, Vinmec đã đưa DrAid vào xử lý hồ sơ bệnh án và công bố thời gian tóm tắt hồ sơ giảm từ khoảng 5 phút xuống 1 phút. Vinhomes cũng đã có Trợ lý ảo trên Vinhomes Resident, đồng thời V-PMS đã tự động giao việc và theo dõi xử lý phản ánh khách hàng. Vì vậy, nếu tiếp tục đề xuất “AI tóm tắt hồ sơ Vinmec” hoặc “xây trợ lý cư dân Vinhomes” như một bài toán mới thì không còn thuyết phục.

Bước Lọc ảo giúp tránh một lỗi khá phổ biến: **giải một bài toán nghe hợp lý nhưng thực tế doanh nghiệp đã giải rồi**.

---

# Phase 1 — SCAN

Worksheet yêu cầu tìm ít nhất 5 vấn đề thực tế. Tôi dùng các góc nhìn: công việc lặp lại, công việc tốn thời gian, dịch vụ có thể cải thiện bằng AI và pain point của người dùng/nhân viên.

## 1. Danh sách 5 vấn đề

| # | Công ty / Bộ phận | Góc nhìn | Vấn đề được ghi nhận |
|---:|---|---|---|
| **1** | **VinFast — Chăm sóc khách hàng / hậu mãi** | Lặp lại + tốn thời gian | Khách hàng gửi yêu cầu qua nhiều kênh. Trung tâm CSKH phải tiếp nhận, phân loại và quyết định yêu cầu nào xử lý ngay, yêu cầu nào chuyển sang phòng ban hoặc đại lý ủy quyền. |
| **2** | **Vinpearl — Đặt phòng / chăm sóc khách hàng** | Lặp lại + tốn thời gian | Nhân viên tiếp nhận các yêu cầu đặt phòng, đặt vé, thay đổi hoặc hủy dịch vụ; sau đó phải đọc nội dung, xác định đầy đủ thông tin và thao tác trên hệ thống B2B/OTA hoặc làm việc với đối tác. |
| **3** | **Vinhomes — Kiểm soát chất lượng vận hành CRM** | Lặp lại | Bộ phận QC phải kiểm tra việc tuân thủ quy trình, thao tác CRM, tình trạng cập nhật dữ liệu, lỗi nhập liệu và các bước bị bỏ sót. |
| **4** | **VinBus — Chăm sóc khách hàng** | Tốn thời gian + pain từ khách hàng | Khi tiếp nhận phản ánh, CSKH cần thu thập nhiều thông tin như thời gian xảy ra sự việc, biển số xe, tuyến, hướng di chuyển, điểm dừng và nội dung phản ánh để xác minh. |
| **5** | **VinBus — Vận hành thông tin thời gian xe đến trạm** | AI có thể cải thiện + pain từ khách hàng | VinBus thừa nhận có trường hợp thời gian xe đến trạm hiển thị chưa chính xác khi xe mất kết nối và hệ thống không nhận được vị trí, vận tốc chính xác. |

### Cơ sở lựa chọn

**VinFast:** quy trình chính thức của VinFast nêu rõ ba bước: tiếp nhận yêu cầu → phân loại và chuyển xử lý → phản hồi/xác nhận kết quả. Yêu cầu có thể đến từ hotline, email, website, ứng dụng VinFast hoặc thư.

**Vinpearl:** mô tả công việc chính thức của Vinpearl cho thấy nhân viên phải tiếp nhận yêu cầu đặt vé, đặt phòng, dịch vụ; thực hiện đặt, xuất, hủy hoặc thay đổi qua B2B/OTA hoặc đối tác.

**Vinhomes:** mô tả công việc vị trí QC yêu cầu kiểm tra SOP, thao tác CRM, phát hiện lỗi nhập liệu, sai chức năng, không cập nhật đúng thời gian và bỏ sót bước.

**VinBus:** FAQ chính thức yêu cầu khách cung cấp thông tin khá chi tiết khi phản ánh. FAQ cũng xác nhận ETA có thể sai khi xe mất kết nối.

---

# Phase 2 — QUICK-ASSESS

Từ 5 vấn đề trên, tôi chọn 3 vấn đề có quy trình rõ nhất để đánh giá sâu hơn:

1. VinFast — phân loại và chuyển yêu cầu khách hàng.
2. Vinpearl — xử lý yêu cầu đặt phòng/dịch vụ từ nội dung tự do.
3. Vinhomes — kiểm tra sai sót CRM và tuân thủ quy trình.

---

# Quick Problem Card 1
## VinFast — Hỗ trợ phân loại và chuyển yêu cầu khách hàng

### Bài toán

Hỗ trợ nhân viên CSKH đọc hiểu yêu cầu của khách, tóm tắt nội dung, xác định loại vấn đề và **đề xuất** bộ phận/đại lý phù hợp để xử lý. Quyết định chuyển yêu cầu cuối cùng vẫn thuộc về nhân viên.

### Ai đang gặp khó khăn?

- Nhân viên Trung tâm Chăm sóc Khách hàng.
- Phòng ban hoặc đại lý nhận yêu cầu được chuyển đến.
- Khách hàng nếu yêu cầu bị hiểu sai hoặc phải chuyển qua nhiều nơi.

### Quy trình hiện tại

Theo quy trình chính thức của VinFast:

1. Khách hàng gửi yêu cầu qua hotline, email, website, ứng dụng hoặc thư.
2. Trung tâm CSKH tiếp nhận thông tin.
3. CSKH phân loại yêu cầu.
4. Nếu có thể xử lý ngay, CSKH tư vấn và đóng sự vụ.
5. Nếu chưa thể xử lý ngay, yêu cầu được chuyển sang phòng ban phụ trách hoặc đại lý ủy quyền.
6. Sau khi xử lý, VinFast phản hồi và xác nhận kết quả với khách hàng.

### Bước có khả năng gây khó khăn nhất

Bước **phân loại và xác định nơi xử lý phù hợp**.

Nguồn công khai không cho biết VinFast hiện đang tự động hóa bước này đến mức nào, cũng không có số liệu về thời gian xử lý một yêu cầu. Vì vậy, đây được xem là **điểm nghẽn cần kiểm chứng**, không phải một kết luận rằng toàn bộ công việc đang làm thủ công.

### AI có thể hỗ trợ gì?

AI có thể:

- tóm tắt nội dung khách hàng gửi;
- nhận diện một hoặc nhiều ý định trong cùng yêu cầu;
- trích xuất thông tin quan trọng;
- chỉ ra thông tin còn thiếu;
- đề xuất nhóm vấn đề và nơi tiếp nhận phù hợp;
- cảnh báo các trường hợp nhạy cảm hoặc cần ưu tiên.

AI **không tự chuyển yêu cầu** mà chỉ tạo gợi ý để nhân viên duyệt.

### Chỉ số đánh giá đề xuất cho thử nghiệm

Đây là **mục tiêu thử nghiệm**, không phải số liệu hiện tại của VinFast:

- Đề xuất đúng nơi xử lý so với nhãn của nhân viên: **từ 95% trở lên**.
- Phát hiện các trường hợp nghiêm trọng/an toàn cần chuyển người kiểm tra: **từ 99% trở lên**.
- Kết quả trả về đúng cấu trúc dữ liệu yêu cầu: **100%**.
- Trường hợp AI không chắc chắn phải chuyển sang người kiểm tra: **100%**.
- Thời gian AI xử lý một yêu cầu: **dưới 10 giây**.

### Kiến trúc phù hợp

**LLM Feature kết hợp Rule và Human-in-the-loop.**

Rule dùng cho các điều kiện cứng; mô hình ngôn ngữ dùng để hiểu nội dung tự do; nhân viên là người quyết định cuối cùng.

Không cần Agent tự hành.

---

# Quick Problem Card 2
## Vinpearl — Chuẩn hóa yêu cầu đặt phòng và dịch vụ

### Bài toán

Hỗ trợ nhân viên đọc các yêu cầu đặt phòng, đặt vé, thay đổi hoặc hủy dịch vụ và chuyển nội dung tự do thành thông tin có cấu trúc trước khi thao tác trên hệ thống.

### Ai đang gặp khó khăn?

Nhân viên đặt phòng và chăm sóc khách hàng, đặc biệt khi một yêu cầu chứa nhiều thông tin như ngày đi, số lượng người, số phòng, trẻ em, yêu cầu đặc biệt hoặc thay đổi lịch trình.

### Quy trình hiện tại

Từ mô tả công việc chính thức của Vinpearl:

1. Tiếp nhận yêu cầu đặt vé, đặt phòng hoặc dịch vụ.
2. Tư vấn và làm rõ nhu cầu khách hàng.
3. Xác định các thông tin cần thiết.
4. Thực hiện đặt, xuất, hủy hoặc thay đổi qua B2B/OTA hoặc đối tác.
5. Theo dõi dịch vụ và xử lý các vấn đề phát sinh.

### Bước có khả năng gây khó khăn nhất

Bước đọc yêu cầu tự do và chuyển thành đầy đủ các trường thông tin cần thiết trước khi đặt dịch vụ.

Nguồn công khai không cho biết bước này hiện mất bao lâu, vì vậy thời gian xử lý cần được đo nếu triển khai thử nghiệm.

### AI có thể hỗ trợ gì?

AI chỉ thực hiện phần **đọc và trích xuất thông tin**, ví dụ:

- ngày nhận/trả phòng;
- số khách;
- số phòng;
- loại yêu cầu;
- yêu cầu đặc biệt;
- thông tin còn thiếu cần hỏi lại.

AI không được tự xác nhận phòng trống, giá hoặc đặt phòng.

### Chỉ số đánh giá đề xuất

- Độ chính xác khi trích xuất các trường bắt buộc: **từ 98% trở lên**.
- Kết quả đúng cấu trúc: **100%**.
- Phát hiện yêu cầu còn thiếu thông tin: **từ 99% trở lên**.
- Không có trường hợp AI tự xác nhận đặt phòng hoặc tự báo giá: **0 trường hợp**.

### Kiến trúc phù hợp

**LLM Feature + Rule kiểm tra dữ liệu + nhân viên duyệt.**

---

# Quick Problem Card 3
## Vinhomes — Kiểm tra sai sót CRM và tuân thủ quy trình

### Bài toán

Hỗ trợ bộ phận QC phát hiện các bản ghi CRM có dấu hiệu sai quy trình hoặc thiếu dữ liệu để nhân viên tập trung kiểm tra những trường hợp bất thường.

### Ai đang gặp khó khăn?

Chuyên viên QC, bộ phận Sales Operations và Marketing Operations.

### Quy trình hiện tại

Theo tin tuyển dụng chính thức của Vinhomes:

1. Kiểm tra việc tuân thủ SOP trong vận hành nền tảng và phân phối lead.
2. Kiểm tra thao tác trên CRM, listing và dashboard.
3. Phát hiện lỗi nhập liệu, sử dụng sai chức năng, không cập nhật đúng hạn hoặc bỏ sót bước.
4. Phân loại lỗi theo mức độ.
5. Tổng hợp và báo cáo.

### Bước có khả năng gây khó khăn nhất

Việc kiểm tra lặp lại một lượng lớn bản ghi và tìm các trường hợp bất thường.

### AI có thể hỗ trợ gì?

Sau khi phân tích, tôi cho rằng **phần lớn bài toán này không cần mô hình ngôn ngữ**.

Ví dụ:

- trường bắt buộc bị bỏ trống → Rule;
- cập nhật trễ → Rule;
- trạng thái đi sai thứ tự → State Machine;
- phân phối sai khu vực → Rule.

Mô hình ngôn ngữ chỉ có ích nếu cần kiểm tra các phần văn bản tự do như ghi chú, mô tả hoặc nội dung listing.

### Chỉ số đánh giá đề xuất

- Phát hiện được ít nhất **95%** lỗi đã cài sẵn trong bộ dữ liệu thử nghiệm.
- Tỷ lệ cảnh báo sai không vượt quá **5%**.
- Các điều kiện cứng phải cho kết quả lặp lại giống nhau: **100%**.
- Hệ thống không tự khóa hay xử phạt bản ghi: **0 trường hợp**.

### Kiến trúc phù hợp

**Rule / State Machine là chính.**

Đây là ví dụ cho thấy không phải vấn đề nào cũng nên dùng LLM.

---

# Quyết định sau Phase 2

## Bài toán được chọn: VinFast — hỗ trợ phân loại và chuyển yêu cầu khách hàng

Tôi chọn bài toán VinFast vì bốn lý do.

Thứ nhất, **quy trình có bằng chứng trực tiếp từ VinFast**. Công ty công khai rõ bước tiếp nhận, phân loại và chuyển yêu cầu cho phòng ban/đại lý.

Thứ hai, phần khó của bài toán nằm ở **hiểu nội dung ngôn ngữ tự nhiên**, đây là nơi mô hình ngôn ngữ có lợi thế rõ hơn so với chỉ dùng luật cố định.

Thứ ba, bài toán có thể giới hạn rủi ro tốt. AI chỉ đưa ra gợi ý, còn nhân viên CSKH giữ quyền quyết định.

Thứ tư, đây là bài toán đủ thực tế nhưng không cần xây một Agent tự hành phức tạp. Vì vậy nhóm có thể tập trung đúng vào mục tiêu của lab: xác định bài toán, chọn đúng mức AI và thiết kế ranh giới vận hành.

## Phạm vi bài toán

### AI được phép hỗ trợ

- đọc và tóm tắt yêu cầu;
- nhận diện loại vấn đề;
- phát hiện thông tin thiếu;
- gợi ý mức độ ưu tiên;
- đề xuất nơi tiếp nhận;
- đánh dấu trường hợp cần người kiểm tra.

### AI không được phép

- tự chẩn đoán lỗi kỹ thuật của xe;
- quyết định bảo hành hoặc bồi thường;
- tự trả lời khiếu nại cuối cùng;
- tự đóng sự vụ;
- tự chuyển sự vụ mà không có người duyệt;
- tự thay đổi dữ liệu trên hệ thống CRM.

---

# Nguồn tham khảo

1. **VinFast — Quy trình tiếp nhận, phản hồi và giải quyết phản ánh/yêu cầu/khiếu nại của khách hàng**  
   https://vinfastauto.com/vn_vi/quy-trinh-tiep-nhan-phan-hoi-thong-tin-va-giai-quyet-phan-anh-yeu-cau-khieu-nai-cua-khach-hang

2. **Vinpearl Careers — Chuyên viên Kinh doanh & Chăm sóc Khách hàng**  
   https://careers.vinpearl.com/job/vinpearl-head-office-chuyen-vien-kinh-doanh-cham-soc-khach-hang-ve-may-bay-khach-san-quoc-te-10386

3. **Vinhomes Careers — Chuyên viên Quản lý Chất lượng (QC)**  
   https://careers.vinhomes.vn/job/chuyen-vien-quan-ly-chat-luong-qc-10681

4. **VinBus — FAQ và thông tin liên hệ**  
   https://vinbus.vn/lien-he

5. **Vinmec — DrAid tiết kiệm thời gian xử lý hồ sơ y tế**  
   https://www.vinmec.com/vie/bai-viet/dot-pha-cong-nghe-ai-tai-vinmec-tiet-kiem-80-thoi-gian-xu-ly-ho-so-y-te

6. **Vinhomes — Trợ lý ảo trên Vinhomes Resident và Vinhomes Online**  
   https://market.vinhomes.vn/blog/ra-mat-tro-ly-ao-tren-ung-dung-vinhomes-resident-va-vinhomes-online

7. **Vinhomes Annual Report 2024 — V-PMS**  
   https://vinhomes.vn/vi/bao-cao-thuong-nien
