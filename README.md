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

Xem BAO_CAO.md và logs/local_test.log. Minh chứng viết tay, ảnh CI và raw log GitHub cần được bổ sung sau khi thực hiện thực tế.
