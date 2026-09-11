# 01 — Problem Scan & Quick Cards

> **Lab 02: AI Product Scoping (Vin Smart Future)**
> Họ và tên: `<Điền tên của bạn>`
> Mã sinh viên: `<Điền MSSV>`
> Branch cá nhân: `nguyenkhacgiap`
> Ngày thực hiện: `<dd/mm/yyyy>`

> Tôi không có quyền truy cập dữ liệu vận hành nội bộ Vingroup. Các con số trong tài liệu này hoặc trích từ nguồn công khai (có link ở cuối file), hoặc là ước tính của tôi kèm chuỗi lập luận — không con số nào được trình bày như số liệu nội bộ.

---

# 🔍 Phase 1 — SCAN: Quét cơ hội (Cá nhân)

Sử dụng **4 Lenses** để quét hoạt động vận hành của các công ty thành viên Vingroup:

1. **Repetitive** — Tác vụ lặp đi lặp lại nhiều lần hằng ngày.
2. **Time-consuming** — Tác vụ ngốn thời gian xử lý thủ công của nhân viên.
3. **AI-upgrade** — Dịch vụ hiện tại còn chậm hoặc phản hồi rập khuôn.
4. **Stakeholder Pain** — Bottleneck khiến khách hàng/nhân viên thực địa phàn nàn.

## 📝 Danh sách bài toán của tôi

| # | Subsidiary | Lens | Mô tả ngắn bài toán | Mức độ xác thực |
|---|---|---|---|---|
| 1 | **Xanh SM** | Stakeholder Pain | Taxi điện và chủ xe cá nhân tranh nhau trụ sạc công cộng. Điều phối viên phải xếp lịch sạc cho đội xe trên tài nguyên dùng chung đang tắc nghẽn, đồng thời tôn trọng quy tắc nhường trụ cho xe cá nhân. | **Có nguồn** — báo chí ghi nhận trạm quá tải, VinFast đã lập trạm ưu tiên và ban hành quy tắc nhường trụ |
| 2 | **VinFast** | Time-consuming | Giữ cam kết cấp phụ tùng trong 24h: cần dự báo phụ tùng cần thiết ngay khi khách mô tả lỗi, để kho vùng điều chuyển trước khi xe vào xưởng. | **Có nguồn, cần xác minh lại hiệu lực** — cam kết 24h là công bố chính thức (01/9/2024), xác nhận còn duy trì tới 2025; chưa kiểm chứng được tình trạng hiện tại |
| 3 | **Vinpearl** | Stakeholder Pain | Review tiêu cực nằm rải trên Booking.com, Agoda, Google Maps; quản lý đọc thủ công nên phàn nàn khẩn bị phát hiện muộn. | **Chưa kiểm chứng** — lấy từ inspiration kit, tôi chưa tìm được nguồn công khai |
| 4 | **Vinhomes** | Repetitive | Gia hạn vé gửi xe hằng tháng: nhân viên BQL đối chiếu mã căn hộ, biển số, trạng thái thanh toán rồi kích hoạt thẻ. | **Chưa kiểm chứng** — lấy từ inspiration kit |
| 5 | **Vinmec** | Time-consuming | Bác sĩ trích xuất thông tin từ bệnh án điện tử để soạn tóm tắt xuất viện bằng ngôn ngữ bệnh nhân hiểu được. | **Chưa kiểm chứng** — lấy từ inspiration kit |

### Vì sao 5 bài này?

* **Phủ đủ 4 lenses** và trải trên **5 công ty thành viên**, tránh dồn hết vào một mảng.
* **#1 và #2 được ưu tiên vì có bằng chứng công khai.** Hai bài này không chỉ "nghe hợp lý" — pain đã được báo chí ghi nhận và doanh nghiệp đã phải phản ứng bằng chính sách. Đó là dấu hiệu mạnh nhất cho thấy bài toán có thật.
* **#1 được neo vào bối cảnh điều vận Xanh SM** để ranh giới vận hành khớp với prompt prototype ở Phase 4 (`[DRAFT_ONLY]` + ngưỡng pin 5% + `dispatch_mobile_charger`).
* Có **cả bài đáng làm lẫn bài đáng từ chối**: #4 cố tình được đưa vào vì nó *trông* hợp AI (lặp lại nhiều) nhưng thực chất là bài toán rule-based — dùng làm đối chứng ở Phase 2.
* **#5 bị loại sớm** dù tác động lớn: không thành viên nào trong nhóm nắm được quy trình thật trong bệnh viện, nên phần Current-State Workflow (Gate G1) sẽ chỉ là phỏng đoán. Ghi nhận rồi loại có lý do là cách xử lý trung thực hơn là viết bừa.

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

Top 3 được chọn: **#1 (Xanh SM lịch sạc), #2 (VinFast phụ tùng 24h), #4 (Vinhomes vé gửi xe).**

---

## 🃏 QUICK PROBLEM CARD #1 — Xanh SM: Lập lịch sạc trên trạm dùng chung

| Trường | Nội dung |
|---|---|
| **Bài toán** | Điều phối viên phải xếp lịch sạc cho đội taxi điện trên mạng trạm sạc công cộng đang tắc nghẽn, vừa đảm bảo xe đủ pin cho ca sau, vừa tôn trọng quy tắc nhường trụ cho chủ xe cá nhân — hiện làm hoàn toàn thủ công. |
| **Công ty thành viên** | `[ ] VinFast  [x] Xanh SM  [ ] Vinhomes  [ ] Vinmec  [ ] Vinpearl` |
| **Ai đang đau (Actor)** | **Hai nhóm cùng lúc:** (a) Điều phối viên Trung tâm Điều vận Xanh SM — người xếp lịch; (b) Chủ xe VinFast cá nhân — người chịu hậu quả khi taxi chiếm trụ |
| **Workflow thủ công hiện tại** | 1. Xuất báo cáo mức pin cuối ca từ dashboard ──> 2. Đọc ghi chú tự do tài xế nhập trong app (*"mai em nghỉ"*, *"trạm Mỹ Đình hỏng trụ 3"*) ──> 3. Tra trạm còn trụ trống, loại trừ 16 trạm ưu tiên dành cho xe cá nhân ──> 4. Xếp xe vào khung giờ/trạm, soạn tin báo từng tài xế ──> 5. Tự rà lại rồi gửi |
| **Bước tốn thời gian/lỗi nhất** | **Bước 3 + 4** — ước tính ~65/90 phút mỗi ca. Bước 2 là nơi sinh lỗi: ghi chú tự do dễ bị đọc sót. |
| **AI nhảy vào ở bước nào** | **Bước 2** — LLM đọc & chuẩn hoá ghi chú tự do thành trường có cấu trúc (xe nghỉ / trạm lỗi / yêu cầu đặc biệt); **Bước 4** — LLM soạn nháp tin nhắn cá nhân hoá cho từng tài xế. **Bước 3 giữ nguyên bằng solver/rule.** |
| **Metric thành công (có số)** | 1. Thời gian lập lịch giảm từ ~90 phút → **dưới 20 phút/ca**<br>2. Tỉ lệ xe phải gọi cứu hộ pin khẩn đầu ca sáng giảm từ ~6% → **dưới 2% đội xe**<br>3. Tỉ lệ lịch sạc vi phạm quy tắc nhường trụ (chiếm trạm ưu tiên, hoặc giữ trụ quá 80% pin) → **dưới 5%** |
| **Quick Architecture** | `[ ] No AI  [x] Rule  [x] LLM  [ ] Agent` — **hybrid:** rule/solver lo phân bổ trạm, LLM lo phần ngôn ngữ |

**Bằng chứng bài toán có thật:**
* Trạm **Vinhomes Times City**: 18h giờ tan tầm chỉ còn **1 trụ trống**; nửa đêm "toàn taxi án ngữ ở từng trụ sạc".
* Trạm **Big C Thăng Long**: chủ xe cá nhân phải **chờ vài tiếng** mỗi lần đi sạc.
* VinFast đã phải phản ứng bằng chính sách: lập **16 trạm sạc ưu tiên** cho xe cá nhân (Bắc/Nam Từ Liêm, Gia Lâm, Hà Đông, Cầu Giấy) và **đào tạo tài xế nhường trụ khi đạt 70-80% pin**.
* Quy mô đội xe: **hơn 20.000 xe taxi điện** (03/2026), tăng 33 lần từ 600 xe lúc khai trương 30/4/2023.

> ⚠️ **Giới hạn của bằng chứng:** bài báo về quá tải trạm sạc đăng **25/04/2023**, gần 3 năm trước thời điểm làm lab. VinFast đã mở rộng mạng lưới trạm từ đó nên mức độ tắc nghẽn hiện tại có thể đã giảm. **Việc cần làm đầu tiên nếu GO: đo lại tình trạng thực tế trước khi cam kết bất kỳ metric nào.**

**Cách suy ra con số ước tính:** Từ 20.000 xe toàn quốc, giả định Hà Nội chiếm ~25% đội (~5.000 xe) và một điều phối viên phụ trách ~120 xe/ca → ~42 người/ca. Với ~45 giây xử lý thủ công mỗi xe → ~90 phút/ca. Tỉ lệ 6% cứu hộ khẩn là giả định thuần tuý, **chưa có nguồn nào xác nhận** — đây là số yếu nhất trong thẻ này.

**Phản biện (đóng vai CFO + Trưởng phòng Vận hành):**
1. *"Phân bổ xe vào trạm là bài toán tối ưu có ràng buộc — đó là việc của solver, không phải LLM. Anh đang trả tiền token cho việc mà OR-Tools làm tốt hơn và tất định."* → **Đúng, và tôi chấp nhận:** LLM chỉ được giao phần đọc ghi chú tự do và soạn tin; phần xếp lịch để rule/solver.
2. *"Nếu bắt tài xế nhập ghi chú theo dropdown thay vì gõ tự do thì bước 2 biến mất, khỏi cần AI."* → **Phản biện hợp lệ.** Cần đo trước: bao nhiêu % ghi chú thực sự không nhét vừa 8 lựa chọn dropdown. Nếu dưới 15% thì bài này nên NO-GO.
3. *"Bài báo anh dẫn từ 2023. Lấy gì đảm bảo trạm vẫn còn tắc?"* → **Không đảm bảo được.** Đây là lý do metric phải được thiết lập lại từ baseline đo mới, và cũng là lý do scope pilot nên giới hạn ở vài trạm cụ thể thay vì triển khai toàn quốc.

---

## 🃏 QUICK PROBLEM CARD #2 — VinFast: Giữ cam kết cấp phụ tùng trong 24h

| Trường | Nội dung |
|---|---|
| **Bài toán** | VinFast cam kết công khai cấp phụ tùng trong tối đa 24h. Để giữ cam kết, kho vùng cần biết xe sắp vào xưởng cần phụ tùng gì — nhưng thông tin đó đang nằm trong mô tả lỗi bằng tiếng Việt đời thường của khách và ghi chú tự do của kỹ thuật viên. |
| **Công ty thành viên** | `[x] VinFast  [ ] Xanh SM  [ ] Vinhomes  [ ] Vinmec  [ ] Vinpearl` |
| **Ai đang đau (Actor)** | Nhân viên điều phối kho vùng + Cố vấn dịch vụ tại xưởng |
| **Workflow thủ công hiện tại** | 1. Khách mô tả lỗi qua hotline/app (*"đi qua gờ giảm tốc kêu cụp cụp ở bánh trước"*) ──> 2. Cố vấn dịch vụ đoán nhóm lỗi, đặt lịch ──> 3. Xe vào xưởng, kỹ thuật viên chẩn đoán chính thức ──> 4. **Lúc này mới** đặt phụ tùng từ kho vùng ──> 5. Chờ điều chuyển |
| **Bước tốn thời gian/lỗi nhất** | **Bước 4-5** — đồng hồ 24h chỉ bắt đầu chạy sau khi xe đã vào xưởng. Mọi thời gian ở bước 1-3 là thời gian chết mà đáng lẽ đã có thể dùng để điều chuyển phụ tùng trước. |
| **AI nhảy vào ở bước nào** | **Bước 1-2** — LLM đọc mô tả lỗi của khách, sinh ra danh sách 1-3 nhóm phụ tùng khả năng cần kèm độ tin cậy, để kho vùng **điều chuyển dự phòng trước khi xe tới**. |
| **Metric thành công (có số)** | 1. Tỉ lệ giữ đúng cam kết **24h** tăng lên **≥ 95%** (ngưỡng lấy từ chính cam kết công khai, không phải tôi tự đặt)<br>2. Thời gian chờ phụ tùng trung bình giảm **≥ 30%** so với baseline đo được<br>3. Tỉ lệ điều chuyển dự phòng **sai** (phụ tùng chuyển đi nhưng không dùng) giữ **dưới 20%** |
| **Quick Architecture** | `[ ] No AI  [ ] Rule  [x] LLM  [ ] Agent` — LLM lo phần ngôn ngữ; phần tối ưu tồn kho là bài toán OR riêng |

**Bằng chứng bài toán có thật:** Từ **01/9/2024**, VinFast cam kết rút ngắn thời gian cung cấp linh kiện, phụ tùng chính hãng xuống **tối đa 24 giờ** — được mô tả là cam kết chưa hãng xe nào tại Việt Nam đưa ra. Để thực hiện, hãng đầu tư mạng kho trung chuyển theo vùng và quy trình nối nhà máy → kho trung tâm → kho vùng → xưởng dịch vụ.

> **Hiệu lực chính sách — rủi ro của thẻ này:**
> * Chính sách hậu mãi đặc biệt (27/6/2024) có **bồi thường tiền mặt** khi sửa chữa kéo dài, nhưng đã **dừng áp dụng từ 01/01/2025**. Vì vậy Business Impact của thẻ này **không quy đổi trực tiếp ra tiền được**.
> * Cam kết **cấp phụ tùng 24 giờ vẫn được giữ**, cùng bảo hành 10 năm và cứu hộ 24/7 — theo chính thông báo dừng chính sách của hãng (12/2024).
> * **Chưa xác minh được cam kết 24h còn hiệu lực tại 9/2026 hay không** — trang chính sách chính thức trả lỗi 403, mốc xác nhận gần nhất là năm 2025. Nếu cam kết đã bị bỏ thì metric #1 mất hiệu lực và thẻ phải bị loại.

**Vì sao đây vẫn là thẻ có metric tốt:** ngưỡng 24h là cam kết công khai của chính doanh nghiệp, nên baseline và mục tiêu đều có điểm neo bên ngoài thay vì do nhóm tự đặt.

**Ranh giới an toàn bắt buộc:** AI **tuyệt đối không** kết luận xe có an toàn để lưu thông hay không, và **không** tự động đặt hàng phụ tùng. Output chỉ là **gợi ý điều chuyển dự phòng** để nhân viên kho quyết định.

**Phản biện (đóng vai CFO + Trưởng phòng Vận hành):**
1. *"Điều chuyển dự phòng sai thì phụ tùng nằm chết ở kho vùng — anh đang đổi rủi ro trễ hẹn lấy chi phí tồn kho, mà giờ trễ hẹn còn chẳng phải đền tiền nữa."* → **Phản biện rất mạnh sau khi chính sách đền bù bị dừng.** Vì thế metric #3 (tỉ lệ điều chuyển sai) phải được theo dõi ngang hàng với metric #1, và chỉ áp dụng cho nhóm phụ tùng giá trị thấp, xoay vòng nhanh trong giai đoạn pilot.
2. *"Anh lấy đâu ra tập mô tả-lỗi-đã-gán-nhãn-mã-phụ-tùng để đo độ chính xác?"* → **Đây chính là điểm chặn.** Dữ liệu này về lý thuyết tồn tại trong lịch sử phiếu sửa chữa, nhưng nhóm không có quyền truy cập để xác nhận. Chưa nối được mô tả của khách với mã phụ tùng thực tế đã dùng thì không thể đo → thẻ này chỉ có thể là **NOT YET**.
3. *"Phần khó thật sự là tối ưu tồn kho đa kho, đó là bài toán OR chứ không phải LLM."* → **Đồng ý.** LLM chỉ giải quyết khúc đầu (hiểu ngôn ngữ). Nếu khúc OR chưa sẵn sàng thì khúc LLM có chính xác mấy cũng vô dụng.

---

## 🃏 QUICK PROBLEM CARD #3 — Vinhomes: Gia hạn vé gửi xe hằng tháng

| Trường | Nội dung |
|---|---|
| **Bài toán** | Đầu mỗi tháng nhân viên Ban quản lý phải xử lý thủ công hàng loạt yêu cầu gia hạn vé gửi xe: đối chiếu căn hộ, biển số, trạng thái thanh toán rồi kích hoạt thẻ. |
| **Công ty thành viên** | `[ ] VinFast  [ ] Xanh SM  [x] Vinhomes  [ ] Vinmec  [ ] Vinpearl` |
| **Ai đang đau (Actor)** | Nhân viên Ban quản lý tòa nhà (Vinhomes Resident) |
| **Workflow thủ công hiện tại** | 1. Nhận yêu cầu gia hạn qua app ──> 2. Đối chiếu mã căn hộ + biển số trong hệ thống ──> 3. Kiểm tra trạng thái thanh toán ──> 4. Kích hoạt thẻ + gửi xác nhận cho cư dân |
| **Bước tốn thời gian/lỗi nhất** | **Bước 2 + 3** — ước tính ~2/3 phút mỗi yêu cầu, dồn cục vào 3 ngày đầu tháng |
| **AI nhảy vào ở bước nào** | ❌ **Không bước nào.** Toàn bộ đầu vào đã có cấu trúc sẵn: mã căn hộ, biển số, tháng, trạng thái thanh toán. Không có ngôn ngữ tự nhiên nào cần hiểu. |
| **Metric thành công (có số)** | Thời gian xử lý giảm từ ~3 phút → **dưới 10 giây**, độ chính xác **100%** (không phải 97%) |
| **Quick Architecture** | `[x] No AI  [x] Rule  [ ] LLM  [ ] Agent` |

**Vì sao tôi đưa thẻ này vào rồi chủ động loại:** Đây là **bài toán bẫy**. Nó thoả mãn lens "Lặp lại" một cách hoàn hảo và tổng thời gian tiết kiệm được thậm chí lớn hơn thẻ #2. Nhưng đầu vào hoàn toàn tất định — một form kèm vài ràng buộc `if` giải quyết xong, **rẻ hơn, nhanh hơn và đúng 100%** thay vì 97%. Nhét LLM vào đây là biến một bài toán tất định thành bài toán xác suất, tức là làm nó tệ đi.

**Phản biện (đóng vai CFO + Trưởng phòng Vận hành):** cả ba ý kiến phản biện đều thống nhất — *"Đây là bài toán tự động hoá quy trình, không phải bài toán AI. Làm rule-based, đóng hồ sơ."* Tôi đồng ý.

---

# 🗳️ Quyết định lựa chọn

| Thẻ | Bài toán | Verdict | Lý do một dòng |
|---|---|---|---|
| **#1** | Xanh SM — lịch sạc trên trạm dùng chung | ✅ **GO** → Deep-Dive | Pain có bằng chứng công khai, có sẵn quy tắc vận hành thành văn để làm ranh giới, phần ngôn ngữ tự nhiên thật sự cần LLM |
| **#2** | VinFast — phụ tùng 24h | ⏸️ **NOT YET** | SLA công khai cho metric tốt, nhưng chưa nối được mô tả lỗi với mã phụ tùng thực dùng, **và chưa xác minh được cam kết 24h còn hiệu lực năm 2026** |
| **#3** | Vinhomes — vé gửi xe | ⛔ **NO-GO** | Đầu vào tất định, rule-based rẻ hơn và chính xác hơn |

* **Thẻ được chọn để Deep-Dive:** **Card #1 — Xanh SM: Lập lịch sạc trên trạm dùng chung**

* **Lý do chọn:**
  1. **Có bằng chứng công khai** rằng bài toán tồn tại, thay vì chỉ là giả định hợp lý.
  2. **Ranh giới vận hành đã có sẵn dạng thành văn:** quy tắc nhường trụ ở 70-80% pin là chính sách doanh nghiệp đã ban hành — đưa thẳng vào Operational Boundary được, không cần tự nghĩ ra.
  3. **Ranh giới rủi ro kiểm soát được:** mọi lệnh điều phối đều là bản nháp chờ điều phối viên duyệt, và xe đã dưới ngưỡng pin nguy cấp thì buộc chuyển sang điều xe sạc di động thay vì xếp chạy tới trạm — đúng hai ranh giới được lập trình và stress-test ở Phase 4.
  4. **AI Fit trung thực:** nhóm phân định rõ phần nào để rule/solver, phần nào để LLM, thay vì nhét LLM vào toàn bộ quy trình.

* **Lý do loại 2 thẻ còn lại:**
  * **Card #2 (VinFast):** ngưỡng 24h là cam kết công khai nên cho metric có điểm neo bên ngoài. Nhưng thiếu tập dữ liệu nối mô tả lỗi với mã phụ tùng thực dùng, phần nặng nhất lại là bài toán tối ưu tồn kho chứ không phải LLM, **và bản thân cam kết 24h chưa được xác minh là còn hiệu lực**. Sẽ chỉ chuyển thành GO khi xác minh được cả hai điều đó.
  * **Card #3 (Vinhomes):** loại vì rule-based là lời giải đúng. Giữ lại trong báo cáo làm bằng chứng rằng nhóm có sàng lọc chứ không mặc định mọi bài toán đều cần AI.

---

# 📚 Nguồn tham khảo

| # | Nguồn | Dùng cho | Ngày đăng |
|---|---|---|---|
| 1 | [Khắc phục tình trạng người dùng giành chỗ sạc với taxi Xanh SM — AutoPro](https://autopro.com.vn/khac-phuc-tinh-trang-nguoi-dung-gianh-cho-sac-voi-taxi-xanh-sm-danh-sach-tram-sac-uu-tien-nen-biet-177230425143104513.chn) | Trạm quá tải (Times City, Big C Thăng Long), 16 trạm ưu tiên, quy tắc nhường trụ 70-80% | 25/04/2023 |
| 2 | [Xanh SM tăng quy mô gấp 33 lần, chiếm 83% thị phần taxi TP.HCM — Người Quan Sát](https://nguoiquansat.vn/xanh-sm-cua-ty-phu-pham-nhat-vuong-tang-quy-mo-gap-33-lan-dang-chiem-83-thi-phan-taxi-tai-tp-hcm-278787.html) | Quy mô đội xe >20.000 xe; mốc khởi điểm 600 xe (30/4/2023) | 12/03/2026 |
| 3 | [Thị trường taxi Việt Quý I/2026: Xe xanh áp đảo — VnEconomy](https://vneconomy.vn/automotive/thi-truong-taxi-viet-quy-i2026-xe-xanh-ap-dao-tai-cau-truc-thi-phan.htm) | Thị phần Green SM 54,51% Q1/2026 | Q2/2026 |
| 4 | [VinFast cam kết cung cấp phụ tùng trong 24 giờ — VnExpress](https://vnexpress.net/vinfast-cam-ket-cung-cap-phu-tung-trong-24-gio-4786422.html) | Cam kết SLA 24h, hiệu lực từ 01/9/2024 | 08/2024 |
| 5 | [VinFast cam kết phụ tùng hậu mãi trong 24 giờ — Dân Việt](https://danviet.vn/vinfast-cam-ket-tai-viet-nam-se-cung-cap-phu-tung-hau-mai-trong-vong-24-gio-thiet-lap-tieu-chuan-moi-ve-chat-luong-20240827154902913.htm) | Mạng kho trung chuyển; mượn pin/xe thay thế | 27/08/2024 |
| 6 | [VinFast dừng một loạt chính sách hậu mãi đặc biệt — CafeF](https://cafef.vn/vinfast-dung-mot-loat-chinh-sach-hau-mai-dac-biet-cho-khach-hang-gap-su-co-sau-khi-thong-bao-xe-duoc-sac-mien-phi-them-2-nam-188241226225320197.chn) | **Đính chính:** dừng đền bù tiền mặt từ 01/01/2025; xác nhận cam kết 24h vẫn được giữ | 27/12/2024 |

## Giới hạn của các nguồn trên

* **Nguồn #1 đã gần 3 năm tuổi.** VinFast mở rộng mạng lưới trạm từ 2023 tới nay, nên mức tắc nghẽn hiện tại có thể đã khác. Đo lại là việc bắt buộc trước khi cam kết metric cho Card #1.
* **Cam kết 24h chưa xác minh được tình trạng hiện tại** — xem rủi ro đã ghi trong Card #2.
* **Có một nguồn bị loại:** phản ánh trên diễn đàn cộng đồng VinFast về việc chờ phụ tùng kéo dài không được trích dẫn, vì không truy cập được trang gốc để xác minh (lỗi 403).

*Quá trình tìm nguồn và các sai sót đã mắc được ghi trong [03-ai-log.md](03-ai-log.md).*
