# Bài thực hành 7 — Kiểm thử Mocking và CI

- Sinh viên: Vũ Thế Huỳnh
- MSSV: 2312639
- Email: vuthehuynh87@gmail.com

YummyApp gồm kiểm thử tính tiền, mã khuyến mãi theo trạng thái mạng/OS và dịch vụ GPS được mock bằng unittest.mock.patch.

## Chạy kiểm tra

```sh
python -m pip install -r requirements.txt
python -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
python -m coverage run -m unittest discover -s . -p "test_*.py"
python -m coverage report -m --fail-under=80
python -m coverage html -d coverage_html
```

Kết quả local: 15 test đạt, coverage dòng và nhánh 100%. Workflow dùng Python 3.11 trên Ubuntu, chạy khi push hoặc pull request vào main và tải báo cáo HTML lên Artifacts.

## Cấu trúc nộp bài

```text
2312639_VuTheHuynh_Lab7/
|-- .github/workflows/yummyapp-ci.yml
|-- gps_service.py
|-- yummy_app.py
|-- test_yummy_app.py
|-- requirements.txt
|-- .coveragerc
|-- logs/
|   |-- local_test.log
|   |-- git_history.log
|   |-- github_actions_run.log
|-- MinhChung_VietTay_2312639.pdf
|-- BaoCao_KetQua_Lab7.pdf
```

Mã nguồn và các file nộp bài nằm trực tiếp tại gốc repository. Bản thư mục/ZIP nộp bài được đóng gói với tên `2312639_VuTheHuynh_Lab7`. `.coveragerc` giữ cấu hình đo coverage theo module nghiệp vụ và nhánh.

Xem [báo cáo kết quả](BaoCao_KetQua_Lab7.pdf), [minh chứng viết tay 4 trang](MinhChung_VietTay_2312639.pdf) và ba file log trong `logs/`.

Raw log GitHub được tải từ [lần chạy thành công 38869623646](https://github.com/1convitt/2312639__VuTheHuynh_Lab7/actions/runs/38869623646), commit `b8570f9`: 15 test đạt, coverage 100%, artifact `YummyApp-Coverage-Report` đã tải lên. Báo cáo kèm ảnh trích log thật; ảnh chụp giao diện Actions cần bổ sung nếu giảng viên yêu cầu.

`BAO_CAO.md` là tài liệu lý thuyết tham khảo. `docs/local_failure_demo.log` ghi thử nghiệm lỗi local, không phải raw log GitHub.
