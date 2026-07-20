<p align="center">
  <img src="img/logo.png"/>
</p>

<p align="center">
  <a href="https://pepy.tech/projects/C_healthy">
    <img src="https://static.pepy.tech/badge/C_healthy" alt="Downloads"/>
  </a>
  <a href="https://pypi.org/project/C-healthy/0.3.0/">
    <img src="https://img.shields.io/pypi/v/C-healthy.svg?color=blue&label=PyPI" alt="PyPI Version"/>
  </a>
  <a href="https://github.com/trgchinhh/library-C_healthy-cpp">
    <img src="https://img.shields.io/badge/Language-Python-orange.svg" alt="Language"/>
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"/>
  </a>
  <a href="https://github.com/trgchinhh">
    <img src="https://img.shields.io/badge/Author-Tr%C6%B0%E1%BB%9Dng%20Chinh-blueviolet" alt="Author"/>
  </a>
</p>

## C-healthy

C_healthy là thư viện hỗ trợ tính toán và phân tích các chỉ số sức khỏe như BMI, BMR, TDEE cùng nhiều chỉ số nhân trắc học khác. Bên cạnh việc thực hiện các phép tính, thư viện còn tích hợp hệ thống NA (Nutrition Advice) để phân tích kết quả và đưa ra các khuyến nghị về sức khỏe và dinh dưỡng dựa trên tình trạng hiện tại của người dùng. Thư viện hiện hỗ trợ cả Python và C++.

---

## Liên kết dự án
**Pypi:** [Linh thư viện chính thức C-healthy v0.3.0](https://pypi.org/project/C-healthy/0.3.0/)<br>
**C++ (GitHub):** [library-C_healthy-cpp](https://github.com/trgchinhh/C_healthy-cpp)<br>
**Hướng dẫn xây dựng thư viện:** [Instruct.md](https://github.com/trgchinhh/C_healthy/blob/main/INSTRUCT.md)<br>
**Bài viết trên FB:** [Bài viết chính thức trên Facebook](https://www.facebook.com/share/p/161whS2WdN/)<br>

<!--
---

## Số sao
<a href="https://www.star-history.com/?repos=trgchinhh%2FC_healthy&type=date&legend=bottom-right">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=trgchinhh/C_healthy&type=date&theme=dark&legend=bottom-right&sealed_token=jfn3Ybok43PjkJIpsTi0s-wFWkB2SB2jkaGlyJc83mVE0Vm_RjiFasJpBsQPp7o5vPZj4H6sRFVaqzlqPBNe_0KOAdzc6ObfzJqDjeEsiLNzhq1jzAKcruzCqPCjdlYkjUM8yKCgL88dbwK3ABlKh5274o1TfmZunU02DU17-IcycrP-JdcgRlIbrUOF" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=trgchinhh/C_healthy&type=date&legend=bottom-right&sealed_token=jfn3Ybok43PjkJIpsTi0s-wFWkB2SB2jkaGlyJc83mVE0Vm_RjiFasJpBsQPp7o5vPZj4H6sRFVaqzlqPBNe_0KOAdzc6ObfzJqDjeEsiLNzhq1jzAKcruzCqPCjdlYkjUM8yKCgL88dbwK3ABlKh5274o1TfmZunU02DU17-IcycrP-JdcgRlIbrUOF" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=trgchinhh/C_healthy&type=date&legend=bottom-right&sealed_token=jfn3Ybok43PjkJIpsTi0s-wFWkB2SB2jkaGlyJc83mVE0Vm_RjiFasJpBsQPp7o5vPZj4H6sRFVaqzlqPBNe_0KOAdzc6ObfzJqDjeEsiLNzhq1jzAKcruzCqPCjdlYkjUM8yKCgL88dbwK3ABlKh5274o1TfmZunU02DU17-IcycrP-JdcgRlIbrUOF" />
 </picture>
</a>
-->
---

## Danh mục chỉ số tính toán hỗ trợ

| Ký Hiệu | Tên Chỉ Số | Chức Năng Phân Tích |
|:---:|:---|:---|
| **BMI** | Body Mass Index | Chỉ số khối cơ thể (Đánh giá gầy, bình thường, thừa cân, béo phì) |
| **BMR** | Basal Metabolic Rate | Tỷ lệ chuyển hóa cơ bản (Lượng calo cơ thể tiêu hao khi nghỉ ngơi) |
| **TDEE** | Total Daily Energy Expenditure | Tổng năng lượng tiêu hao trong một ngày |
| **LBM** | Lean Body Mass | Khối lượng cơ thể không bao gồm mỡ |
| **FFMI** | Fat-Free Mass Index | Chỉ số khối lượng cơ thể không mỡ (Đánh giá mức phát triển cơ bắp) |
| **RFM** | Relative Fat Mass | Chỉ số mỡ tương đối dựa trên chiều cao và vòng eo |
| **BFP** | Body Fat Percentage | Tỷ lệ phần trăm mỡ cơ thể |
| **IBW** | Ideal Body Weight | Cân nặng lý tưởng theo chiều cao |
| **WHR** | Waist-to-Hip Ratio | Tỷ lệ vòng eo trên vòng hông (Đánh giá nguy cơ tim mạch) |
| **BBW** | Body Water Requirement | Ước tính nhu cầu nước của cơ thể |
| **MA** | Metabolic Age | Tuổi chuyển hóa của cơ thể |
| **VFR** | Visceral Fat Rating | Đánh giá mức độ mỡ nội tạng |
| **BSA** | Body Surface Area | Diện tích bề mặt cơ thể |
| **VO2MAX** | Maximal Oxygen Uptake | Khả năng hấp thụ oxy tối đa |
| **HSI** | Hepatic Steatosis Index | Chỉ số sàng lọc nguy cơ gan nhiễm mỡ |
| **MMI** | Muscle Mass Index | Chỉ số khối lượng cơ bắp |
| **BFM** | Body Fat Mass | Khối lượng mỡ cơ thể (kg) |
| **ABSI** | A Body Shape Index | Chỉ số hình dáng cơ thể dựa trên BMI và vòng eo |
| **AVI** | Abdominal Volume Index | Chỉ số thể tích vùng bụng |
| **BAI** | Body Adiposity Index | Chỉ số mỡ cơ thể dựa trên vòng hông |
| **CI** | Conicity Index | Chỉ số hình nón (Đánh giá béo bụng) |
| **WHtR** | Waist-to-Height Ratio | Tỷ lệ vòng eo trên chiều cao |
| **PI** | Ponderal Index | Chỉ số Ponderal (Đánh giá thể trạng theo chiều cao) |
| **FMI** | Fat Mass Index | Chỉ số khối lượng mỡ |
| **FFM** | Fat-Free Mass | Khối lượng cơ thể không mỡ |
| **FMR** | Fat Mass Ratio | Tỷ lệ giữa khối lượng mỡ và khối lượng không mỡ |
| **TBW** | Total Body Water | Tổng lượng nước trong cơ thể |
| **ECW** | Extracellular Water | Lượng nước ngoài tế bào |
| **ICW** | Intracellular Water | Lượng nước trong tế bào |
| **BCM** | Body Cell Mass | Khối lượng tế bào hoạt động |
| **SMI** | Skeletal Muscle Index | Chỉ số khối cơ xương |
| **ASMI** | Appendicular Skeletal Muscle Index | Chỉ số khối cơ xương tứ chi |
| **MAMC** | Mid-Upper Arm Muscle Circumference | Chu vi cơ cánh tay giữa |
| **MUAC** | Mid-Upper Arm Circumference Assessment | Đánh giá dinh dưỡng qua chu vi cánh tay |
| **BEE** | Basal Energy Expenditure | Tiêu hao năng lượng cơ bản |
| **REE** | Resting Energy Expenditure | Tiêu hao năng lượng khi nghỉ ngơi |
| **PAL** | Physical Activity Level | Hệ số mức độ hoạt động thể chất |
| **MET** | Metabolic Equivalent of Task | Đương lượng chuyển hóa của hoạt động |
| **MHR** | Maximum Heart Rate | Nhịp tim tối đa theo độ tuổi |
| **HRR** | Heart Rate Reserve | Dự trữ nhịp tim |
| **THR** | Target Heart Rate | Nhịp tim mục tiêu khi tập luyện |
| **CalDef** | Calorie Deficit | Mức thâm hụt calo để giảm cân |
| **CalSur** | Calorie Surplus | Mức dư calo để tăng cân |
| **ProtNeed** | Protein Requirement | Nhu cầu Protein hằng ngày |
| **FatNeed** | Fat Requirement | Nhu cầu chất béo hằng ngày |
| **CarbNeed** | Carbohydrate Requirement | Nhu cầu Carbohydrate hằng ngày |
| **WaterNeed** | Water Requirement | Nhu cầu nước uống mỗi ngày |
| **IdealWater** | Ideal Water Intake | Lượng nước lý tưởng theo cân nặng |
| **LBP** | Lean Body Percentage | Tỷ lệ phần trăm khối lượng không mỡ |
| **MP** | Muscle Percentage | Tỷ lệ phần trăm cơ bắp |
| **BME** | Bone Mass Estimate | Ước tính khối lượng xương |
| **BMIP** | BMI Prime | Chỉ số BMI Prime (So sánh BMI với mức chuẩn 25) |
| **FatMass** | Fat Mass | Khối lượng mỡ cơ thể (kg) được tính từ cân nặng và tỷ lệ mỡ cơ thể |
| **LeanMass** | Lean Mass | Khối lượng nạc của cơ thể (Khối lượng cơ thể không bao gồm mỡ) |
| **GenderTest** | Gender Validation | Kiểm tra và chuẩn hóa giới tính đầu vào trước khi tính toán các chỉ số |
| **ABRI** | Advanced Body Roundness Index | Chỉ số độ tròn cơ thể mở rộng (Biến thể nâng cao của Body Roundness Index để đánh giá hình dáng cơ thể) |
| **BRI** | Body Roundness Index | Chỉ số độ tròn cơ thể |
| **VAI** | Visceral Adiposity Index | Chỉ số mỡ nội tạng chuyên sâu |
| **LAP** | Lipid Accumulation Product | Chỉ số tích lũy lipid |

---

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
print(INSTRUCT("bmi", write_file = False))

# in ra hdsd 1 hàm và ghi ra file
print(INSTRUCT("bmi", write_file = True))

# ghi hết nội dung vào file
print(INSTRUCT(write_file = True))
```

Chi tiết đầy đủ cách dùng 
```python
import C_healthy
from C_healthy import *

bmi = BMI(70, 1.75)
bmr = BMR("male", 60, 1.75, 18)
tdee = TDEE("male", 60, 1.75, 18, 3)
lbm = LBM("male", 70, 1.75)
ffmi = FFMI("male", 60, 1.7)
rfm = RFM(85, 1.7)
bfp = BFP("male", 70, 1.75, 20)
ibw = IBW("male", 1.75)
whr = WHR("male", 85, 95)
bbw = BBW(60)
ma = MA("male", 70, 1.7, 18)
vfr = VFR(85, 95)
bsa = BSA(1.7, 60)
vo2max = VO2MAX(110, 60)
hsi = HSI("male", 60, 1.7, 18, 200, 110)
mmi = MMI("male", 60, 1.7)
bfm = BFM("male", 60, 1.7, 18)
absi = ABSI(85, 70, 1.75)
avi = AVI(85, 95)
bai = BAI(95, 1.75)
ci = CI(70, 1.75, 85)
whtr = WHtR(85, 1.75)
pi = PonderalIndex(70, 1.75)
fmi = FMI("male", 70, 1.75, 20)
ffm = FFM("male", 70, 1.75)
fmr = FMR("male", 70, 1.75, 20)
tbw = TBW("male", 70, 1.75, 20)
ecw = ECW("male", 70, 1.75, 20)
icw = ICW("male", 70, 1.75, 20)
bcm = BCM("male", 70, 1.75, 20)
smi = SMI("male", 70, 1.75)
asmi = ASMI("male", 70, 1.75)
mamc = MAMC(28.0, 12.0)
muac_assess = MUAC_Assessment("male", 28.0)
bee = BEE("male", 70, 1.75, 20)
ree = REE("male", 70, 1.75, 20)
pal = PAL("male", 70, 1.75, 20, 3)
met = MET(14.0)
mhr = MaxHeartRate(20)
hrr = HeartRateReserve(60, 20)
thr = TargetHeartRate(60, 20, 0.7)
cal_deficit = CalorieDeficit(2100.0, 500)
cal_surplus = CalorieSurplus(2100.0, 300)
p_need = ProteinNeed(70, "high") 
f_need = FatNeed(2100.0, 0.25)
c_need = CarbNeed(2100.0, p_need, f_need)
w_need = WaterNeed(70, 60)
ideal_w = IdealWater(70)
lbp = LeanBodyPercentage("male", 70, 1.75)
fp = FatPercentage("male", 70, 1.75, 20)
mp = MusclePercentage("male", 70, 1.75)
bm_est = BoneMassEstimate("male", 70, 1.75)
bmi_prime = BMIPrime(70, 1.75)
corp_idx = CorpulenceIndex(70, 1.75)
rfm_ext = RelativeFatMass_Ext("male", 85, 1.75)
bri = BodyRoundnessIndex(85, 1.75)
abri = ABodyRoundness(85, 1.75)
vai = VisceralAdiposityIndex("male", 70, 1.75, 85, 1.5, 1.2)
lap = LipidAccumulationProduct("male", 85, 1.5)
fat_mass = FatMass("male", 70, 1.75, 20)
lean_mass = LeanMass("male", 70, 1.75)

print("BMI:", bmi, "\nAdvice:", NABMI(bmi))
print("BMR:", bmr, "\nAdvice:", NABMR("male", bmr))
print("TDEE:", tdee, "\nAdvice:", NATDEE("male", tdee))
print("LBM:", lbm, "\nAdvice:", NALBM(lbm))
print("FFMI:", ffmi, "\nAdvice:", NAFFMI(ffmi))
print("RFM:", rfm, "\nAdvice:", NARFM(rfm))
print("BFP:", bfp, "\nAdvice:", NABFP(bfp))
print("IBW:", ibw, "\nAdvice:", NAIBW(ibw))
print("WHR:", whr, "\nAdvice:", NAWHR(whr))
print("BBW:", bbw, "\nAdvice:", NABBW(bbw))
print("MA:", ma, "\nAdvice:", NAMA(ma))
print("VFR:", vfr, "\nAdvice:", NAVFR(vfr))
print("BSA:", bsa, "\nAdvice:", NABSA(bsa))
print("VO2MAX:", vo2max, "\nAdvice:", NAVO2MAX(vo2max))
print("HSI:", hsi, "\nAdvice:", NAHSI(hsi))
print("MMI:", mmi, "\nAdvice:", NAMMI(mmi))
print("BFM:", bfm, "\nAdvice:", NABFM(bfm))
print("ABSI:", absi, "\nAdvice:", NAABSI(absi))
print("AVI:", avi, "\nAdvice:", NAAVI(avi))
print("BAI:", bai, "\nAdvice:", NABAI(bai))
print("CI:", ci, "\nAdvice:", NACI(ci))
print("WHtR:", whtr, "\nAdvice:", NAWHtR(whtr))
print("Ponderal Index:", pi, "\nAdvice:", NAPonderalIndex(pi))
print("FMI:", fmi, "\nAdvice:", NAFMI(fmi))
print("FFM:", ffm, "\nAdvice:", NAFFM(ffm))
print("FMR:", fmr, "\nAdvice:", NAFMR(fmr))
print("TBW:", tbw, "\nAdvice:", NATBW(tbw))
print("ECW:", ecw, "\nAdvice:", NAECW(ecw))
print("ICW:", icw, "\nAdvice:", NAICW(icw))
print("BCM:", bcm, "\nAdvice:", NABCM(bcm))
print("SMI:", smi, "\nAdvice:", NASMI(smi))
print("ASMI:", asmi, "\nAdvice:", NAASMI(asmi))
print("MAMC:", mamc, "\nAdvice:", NAMAMC(mamc))
print("MUAC Assessment:", muac_assess, "\nAdvice:", NAMUAC(muac_assess))
print("BEE:", bee, "\nAdvice:", NABEE(bee))
print("REE:", ree, "\nAdvice:", NAREE(ree))
print("PAL:", pal, "\nAdvice:", NAPAL(pal))
print("MET:", met, "\nAdvice:", NAMET(met))
print("Max HR:", mhr, "\nAdvice:", NAMaxHeartRate(mhr))
print("HRR:", hrr, "\nAdvice:", NAHeartRateReserve(hrr))
print("Target HR:", thr, "\nAdvice:", NATargetHeartRate(thr))
print("Calorie Deficit:", cal_deficit, "\nAdvice:", NACalorieDeficit(cal_deficit))
print("Calorie Surplus:", cal_surplus, "\nAdvice:", NACalorieSurplus(cal_surplus))
print("Protein Need:", p_need, "\nAdvice:", NAProteinNeed(p_need))
print("Fat Need:", f_need, "\nAdvice:", NAFatNeed(f_need))
print("Carb Need:", c_need, "\nAdvice:", NACarbNeed(c_need))
print("Water Need (w/ exercise):", w_need, "\nAdvice:", NAWaterNeed(w_need))
print("Ideal Water:", ideal_w, "\nAdvice:", NAIdealWater(ideal_w))
print("Lean Body Percentage:", lbp, "\nAdvice:", NALeanBodyPercentage(lbp))
print("Fat Percentage:", fp, "\nAdvice:", NAFatPercentage(fp))
print("Muscle Percentage:", mp, "\nAdvice:", NAMusclePercentage(mp))
print("Bone Mass Estimate:", bm_est, "\nAdvice:", NABoneMassEstimate(bm_est))
print("BMI Prime:", bmi_prime, "\nAdvice:", NABMIPrime(bmi_prime))
print("Corpulence Index:", corp_idx, "\nAdvice:", NACorpulenceIndex(corp_idx))
print("RFM Ext:", rfm_ext, "\nAdvice:", NARelativeFatMass(rfm_ext))
print("BRI:", bri, "\nAdvice:", NABodyRoundnessIndex(bri))
print("ABRI:", abri, "\nAdvice:", NAABodyRoundness(abri))
print("VAI:", vai, "\nAdvice:", NAVisceralAdiposityIndex(vai))
print("LAP:", lap, "\nAdvice:", NALipidAccumulationProduct(lap))
print("Fat Mass:", fat_mass, "\nAdvice:", NAFatMass(fat_mass))
print("Lean Mass:", lean_mass, "\nAdvice:", NALeanMass(lean_mass))

# Phiên bản 
print("C_healthy Version:", C_healthy.__version__)

# Nội dung hướng dẫn
print(INSTRUCT())
```
---

## Tác giả
**Nguyễn Trường Chinh (NTC++)**<br>
**GitHub:** [https://github.com/trgchinhh](https://github.com/trgchinhh)

---

> 📌 Dự án nhỏ được phát triển với mục đích học tập và nghiên cứu. Mọi góp ý và đóng góp đều được hoan nghênh.
