# Thư viện tính chỉ số cơ thể Python

### Phiên bản mới nhất trên Pypi: [Version 0.2.6](https://pypi.org/project/C-healthy/0.2.6/)
### Phiên bản C++: [Xem tại đây](https://github.com/trgchinhh/library-C_healthy-Cpp)

### Link bài viết: [Xem bài viết tại đây](https://www.facebook.com/share/p/161whS2WdN/)

### Cách tạo thư viện: [Xem hướng dẫn tại đây](https://github.com/trgchinhh/library-C_healthy/blob/main/Instruct.md)

## Tính năng 
C_healthy là thư viện Python để tính toán các chỉ số sức khỏe (BMI, BMR, TDEE, và nhiều chỉ số khác) và đồng thời đưa ra lời khuyên với chỉ số cơ thể hiện tại 

## Cách cài đặt và nâng cấp 
```bash
Cài đặt: pip install C_healthy
Nâng cấp: pip install --upgrade C-healthy
```

## Cách sử dụng 
```bash
# version 0.2.6

import C_healthy
from C_healthy import *

# Các hàm NA: đưa ra lời khuyên dựa trên chỉ số cơ thể  

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

print("Version: ",C_healthy.__version__)
```
