![C_healthy-logo](img/logo.png)
<p align="center"><a href="https://pypi.org/project/C-healthy/0.2.6/"><img src="https://img.shields.io/pypi/v/C-healthy.svg?color=blue&label=PyPI" alt="PyPI Version"/></a> <a href="https://github.com/trgchinhh/library-C_healthy-cpp"><img src="https://img.shields.io/badge/Language-Python%20%7C%20C%2B%2B-orange.svg" alt="Languages"/></a> <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"/></a></p>

## C_healthy

C_healthy là thư viện hỗ trợ tính toán và phân tích các chỉ số sức khỏe như BMI, BMR, TDEE cùng nhiều chỉ số nhân trắc học khác. Bên cạnh việc thực hiện các phép tính, thư viện còn tích hợp hệ thống NA (Nutrition Advice) để phân tích kết quả và đưa ra các khuyến nghị về sức khỏe và dinh dưỡng dựa trên tình trạng hiện tại của người dùng. Thư viện hiện hỗ trợ cả Python và C++.

---

## Liên kết dự án
**Pypi:** [Linh thư viện chính thức C-healthy v0.2.6](https://pypi.org/project/C-healthy/0.2.6/)<br>
**C++ (GitHub):** [library-C_healthy-cpp](https://github.com/trgchinhh/library-C_healthy-cpp)<br>
**Hướng dẫn xây dựng thư viện:** [Instruct.md](https://github.com/trgchinhh/library-C_healthy/blob/main/Instruct.md)<br>
**Bài viết trên FB:** [Bài viết chính thức trên Facebook](https://www.facebook.com/share/p/161whS2WdN/)<br>

---

## Danh mục chỉ số tính toán hỗ trợ
| Ký Hiệu | Tên Chỉ Số | Chức Năng Phân Tích |
| :--- | :--- | :--- |
| **BMI** | Body Mass Index | Chỉ số khối cơ thể (Đánh giá gầy/béo) |
| **BMR** | Basal Metabolic Rate | Tỷ lệ trao đổi chất cơ bản (Năng lượng duy trì sự sống) |
| **TDEE** | Total Daily Energy Expenditure | Tổng lượng calo tiêu thụ trong một ngày dựa trên vận động |
| **LBM** | Lean Body Mass | Khối lượng cơ thể không tính mỡ |
| **FFMI** | Fat-Free Mass Index | Chỉ số khối lượng cơ thể không mỡ (Đánh giá lượng cơ bắp) |
| **RFM** | Relative Fat Mass | Khối lượng mỡ tương đối (Đánh giá tỷ lệ mỡ nhanh qua eo/chiều cao) |
| **BFP** | Body Fat Percentage | Tỷ lệ phần trăm mỡ cơ thể |
| **IBW** | Ideal Body Weight | Trọng lượng cơ thể lý tưởng theo chiều cao |
| **WHR** | Waist-to-Hip Ratio | Tỷ lệ eo trên mông (Đánh giá phân phối mỡ, nguy cơ tim mạch) |
| **BBW** | Blood Volume / Water | Ước lượng tổng lượng nước / thể tích máu trong cơ thể |
| **MA** | Metabolic Age | Tuổi sinh học / Tuổi chuyển hóa của cơ thể |
| **VFR** | Visceral Fat Rating | Đánh giá mức độ mỡ nội tạng (Mỡ quanh cơ quan bụng) |
| **BSA** | Body Surface Area | Diện tích bề mặt cơ thể |
| **VO2MAX**| Maximal Oxygen Uptake | Tốc độ tiêu thụ oxy tối đa (Đánh giá sức bền tim mạch) |
| **HSI** | Hepatic Steatosis Index | Chỉ số sàng lọc nguy cơ gan nhiễm mỡ |
| **MMI** | Muscle Mass Index | Chỉ số khối lượng cơ bắp thuần |
| **BFM** | Body Fat Mass | Tổng khối lượng mỡ tính bằng kilôgam |

--

## Cách cài đặt và nâng cấp
```bash
pip install C_healthy
pip install --upgrade C-healthy
```
## Cách sử dụng chi tiết

1. Hàm tính toán chỉ số (trả về số thực float/double)
2. Hàm đưa ra lời khuyên (có tiền tố NA - trả về chuỗi thông báo string)
3. Hàm hướng dẫn cách dùng (INSTRUCT)

Cách dùng hàm tính chỉ số BMI, những hàm khác tương tự
```python
from C_healthy import BMI, NABMI

# Tham số BMI: cân nặng (kg), chiều cao (m)
bmi = BMI(55, 1.7) # đây là hàm tính chỉ số bmi
nabmi = NABMI(bmi) # đây là hàm trả về lời khuyên dựa trên chỉ số bmi đã tính (có tiền tố NA)

print(f"Chỉ số bmi của bạn là: {bmi}")
print("Lời khuyên:", nabmi)
```

Cách dùng hàm in ra hướng dẫn sử dụng
```python
from C_healthy import INSTRUCT

# in hết nội dung hướng dẫn ra màn hình và không ghi vào file
print(INSTRUCT())

# in ra hdsd 1 hàm và không ghi ra file
print(INSTRUCT("bmi", ghi_file=False))

# in ra hdsd 1 hàm và ghi ra file
print(INSTRUCT("bmi", ghi_file=True))

# ghi hết nội dung vào file
print(INSTRUCT(ghi_file=True))
```

Chi tiết đầy đủ cách dùng 
```python
from C_healthy import *

bmi = BMI(70, 1.75)
bmr = BMR("nam", 60, 1.75, 18)
tdee = TDEE("nam", 60, 1.75, 18, 3)
lbm = LBM("nam", 70, 1.75)
ffmi = FFMI("nam", 60, 1.7)
rfm = RFM(85, 1.7)
bfp = BFP("nam", 70, 1.75, 20)
ibw = IBW("nam", 1.75)
whr = WHR("nam", 85, 95)
bbw = BBW(60)
ma = MA("nam", 70, 1.7, 18)
vfr = VFR(85, 95)
bsa = BSA(1.7, 60)
vo2max = VO2MAX(110, 60)
hsi = HSI("nam", 60, 1.7, 18, 200, 110)
mmi = MMI("nam", 60, 1.7)
bfm = BFM("nam", 60, 1.7, 18)

print("BMI:", bmi, "\nLời khuyên:", NABMI(bmi))
print("BMR:", bmr, "\nLời khuyên:", NABMR("nam", bmr))
print("TDEE:", tdee, "\nLời khuyên:", NATDEE("nam", tdee))
print("LBM:", lbm, "\nLời khuyên:", NALBM(lbm))
print("FFMI:", ffmi, "\nLời khuyên:", NAFFMI(ffmi))
print("RFM:", rfm, "\nLời khuyên:", NARFM(rfm))
print("BFP:", bfp, "\nLời khuyên:", NABFP(bfp))
print("IBW:", ibw, "\nLời khuyên:", NAIBW(ibw))
print("WHR:", whr, "\nLời khuyên:", NAWHR(whr))
print("BBW:", bbw, "\nLời khuyên:", NABBW(bbw))
print("MA:", ma, "\nLời khuyên:", NAMA(ma))
print("VFR:", vfr, "\nLời khuyên:", NAVFR(vfr))
print("BSA:", bsa, "\nLời khuyên:", NABSA(bsa))
print("VO2MAX:", vo2max, "\nLời khuyên:", NAVO2MAX(vo2max))
print("HSI:", hsi, "\nLời khuyên:", NAHSI(hsi))
print("MMI:", mmi, "\nLời khuyên:", NAMMI(mmi))
print("BFM:", bfm, "\nLời khuyên:", NABFM(bfm))

print(INSTRUCT()) # hàm hướng dẫn 
```
---

## Tác giả
**Nguyễn Trường Chinh (NTC++)**
GitHub: [https://github.com/trgchinhh](https://github.com/trgchinhh)

---

> 📌 Dự án nhỏ được phát triển với mục đích học tập và nghiên cứu. Mọi góp ý và đóng góp đều được hoan nghênh.
