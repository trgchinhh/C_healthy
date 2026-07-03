# HƯỚNG DẪN TẠO THƯ VIỆN PYTHON 

## BƯỚC 1: TẠO FOLDER THEO CẤU TRÚC DƯỚI ĐÂY

```bash
my_library/
├── my_library/
│   ├── __init__.py
│   ├── file_module1.py
│   ├── file_module2.py
│   └── file_module....py
├── .gitignore 
├── setup.py
├── README.md
└── LICENSE

- Với my_library: là folder chính chứa hàm chính của thư viện
- file_module: các file tạo chương trình 
- __init__: file khởi tạo câu lệnh chính của thư viện
- setup: file chứa thông tin như version, tên thư viện, tên tác giả,...
- README.md: cách sử dụng thư viện 
- LICENSE: bản quyền, xác định quyền sử dụng.
```

## BƯỚC 2: ĐÓNG GÓI THƯ VIỆN 

```bash
- Đóng gói thư viện bằng lệnh: python setup.py sdist bdist_wheel
- Lưu ý: chuyển vào folder thư viện chổ có file setup.py trước khi dùng lệnh
```

## BƯỚC 3: UP THƯ VIỆN LÊN TRANG CHỦ 

```bash
- Lưu ý: bạn phải có tài khoản pypi trước khi up 
- Đăng ký tại đây: https://pypi.org/account/register/
- Sau khi tạo tài khoản thì vào đây để tạo api token: https://pypi.org/manage/account/ 
- Api sẽ có dạng: pypi-AgEIcHlwaS5vcmcC...
- Sau khi build ở bước 2 thì tiếp tục bằng lệnh: python -m twine upload dist/* --username __token__ --password <API_token_của_bạn>
```

# Cuối cùng 
```bash
- Lưu ý: nếu muốn nâng cấp version thì +1 vào version hiện tại ví dụ như 0.2.1 thành 0.2.2 thay lẫn trong file 'setup' và 'init'
- Không được để lộ API PYPI
```
## CHÚC CÁC BẠN THÀNH CÔNG !!!
