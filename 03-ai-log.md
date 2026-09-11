# 03 — AI Log & Reflection

## Lab 02: AI Product Scoping — Vin Smart Future

Trong bài lab này, tôi sử dụng AI chủ yếu như một trợ lý để mở rộng góc nhìn, kiểm tra giả định và phản biện lại chính các ý tưởng ban đầu. Tôi không bắt đầu bằng việc chọn một công nghệ AI rồi tìm chỗ để áp dụng. Trước tiên, tôi tìm các vấn đề vận hành có thật, kiểm tra xem vấn đề đó còn tồn tại hay doanh nghiệp đã giải quyết rồi, sau đó mới đánh giá AI có thực sự phù hợp hay không.

Điểm tôi thấy quan trọng nhất sau quá trình làm bài là: AI rất hữu ích để nghĩ nhanh và tìm hướng, nhưng nếu tin ngay câu trả lời đầu tiên thì rất dễ xây cả bài trên một giả định sai.

---

# 1. Bước đầu tiên: dùng AI để “Lọc ảo” trước khi SCAN

File `03-inspiration-kit.md` cung cấp nhiều ý tưởng để bắt đầu. Ban đầu, tôi có thể chọn trực tiếp một trong các ý tưởng đó rồi đi tiếp vào Phase 1. Tuy nhiên, khi dùng ChatGPT để kiểm tra lại từng đề xuất, tôi nhận ra Inspiration Kit chỉ nên được xem là **danh sách gợi ý**, không phải bằng chứng rằng doanh nghiệp hiện vẫn gặp đúng vấn đề đó.

Vì vậy, tôi thêm một bước riêng trước Phase 1 và đặt tên là **“Lọc ảo”**.

Cách tôi làm như sau:

1. Lấy từng ý tưởng trong Inspiration Kit làm giả thuyết ban đầu.
2. Yêu cầu AI tìm thêm nguồn công khai có thật liên quan đến chính công ty đó.
3. Ưu tiên các nguồn như:
   - website chính thức của doanh nghiệp;
   - quy trình vận hành công khai;
   - báo cáo thường niên;
   - trang sản phẩm;
   - tin tuyển dụng chính thức;
   - FAQ hoặc tài liệu hỗ trợ khách hàng.
4. Kiểm tra ba câu hỏi:
   - vấn đề này có thực sự tồn tại không;
   - doanh nghiệp đã có sản phẩm hoặc hệ thống giải quyết nó chưa;
   - phần nào là thông tin được xác nhận, phần nào chỉ là suy luận.
5. Chỉ giữ lại các vấn đề còn hợp lý để đưa vào SCAN.

Bước này giúp tôi loại được khá nhiều ý tưởng nghe hợp lý nhưng thực tế không còn mới.

Ví dụ, Inspiration Kit gợi ý bài toán dùng AI để tóm tắt hồ sơ bệnh án ở Vinmec. Khi research lại, tôi tìm được thông tin Vinmec đã đưa DrAid vào hỗ trợ xử lý hồ sơ và công bố thời gian tóm tắt giảm từ khoảng 5 phút xuống 1 phút. Vì vậy, nếu tôi tiếp tục đề xuất “dùng AI để tóm tắt hồ sơ Vinmec” thì gần như đang đề xuất lại một bài toán đã được doanh nghiệp triển khai.

Tương tự, ý tưởng xây trợ lý cư dân cho Vinhomes cũng không còn phù hợp ở dạng ban đầu vì Vinhomes đã có Trợ lý ảo trên Vinhomes Resident. Ngoài ra, V-PMS đã hỗ trợ giao việc và theo dõi xử lý phản ánh trong vận hành. Những phát hiện này làm tôi thay đổi cách nhìn: thay vì hỏi “ý tưởng này nghe có hay không?”, tôi chuyển sang hỏi “ý tưởng này còn có thật và còn đáng giải không?”.

Bước “Lọc ảo” là phần AI giúp tôi nhiều nhất ở giai đoạn đầu, vì nó ngăn tôi giải một bài toán tưởng tượng hoặc một bài toán đã được giải rồi.

---

# 2. AI đã giúp tôi mở rộng và thu hẹp vấn đề như thế nào?

Sau khi loại các ý tưởng không còn phù hợp, tôi tiếp tục dùng ChatGPT để tìm thêm các bài toán có thể phân tích trong VinFast, Vinpearl, Vinhomes và VinBus.

Lúc này AI giúp tôi ở hai việc.

Thứ nhất là **mở rộng phạm vi tìm kiếm**. AI giúp tôi nghĩ ra nhiều workflow khác nhau thay vì chỉ quanh quẩn ở chatbot hoặc trợ lý ảo.

Thứ hai là **so sánh và loại dần**. Với mỗi bài toán, tôi yêu cầu AI phải trả lời rõ:

- ai là người trực tiếp làm công việc đó;
- quy trình hiện tại gồm những bước nào;
- chỗ nào thực sự có khả năng gây chậm hoặc sai;
- phần nào có thể giải bằng Rule;
- phần nào mới thực sự cần LLM;
- nếu AI sai thì hậu quả là gì;
- có cần con người duyệt hay không.

Cách đặt câu hỏi này giúp tôi tránh tình trạng cứ thấy một công việc lặp lại là mặc định dùng AI.

Ví dụ, với bài toán kiểm tra CRM của Vinhomes, ban đầu có thể nghĩ tới việc dùng LLM để phát hiện lỗi. Nhưng khi phân tích kỹ hơn, tôi nhận ra khá nhiều lỗi như thiếu field bắt buộc, cập nhật trễ, sai thứ tự trạng thái hoặc sai khu vực phân phối đều có thể giải bằng Rule hoặc SQL. Trong trường hợp đó, dùng LLM làm lõi vừa tốn kém vừa khó kiểm soát hơn.

Ngược lại, bài toán VinFast liên quan đến việc đọc hiểu yêu cầu khách hàng đa kênh lại phù hợp hơn với LLM vì nội dung có thể rất tự do, dài, chứa nhiều ý cùng lúc hoặc thiếu thông tin.

Từ đó tôi chọn bài toán VinFast để đi sâu hơn.

---

# 3. AI đã trả lời sai hoặc “hallucinate” ở đâu?

Sai lầm lớn nhất của AI trong quá trình làm bài không phải là trả lời sai một chi tiết nhỏ, mà là **biến một suy luận hợp lý thành một “sự thật” nghe rất thuyết phục**.

Ví dụ, trong giai đoạn brainstorm, AI rất dễ viết những câu như:

> “Nhân viên phải xử lý hàng nghìn ticket mỗi ngày và mất 10–15 phút cho mỗi ticket.”

Câu này nghe rất hợp lý trong bối cảnh doanh nghiệp lớn, nhưng tôi không tìm được nguồn nào xác nhận số ticket hoặc thời gian xử lý như vậy.

Nếu giữ nguyên câu này rồi dùng nó để tính Business Impact, toàn bộ phần sau sẽ dựa trên một con số bịa.

Tôi đã sửa prompt bằng cách yêu cầu AI phân biệt rõ ba loại thông tin:

- **Đã xác minh:** có nguồn trực tiếp hỗ trợ.
- **Suy luận:** có cơ sở nhưng chưa được doanh nghiệp xác nhận.
- **Chưa biết:** cần dữ liệu nội bộ hoặc phỏng vấn stakeholder.

Tôi cũng thêm yêu cầu:

> Không được tự tạo ticket volume, thời gian xử lý, tỷ lệ lỗi hoặc ROI nếu không có nguồn.

Sau khi sửa prompt theo cách này, chất lượng câu trả lời thay đổi rõ. Với VinFast, tôi chỉ giữ những gì nguồn chính thức xác nhận: có bước tiếp nhận yêu cầu, phân loại, chuyển xử lý và phản hồi. Còn những thứ như “mất bao nhiêu phút”, “có bao nhiêu ticket”, “tỷ lệ chuyển sai là bao nhiêu” thì tôi ghi rõ là cần đo sau.

Đây là phần tôi thấy quan trọng nhất khi dùng AI cho product scoping: một câu trả lời nghe hợp lý chưa chắc đã là một fact.

---

# 4. Tôi đã sửa cách prompt như thế nào?

Ban đầu prompt của tôi khá mở, kiểu:

> “Hãy đề xuất các bài toán AI tiềm năng cho VinFast.”

Cách hỏi này cho nhiều ý tưởng nhưng thường quá rộng và thiên về solution.

Sau đó tôi đổi cách prompt thành từng lớp rõ hơn.

Ví dụ:

> “Đây là một ý tưởng từ Inspiration Kit. Hãy tìm nguồn chính thức để xác minh workflow này có thật không. Sau đó tìm luôn bằng chứng ngược lại xem doanh nghiệp đã có solution tương tự chưa. Không được tự tạo số liệu.”

Sau khi có nguồn:

> “Tách rõ phần nào là fact, phần nào là suy luận. Nếu problem đã được giải hoặc chưa đủ bằng chứng thì đề xuất REMOVE hoặc REFRAME, không cố giữ lại.”

Khi đánh giá AI Fit:

> “Hãy giải thích trước vì sao Rule hoặc State Machine có thể tốt hơn LLM. Chỉ chọn LLM nếu có lý do rõ ràng.”

Khi chọn bài toán cuối cùng:

> “Không được đề xuất Agent nếu một LLM Feature kết hợp Rule và Human Review đã đủ.”

Việc thay đổi prompt theo hướng này giúp AI bớt “ham AI” và thực tế hơn nhiều.

---

# 5. Tôi đã sửa ranh giới của AI như thế nào?

Sau khi chọn bài toán VinFast, tôi tiếp tục dùng AI để xác định ranh giới vận hành.

Ban đầu, nếu chỉ nói:

> “AI hỗ trợ phân loại yêu cầu khách hàng.”

thì phạm vi quá rộng. AI có thể hiểu rằng nó được quyền trả lời khách, quyết định nơi xử lý hoặc thậm chí chẩn đoán vấn đề kỹ thuật.

Tôi phải viết rõ AI được phép làm gì và không được phép làm gì.

AI được phép:

- tóm tắt nội dung;
- trích xuất thông tin;
- phân loại vấn đề;
- phát hiện thông tin còn thiếu;
- đề xuất nơi xử lý;
- cảnh báo trường hợp cần ưu tiên.

AI không được phép:

- tự chẩn đoán lỗi kỹ thuật của xe;
- quyết định bảo hành hoặc bồi thường;
- tự trả lời khách hàng cuối cùng;
- tự đóng sự vụ;
- tự thay đổi dữ liệu CRM;
- tự chuyển các trường hợp nhạy cảm mà không có người kiểm tra.

Phần này làm tôi hiểu rõ hơn rằng prompt không chỉ là “hướng dẫn model trả lời”, mà còn là cách giới hạn quyền của model.

---

# 6. Tôi đã dùng adversarial prompt như thế nào?

File `prompt_prototype.py` giúp tôi hiểu một điểm rất rõ: prompt tốt không chỉ cần chạy đúng trong trường hợp bình thường, mà còn phải chịu được lúc người dùng cố tình yêu cầu AI phá luật.

Ví dụ trong bài mẫu Xanh SM, có hai kiểu test:

- ép AI bỏ qua `[DRAFT_ONLY]`;
- ép AI hướng xe pin rất thấp tới trạm sạc quá xa.

Mục đích không phải kiểm tra AI “thông minh đến đâu”, mà kiểm tra ranh giới có giữ được không.

Từ đó, tôi thay đổi cách nghĩ về test.

Thay vì chỉ hỏi:

> “AI có trả lời đúng không?”

tôi chuyển sang hỏi:

> “Nếu người dùng cố tình gây áp lực, yêu cầu bỏ qua quy định hoặc cung cấp dữ liệu mâu thuẫn thì AI có vẫn giữ đúng giới hạn không?”

Đây là phần tôi thấy gần nhất với prompt engineering thực tế.

---

# 7. Điều tôi học được sau quá trình làm bài

Trước bài lab, tôi nghĩ prompt engineering chủ yếu là viết instruction rõ và chi tiết.

Sau quá trình này, tôi thấy một prompt tốt phải đi cùng ít nhất bốn thứ:

1. **Nguồn dữ liệu đáng tin** để tránh xây trên giả định sai.
2. **Ranh giới rõ ràng** để AI không vượt quyền.
3. **Định dạng đầu ra rõ** để có thể kiểm tra bằng chương trình.
4. **Test cố tình phá luật** để biết hệ thống có thực sự an toàn không.

Tôi cũng nhận ra AI không nên là nơi ra quyết định cuối cùng trong mọi bài toán. Có những phần Rule xử lý tốt hơn, có những phần con người bắt buộc phải giữ quyền phê duyệt.

---

# 8. Reflection cuối cùng

Phần giá trị nhất của AI trong bài lab không phải là viết giúp tôi nội dung nhanh hơn, mà là giúp tôi **mở rộng ý tưởng rồi tự phản biện lại chúng**.

Tôi dùng AI để:

- brainstorm;
- tìm hướng research;
- so sánh các bài toán;
- tìm counter-evidence;
- kiểm tra xem Rule có tốt hơn LLM không;
- thiết kế ranh giới;
- tạo adversarial test.

Nhưng tôi cũng phải liên tục kiểm tra lại AI vì nó rất dễ đưa ra các con số hoặc quy trình nghe hợp lý nhưng không có bằng chứng.

Từ bài này, cách tôi dùng AI thay đổi khá rõ:

> **AI không phải nguồn sự thật. AI là trợ lý để đặt giả thuyết, tìm hướng và phản biện. Phần còn lại phải được kiểm chứng bằng evidence, rule và test.**

Đó cũng là lý do tôi thêm bước “Lọc ảo” trước Phase 1. Nếu bước đó không có, rất có thể tôi đã chọn một bài toán nghe hay nhưng thực tế doanh nghiệp đã giải rồi.

---

# Nguồn dùng để kiểm chứng trong quá trình làm bài

1. VinFast — Quy trình tiếp nhận, phản hồi và giải quyết phản ánh/yêu cầu/khiếu nại của khách hàng.  
   https://vinfastauto.com/vn_vi/quy-trinh-tiep-nhan-phan-hoi-thong-tin-va-giai-quyet-phan-anh-yeu-cau-khieu-nai-cua-khach-hang

2. Vinmec — DrAid và cải tiến xử lý hồ sơ y tế.  
   https://www.vinmec.com/vie/bai-viet/dot-pha-cong-nghe-ai-tai-vinmec-tiet-kiem-80-thoi-gian-xu-ly-ho-so-y-te

3. Vinhomes — Trợ lý ảo trên Vinhomes Resident và Vinhomes Online.  
   https://market.vinhomes.vn/blog/ra-mat-tro-ly-ao-tren-ung-dung-vinhomes-resident-va-vinhomes-online

4. Vinhomes Annual Report 2024 — thông tin về V-PMS.  
   https://vinhomes.vn/vi/bao-cao-thuong-nien

5. Inspiration Kit của Lab:  
   `S:\ai20k\VinUni\_Codelab_Day02_Template\03-inspiration-kit.md`
