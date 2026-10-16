# Bài thực hành 7 — YummyApp

- Họ tên: Vũ Thế Huỳnh
- MSSV: 2312639
- Email: vuthehuynh87@gmail.com
- Repository dự kiến: https://github.com/1convitt/2312639__VuTheHuynh_Lab7

Tài liệu tham khảo để thực hiện bài và tự viết tay. Chưa thay thế minh chứng cá nhân hoặc báo cáo nộp cuối cùng.

## Sơ đồ cần vẽ tay (trang 1)

Git Push Event → Checkout Code → Setup Python 3.11 → Install Dependencies → Execute Unit Tests → Quality Gate.

Pipeline thực tế đặt Linter sau Install Dependencies và trước Execute Unit Tests; sau Quality Gate là bước tải báo cáo HTML lên Artifacts. Khi kiểm tra thất bại, job báo Failed. Quality Gate yêu cầu coverage ≥80%.

Mỗi trang viết tay cần Họ tên, MSSV, ngày thực hành và chữ ký tươi bằng mực xanh theo đề.

## Ma trận test cần tự kẻ (trang 2)

| Tên test | Hàm được gọi | Đối tượng và giá trị giả lập | Kết quả kỳ vọng |
|---|---|---|---|
| Online hợp lệ | apply_promo_code(100000, "GIAM10") | network_status="online" | 90000 |
| Offline | apply_promo_code(100000, "GIAM10") | network_status="offline" | ConnectionError |
| Mã đặc biệt OS 15 | apply_promo_code(100000, "NEW_OS_ONLY") | os_version=15 | 80000 |
| Mã đặc biệt OS 14 | apply_promo_code(100000, "NEW_OS_ONLY") | os_version=14 | ValueError |
| GPS trong vùng | get_nearby_restaurants() | patch yummy_app.gps_service.get_current_location trả (10.0, 105.0) | Hai nhà hàng trong dữ liệu |
| GPS ngoài vùng | get_nearby_restaurants() | patch trả (20.0, 110.0) | [] |
| Mất GPS | get_nearby_restaurants() | patch có side_effect=GPSSignalLostError | "Khong the xac dinh vi tri." |

Các trường hợp mạng và OS dùng trạng thái đối tượng để mô phỏng môi trường vì mã khởi tạo không thực hiện gọi API mạng. Ba test GPS dùng unittest.mock.patch và kiểm tra hàm được gọi đúng một lần.

## Câu hỏi (trang 3–4)

### Câu 2.1

Linter phát hiện nhanh lỗi cú pháp, tên chưa định nghĩa và lỗi tĩnh trước khi chạy bộ test. Đặt bước này trước test giúp phản hồi sớm, tránh tốn thời gian chạy các bước tiếp theo khi mã chưa hợp lệ.

### Câu 2.2

coverage report --fail-under=80 so sánh độ phủ với ngưỡng. Nếu dưới ngưỡng, coverage trả exit code 2; nếu đạt và không có lỗi khác, trả 0. Shell của bước run trên GitHub Actions coi mã thoát khác 0 là thất bại. Job báo Failed và các bước sau mặc định bị bỏ qua, trừ bước có điều kiện phù hợp như always(). Muốn chặn merge thực sự, phải cấu hình kiểm tra bắt buộc trong ruleset hoặc bảo vệ nhánh.

### Câu 2.3

-m hiển thị cột Missing với số dòng chưa được thực thi. Khi bật branch coverage, báo cáo còn thể hiện nhánh chưa được đi qua. Kỹ sư dựa vào đó để bổ sung tình huống kiểm thử có ý nghĩa thay vì chỉ tăng số lượng test.

### Câu 3.1

Flaky test có thể lúc đạt lúc thất bại khi mã và đầu vào không đổi, thường do thời gian, mạng, ngẫu nhiên hoặc trạng thái dùng chung. Ví dụ test gọi GPS thật đôi lúc thất bại vì mất tín hiệu; patch giúp kiểm soát đầu vào. Sai lệch phụ thuộc là sự khác nhau về phiên bản thư viện, Python hoặc hệ điều hành giữa các môi trường; lỗi có thể tái hiện ổn định trong một môi trường cụ thể.

### Câu 3.2

Ghim phiên bản giúp các lần cài dùng cùng phiên bản phụ thuộc trực tiếp, giảm lỗi do cập nhật ngoài ý muốn và thuận tiện truy vết. requirements.txt của đề ghim requests, coverage, flake8. Để tái lập chặt chẽ hơn cần khóa cả phụ thuộc gián tiếp, kiểm soát phiên bản Python và có thể xác minh hash gói.

### Câu 3.3 — Sáu bước nâng cấp an toàn

1. Tạo nhánh riêng từ main đã cập nhật.
2. Đọc release notes, thay đổi phá vỡ tương thích và yêu cầu Python của phiên bản mới.
3. Cập nhật phiên bản ghim cùng các phụ thuộc liên quan trong môi trường sạch.
4. Chạy linter, unit test, test tích hợp phù hợp và kiểm tra quality gate; sửa vấn đề trên nhánh.
5. Tạo Pull Request, xem diff và kết quả CI; yêu cầu review trước khi merge.
6. Merge sau khi kiểm tra đạt; theo dõi kết quả và revert commit/PR nếu phát sinh lỗi.

## Minh chứng

- Git cần tác giả là MSSV - Họ tên và email cá nhân; không dùng thông tin giả.
- Push repo công khai và chụp Actions xanh ban đầu.
- Chạy bộ test ban đầu với ngưỡng 80% để ghi nhận CI đỏ; bổ sung test rồi ghi nhận xanh.
- Trên nhánh thực hành, tạo lỗi cú pháp, push để Linter đỏ; sửa và push để xanh. Không để lỗi trong main.
- Xuất git log --graph --pretty=format:"%h - %an (%ad): %s" vào logs/git_history.log sau các commit.
- Tải raw log lần Actions xanh cuối cùng vào logs/github_actions_run.log; không thay bằng log local.
- Chụp/scan bốn trang viết tay của chính bạn thành MinhChung_VietTay_MSSV.pdf.
- Báo cáo BaoCao_KetQua_Lab7.pdf cần thông tin cá nhân, link repo, link run, ảnh CI đỏ/xanh, kết quả coverage và ảnh artifact.
- Nén thư mục hoàn thiện thành MSSV_HoTen_Lab7.zip; chỉ tạo bản nộp cuối khi đủ các minh chứng.

## Chạy lại cục bộ

Kết quả đã kiểm tra: 15 test đạt, coverage dòng và nhánh 100%, quality gate đạt. Log nằm ở logs/local_test.log; báo cáo HTML ở coverage_html/index.html. Môi trường local là Python 3.12; workflow cấu hình Python 3.11 theo đề. Linter local dùng thêm --jobs=1 để tránh giới hạn tạo tiến trình của môi trường chạy.

docs/local_failure_demo.log ghi thử nghiệm thật trong thư mục tạm: bộ bốn test ban đầu không vượt gate, lỗi cú pháp bị Linter phát hiện. Đây là minh họa local, không thay thế bằng chứng đỏ/xanh trên GitHub.

Tại thư mục dự án, dùng Python môi trường ảo đã cài requirements.txt:

```powershell
python -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
python -m coverage run -m unittest discover -s . -p "test_*.py"
python -m coverage report -m
python -m coverage html -d coverage_html
python -m coverage report --fail-under=80
```
