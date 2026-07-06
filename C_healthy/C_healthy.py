#   _____      _    _            _ _   _            
#  / ____|    | |  | |          | | | | |           
# | |   ______| |__| | ___  __ _| | |_| |__  _   _ 
# | |  |______|  __  |/ _ \/ _` | | __| '_ \| | | |  Healthy library for Python
# | |____     | |  | |  __/ (_| | | |_| | | | |_| |  Version 0.3.0
#  \_____|    |_|  |_|\___|\__,_|_|\__|_| |_|\__, |  Github: https:github.com/trgchinhh/library-C_healthy
#                                             __/ |
#                                            |___/ 
# (!) PROGRAM: BODY INDEX CALCULATOR
# (!) AUTHOR: NGUYEN TRUONG CHINH (NTC++)

# /**************************************************************************\
#  * Update new version [0.2.9] -> [0.3.0]
#  * Feature: including indexing and giving advice
#  * This URL lib C-heathy: https://github.com/trgchinhh/library-C_healthy
#  * We will update this library soon
# \**************************************************************************/


import math, os


def BMI(weight : int, height : float):
    try:
        if(weight > 0 and height > 0):
            return round(weight / (height ** 2), 2)
        else:
            return "Invalid input"   
    except Exception as e:
        raise ValueError(f"[{e}]")


def BMR(gender, weight, height, age):
    if(not GenderTest(gender)):
        return("Allowed genders: ['male', 'female']\nPlease re-enter the correct syntax")
    try:
        if(weight > 0 and height > 0 and age > 0):
            height = height * 100
            if(gender.lower() == "female"):
                return round((655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)), 2)
            else:
                return round((66 + (13.7 * weight) + (5 * height) - (6.8 * age)), 2) 
        else:
            return "Invalid input"
    except Exception as e:
        raise ValueError(f"[{e}]")


def TDEE(gender, weight, height, age, activity_index_R):
    try:
        if(not GenderTest(gender)):
            return("Allowed genders: ['male', 'female']\nPlease re-enter the correct syntax")
        activity_factors = {
            1: 1.2,
            2: 1.375,
            3: 1.55,
            4: 1.725,
            5: 1.9
        }
        bmr_value = BMR(gender, weight, height, age)
        if(activity_index_R in activity_factors):
            return round((bmr_value * activity_factors[activity_index_R]), 2)
        else:
            valid_keys = ", ".join(str(k) for k in activity_factors.keys())
            raise ValueError(f"Invalid activity index! Choose 1 from the following values: {valid_keys}")
    except Exception as e:
        raise ValueError(f"[{e}]")


def WHR(gender, waist_circ, hip_circ):
    try:
        if(not GenderTest(gender)):
            return("Allowed genders: ['male', 'female']\nPlease re-enter the correct syntax")
        if(waist_circ <= 0 or hip_circ <= 0):
            return "Invalid input"
        return round((waist_circ / hip_circ), 2)
    except Exception as e:
        raise ValueError(f"[{e}]") 


def LBM(gender, weight, height):
    try:
        if(not GenderTest(gender)):
            return("Allowed genders: ['male', 'female']\nPlease re-enter the correct syntax")
        height = height * 100    
        if(gender.lower() == "male"):
            lbm = round(((0.32810 * weight) + (0.33929 * height) - 29.5336), 2)
        else:
            lbm = round(((0.29569 * weight) + (0.41813 * height) - 43.2933), 2) 
        return lbm    
    except Exception as e:
        raise ValueError(f"[{e}]")


def FFMI(gender, weight, height):
    try:
        if(not GenderTest(gender)):
            return("Allowed genders: ['male', 'female']\nPlease re-enter the correct syntax")
        lbm = LBM(gender, weight, height)
        ffmi = round(lbm / (height**2), 2)
        return ffmi
    except Exception as e:
        raise ValueError(f"[{e}]")


def RFM(waist_circ, height):
    try:
        height = height * 100
        rfm = round(64 - (4 * (waist_circ / height)), 2)
        return rfm
    except Exception as e:
        raise ValueError(f"[{e}]")


def BFP(gender, weight, height, age):
    try:
        if(not GenderTest(gender)):
            return("Allowed genders: ['male', 'female']\nPlease re-enter the correct syntax")
        bmi = BMI(weight, height) 
        if(gender.lower() == "male"):
            bfp = round((1.20 * bmi) + (0.23 * age) - 16.2, 2)
        else:
            bfp = round((1.20 * bmi) + (0.23 * age) - 5.4, 2)
        return bfp
    except Exception as e:
        raise ValueError(f"[{e}]")


def BBW(weight):
    try:
        water_volume = round(weight * 0.033, 2)
        return water_volume
    except Exception as e:
        raise ValueError(f"[{e}]")


def IBW(gender, height):
    try:
        if(not GenderTest(gender)):
            return("Allowed genders: ['male', 'female']\nPlease re-enter the correct syntax")
        height = height * 100
        if(gender.lower() == "male"):
            ibw = round(50 + 2.3 * (height - 152.4) / 2.54, 2)
        else:
            ibw = round(45.5 + 2.3 * (height - 152.4) / 2.54, 2)
        return ibw
    except Exception as e:
        raise ValueError(f"[{e}]")


def MA(gender, weight, height, age):
    try:
        if(not GenderTest(gender)):
            return("Allowed genders: ['male', 'female']\nPlease re-enter the correct syntax")
        bmr_val = BMR(gender, weight, height, age)
        average_bmr_male = {
            (18, 30): 1900,
            (31, 50): 1800,
            (51, 70): 1700,
            (71, 150): 1600
        }
        average_bmr_female = {
            (18, 30): 1500,
            (31, 50): 1400,
            (51, 70): 1300,
            (71, 150): 1200
        }
        bmr_table = average_bmr_male if gender.lower() == "male" else average_bmr_female
        avg_bmr = None
        for age_limit, target_bmr in bmr_table.items():
            if(age_limit[0] <= age <= age_limit[1]):
                avg_bmr = target_bmr
                break
        if avg_bmr is None:
            return(f"Age '{age}' is not supported !") 
        adjustment_factor = (bmr_val - avg_bmr) / 100  
        ma = int(round(age - adjustment_factor))  
        return ma
    except Exception as e:
        raise ValueError(f"[{e}]")


def VFR(waist_circ, hip_circ):
    try:
        vfr = round(waist_circ / hip_circ, 2)
        return vfr
    except Exception as e:
        raise ValueError(f"[{e}]")


def BSA(height, weight):
    try: 
        height = height * 100
        bsa = round(math.sqrt((height * weight) / 3600), 2)
        return bsa 
    except Exception as e:
        raise ValueError(f"[{e}]")


def VO2MAX(max_heart_rate, resting_heart_rate):
    try:
        vo2max_val = 15 * (max_heart_rate / resting_heart_rate)
        return vo2max_val            
    except Exception as e:
        raise ValueError(f"[{e}]")


def HSI(gender, weight, height, age, cholesterol, blood_pressure):
    try:
        if(not GenderTest(gender)):
            return("Allowed genders: ['male', 'female']\nPlease re-enter the correct syntax")
        bmi = BMI(weight, height)
        bfp = BFP(gender, weight, height, age)
        hsi = round((bmi * 0.4 + bfp * 0.3 + blood_pressure * 0.2 + cholesterol * 0.1) / 4, 2)
        return hsi 
    except Exception as e:
        raise ValueError(f"[{e}]")     


def MMI(gender, weight, height):
    try:
        ffmi = FFMI(gender, weight, height)
        mmi = round(ffmi / weight, 2)
        return mmi 
    except Exception as e:
        raise ValueError(f"[{e}]")


def BFM(gender, weight, height, age):
    try:
        if(not GenderTest(gender)):
            return("Allowed genders: ['male', 'female']\nPlease re-enter the correct syntax")
        bfp = BFP(gender, weight, height, age)
        bfm = round(weight * (bfp / 100), 2)
        return bfm 
    except Exception as e:
        raise ValueError(f"[{e}]")                   
     
def ABSI(waist_circ: float, weight: float, height: float):
    try:
        if waist_circ <= 0 or weight <= 0 or height <= 0:
            return "Invalid input"
        bmi = weight / (height ** 2)
        absi = round(waist_circ / ((bmi ** (2/3)) * (height ** (1/2))), 4)
        return absi
    except Exception as e:
        raise ValueError(f"[{e}]")


def AVI(waist_circ: float, hip_circ: float):
    try:
        if waist_circ <= 0 or hip_circ <= 0:
            return "Invalid input"
        avi = round((2 * (waist_circ ** 2) + 0.7 * ((waist_circ - hip_circ) ** 2)) / 1000, 2)
        return avi
    except Exception as e:
        raise ValueError(f"[{e}]")


def BAI(hip_circ: float, height: float):
    try:
        if hip_circ <= 0 or height <= 0:
            return "Invalid input"
        bai = round((hip_circ / (height ** 1.5)) - 18, 2)
        return bai
    except Exception as e:
        raise ValueError(f"[{e}]")


def CI(weight: float, height: float, waist_circ: float):
    try:
        if weight <= 0 or height <= 0 or waist_circ <= 0:
            return "Invalid input"
        ci = round(waist_circ / (0.109 * math.sqrt(weight / height)), 4)
        return ci
    except Exception as e:
        raise ValueError(f"[{e}]")


def WHtR(waist_circ: float, height: float):
    try:
        if waist_circ <= 0 or height <= 0:
            return "Invalid input"
        return round(waist_circ / height, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def PonderalIndex(weight: float, height: float):
    try:
        if weight <= 0 or height <= 0:
            return "Invalid input"
        return round(weight / (height ** 3), 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def FMI(gender: str, weight: float, height: float, age: int):
    try:
        if not GenderTest(gender):
            return "Allowed genders: ['male', 'female']\nPlease re-enter the correct syntax"
        bfm = BFM(gender, weight, height, age)
        if isinstance(bfm, str): return bfm
        return round(bfm / (height ** 2), 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def FFM(gender: str, weight: float, height: float):
    try:
        return LBM(gender, weight, height)
    except Exception as e:
        raise ValueError(f"[{e}]")


def FMR(gender: str, weight: float, height: float, age: int):
    try:
        if not GenderTest(gender):
            return "Allowed genders: ['male', 'female']\nPlease re-enter the correct syntax"
        bfm = BFM(gender, weight, height, age)
        ffm = LBM(gender, weight, height)
        if ffm <= 0: return "Invalid input"
        return round(bfm / ffm, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def TBW(gender: str, weight: float, height: float, age: int):
    try:
        if not GenderTest(gender):
            return "Allowed genders: ['male', 'female']\nPlease re-enter the correct syntax"
        height_cm = height * 100
        if gender.lower() == "male":
            tbw = 2.447 - (0.09156 * age) + (0.1074 * height_cm) + (0.3362 * weight)
        else:
            tbw = -2.097 + (0.1069 * height_cm) + (0.2466 * weight)
        return round(tbw, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def ECW(gender: str, weight: float, height: float, age: int):
    try:
        tbw = TBW(gender, weight, height, age)
        if isinstance(tbw, str): return tbw
        return round(tbw * 0.3333, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def ICW(gender: str, weight: float, height: float, age: int):
    try:
        tbw = TBW(gender, weight, height, age)
        if isinstance(tbw, str): return tbw
        return round(tbw * 0.6667, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def BCM(gender: str, weight: float, height: float, age: int):
    try:
        icw = ICW(gender, weight, height, age)
        if isinstance(icw, str): return icw
        return round(icw / 0.70, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def SMI(gender: str, weight: float, height: float):
    try:
        ffm = LBM(gender, weight, height)
        smm = ffm * 0.57
        return round(smm / (height ** 2), 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def ASMI(gender: str, weight: float, height: float):
    try:
        ffm = LBM(gender, weight, height)
        asm = ffm * 0.42
        return round(asm / (height ** 2), 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def MAMC(muac: float, tsf: float):
    try:
        if muac <= 0 or tsf <= 0:
            return "Invalid input"
        mamc = round(muac - (math.pi * (tsf / 10)), 2)
        return mamc
    except Exception as e:
        raise ValueError(f"[{e}]")


def MUAC_Assessment(gender: str, muac: float):
    try:
        if not GenderTest(gender):
            return "Allowed genders: ['male', 'female']\nPlease re-enter the correct syntax"
        if muac <= 0: return "Invalid input"
        if gender.lower() == "male":
            return "Normal" if muac >= 23 else "Arm muscle area malnutrition"
        else:
            return "Normal" if muac >= 22 else "Arm muscle area malnutrition"
    except Exception as e:
        raise ValueError(f"[{e}]")


def BEE(gender: str, weight: float, height: float, age: int):
    try:
        return BMR(gender, weight, height, age)
    except Exception as e:
        raise ValueError(f"[{e}]")


def REE(gender: str, weight: float, height: float, age: int):
    try:
        if not GenderTest(gender):
            return "Allowed genders: ['male', 'female']\nPlease re-enter the correct syntax"
        height_cm = height * 100
        if gender.lower() == "male":
            ree = (10 * weight) + (6.25 * height_cm) - (5 * age) + 5
        else:
            ree = (10 * weight) + (6.25 * height_cm) - (5 * age) - 161
        return round(ree, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def PAL(gender: str, weight: float, height: float, age: int, activity_index_R: int):
    try:
        tdee = TDEE(gender, weight, height, age, activity_index_R)
        bmr = BMR(gender, weight, height, age)
        if bmr <= 0: return "Invalid input"
        return round(tdee / bmr, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def MET(vo2_rate: float):
    try:
        if vo2_rate <= 0: return "Invalid input"
        return round(vo2_rate / 3.5, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def MaxHeartRate(age: int):
    try:
        if age <= 0: return "Invalid input"
        return round(207 - (0.7 * age))
    except Exception as e:
        raise ValueError(f"[{e}]")


def HeartRateReserve(resting_heart_rate: int, age: int):
    try:
        max_hr = MaxHeartRate(age)
        if resting_heart_rate <= 0 or resting_heart_rate >= max_hr: return "Invalid input"
        return max_hr - resting_heart_rate
    except Exception as e:
        raise ValueError(f"[{e}]")


def TargetHeartRate(resting_heart_rate: int, age: int, intensity: float):
    try:
        hrr = HeartRateReserve(resting_heart_rate, age)
        if isinstance(hrr, str): return hrr
        thr = (hrr * intensity) + resting_heart_rate
        return round(thr)
    except Exception as e:
        raise ValueError(f"[{e}]")


def CalorieDeficit(tdee: float, deficit_amount: float = 500.0):
    try:
        if tdee <= deficit_amount: return "TDEE is too low to apply this deficit"
        return round(tdee - deficit_amount, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def CalorieSurplus(tdee: float, surplus_amount: float = 300.0):
    try:
        if tdee <= 0: return "Invalid input"
        return round(tdee + surplus_amount, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def ProteinNeed(weight: float, activity_level: str = "medium"):
    try:
        factors = {"light": 1.2, "medium": 1.6, "high": 2.0}
        factor = factors.get(activity_level.lower(), 1.6)
        return round(weight * factor, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def FatNeed(tdee: float, calorie_percentage: float = 0.25):
    try:
        if tdee <= 0: return "Invalid input"
        return round((tdee * calorie_percentage) / 9, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def CarbNeed(tdee: float, p_protein_g: float, p_fat_g: float):
    try:
        remaining_calories = tdee - (p_protein_g * 4) - (p_fat_g * 9)
        if remaining_calories <= 0: return "Calories from Protein and Fat have exceeded TDEE"
        return round(remaining_calories / 4, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def WaterNeed(weight: float, workout_minutes: float = 0.0):
    try:
        baseline_water = weight * 0.033
        exercise_water = (workout_minutes / 30) * 0.35
        return round(baseline_water + exercise_water, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def IdealWater(weight: float):
    try:
        return BBW(weight)
    except Exception as e:
        raise ValueError(f"[{e}]")


def LeanBodyPercentage(gender: str, weight: float, height: float):
    try:
        lbm = LBM(gender, weight, height)
        if weight <= 0: return "Invalid input"
        return round((lbm / weight) * 100, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def FatPercentage(gender: str, weight: float, height: float, age: int):
    try:
        return BFP(gender, weight, height, age)
    except Exception as e:
        raise ValueError(f"[{e}]")


def MusclePercentage(gender: str, weight: float, height: float):
    try:
        smi = SMI(gender, weight, height)
        smm = smi * (height ** 2)
        return round((smm / weight) * 100, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def BoneMassEstimate(gender: str, weight: float, height: float):
    try:
        ffm = LBM(gender, weight, height)
        gender_factor = 0.05 if gender.lower() == "male" else 0.04
        return round(ffm * gender_factor, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def BMIPrime(weight: float, height: float):
    try:
        bmi = BMI(weight, height)
        if isinstance(bmi, str): return bmi
        return round(bmi / 25, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def CorpulenceIndex(weight: float, height: float):
    try:
        return PonderalIndex(weight, height)
    except Exception as e:
        raise ValueError(f"[{e}]")


def RelativeFatMass_Ext(gender: str, waist_circ: float, height: float):
    try:
        if not GenderTest(gender):
            return "Allowed genders: ['male', 'female']\nPlease re-enter the correct syntax"
        height_cm = height * 100
        gender_factor = 64 if gender.lower() == "male" else 76
        rfm = round(gender_factor - (20 * (waist_circ / height_cm)), 2)
        return rfm
    except Exception as e:
        raise ValueError(f"[{e}]")


def BodyRoundnessIndex(waist_circ: float, height: float):
    try:
        if waist_circ <= 0 or height <= 0:
            return "Invalid input"
        waist_circ_m = waist_circ / 100 if waist_circ > 5 else waist_circ
        height_m = height if height < 3 else height / 100
        bri = round(364.2 - 365.5 * math.sqrt(1 - ((waist_circ_m / (2 * math.pi)) ** 2) / ((0.5 * height_m) ** 2)), 2)
        return bri
    except Exception as e:
        raise ValueError(f"[{e}]")


def ABodyRoundness(waist_circ: float, height: float):
    try:
        return BodyRoundnessIndex(waist_circ, height)
    except Exception as e:
        raise ValueError(f"[{e}]")


def VisceralAdiposityIndex(gender: str, weight: float, height: float, waist_circ: float, tg: float, hdl: float):
    try:
        if not GenderTest(gender):
            return "Allowed genders: ['male', 'female']\nPlease re-enter the correct syntax"
        bmi = BMI(weight, height)
        waist_circ_cm = waist_circ if waist_circ > 5 else waist_circ * 100
        if gender.lower() == "male":
            vai = (waist_circ_cm / (39.68 + (1.88 * bmi))) * (tg / 1.03) * (1.31 / hdl)
        else:
            vai = (waist_circ_cm / (36.58 + (1.89 * bmi))) * (tg / 0.81) * (1.52 / hdl)
        return round(vai, 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def LipidAccumulationProduct(gender: str, waist_circ: float, tg: float):
    try:
        if not GenderTest(gender):
            return "Allowed genders: ['male', 'female']\nPlease re-enter the correct syntax"
        waist_circ_cm = waist_circ if waist_circ > 5 else waist_circ * 100
        if gender.lower() == "male":
            lap = (waist_circ_cm - 65) * tg
        else:
            lap = (waist_circ_cm - 58) * tg
        return round(max(0.0, lap), 2)
    except Exception as e:
        raise ValueError(f"[{e}]")


def FatMass(gender: str, weight: float, height: float, age: int):
    try:
        return BFM(gender, weight, height, age)
    except Exception as e:
        raise ValueError(f"[{e}]")


def LeanMass(gender: str, weight: float, height: float):
    try:
        return LBM(gender, weight, height)
    except Exception as e:
        raise ValueError(f"[{e}]")

def GenderTest(gender):
    allowed_genders = ["male", "female"]
    if isinstance(gender, (int, float, complex)):  
        return False
    if gender.lower() not in allowed_genders:
        return False
    else: 
        return True      


def NABMI(bmi: float):
    if bmi < 18.5:
        return "Incorporate more protein and carbohydrates into your diet"
    elif bmi < 25:
        return "Maintain a balanced diet and regular exercise routine"
    elif bmi < 30:
        return "Reduce carbohydrates and fats, increase workout intensity"
    else:
        return "Immediate weight loss is highly recommended"


def NABMR(gender: str, bmr: float):
    return f"Ensure your total calorie consumption aligns with your BMR: {bmr} kcal/day"


def NATDEE(gender: str, tdee: float):
    return f"Consume calories according to your TDEE: {tdee} kcal/day to maintain weight"


def NAWHR(whr: float):
    if whr < 0.9:
        return "Normal waist-to-hip ratio"
    else:
        return "Pay attention to reducing visceral fat in the abdominal region"


def NALBM(lbm: float):
    return f"Maintain your current lean muscle mass: {lbm} kg"


def NAFFMI(ffmi: float):
    return f"Standard fat-free mass reference: {ffmi}"


def NARFM(rfm: float):
    return f"Monitor your body fat level: {rfm}%"


def NABFP(bfp: float):
    return f"Body fat percentage: {bfp}%, consider adjusting your nutrition and workouts"


def NABBW(bbw: float):
    return f"Baseline weight configuration: {bbw} kg"


def NAIBW(ibw: float):
    return f"Ideal healthy body weight target: {ibw} kg"


def NAMA(ma: float):
    return f"Calculated metabolic age reference: {ma}"


def NAVFR(vfr: float):
    return f"Visceral fat rating benchmark: {vfr}"


def NABSA(bsa: float):
    return f"Total body surface area metric: {bsa} m²"


def NAVO2MAX(vo2max: float):
    return f"Cardiorespiratory fitness capacity: {vo2max} ml/kg/min"


def NAHSI(hsi: float):
    return f"Hepatic steatosis metric index: {hsi}"


def NAMMI(mmi: float):
    return f"Calculated muscle mass evaluation index: {mmi}"


def NABFM(bfm: float):
    return f"Absolute body fat mass volume: {bfm} kg"

def NAABSI(absi: float):
    return f"A Body Shape Index (ABSI): {absi}. Assesses risks related to abdominal fat distribution."


def NAAVI(avi: float):
    return f"Abdominal Volume Index (AVI): {avi}. Monitor to prevent metabolic syndromes."


def NABAI(bai: float):
    return f"Body Adiposity Index (BAI) via hip metric: {bai}%. Track overall weight controls."


def NACI(ci: float):
    return f"Conicity Index (CI): {ci}. Reflects central fat accumulation trends."


def NAWHtR(whtr: float):
    if whtr <= 0.5:
        return f"Waist-to-height ratio ({whtr}) is Healthy. Maintain current parameters."
    return f"Waist-to-height ratio ({whtr}) is Elevated. Target abdominal fat reduction to minimize cardiovascular risk."


def NAPonderalIndex(pi: float):
    return f"Corpulence density measure (Ponderal Index): {pi} kg/m³."


def NAFMI(fmi: float):
    return f"Fat Mass Index (FMI): {fmi} kg/m²."


def NAFFM(ffm: float):
    return f"Fat-Free Mass (FFM): {ffm} kg. Optimize protein intake to develop muscle tissue structure."


def NAFMR(fmr: float):
    return f"Fat Mass to Fat-Free Mass Ratio (FMR): {fmr}."


def NATBW(tbw: float):
    return f"Total Body Water (TBW) compilation: {tbw} liters."


def NAECW(ecw: float):
    return f"Extracellular Water (ECW) capacity: {ecw} liters."


def NAICW(icw: float):
    return f"Intracellular Water (ICW) capacity: {icw} liters."


def NABCM(bcm: float):
    return f"Body Cell Mass (BCM) active functional volume: {bcm} kg."


def NASMI(smi: float):
    return f"Skeletal Muscle Index (SMI): {smi} kg/m²."


def NAASMI(asmi: float):
    return f"Appendicular Skeletal Muscle Index (ASMI): {asmi} kg/m²."


def NAMAMC(mamc: float):
    return f"Mid-Upper Arm Muscle Circumference (MAMC): {mamc} cm."


def NAMUAC(assessment: str):
    return f"Mid-Upper Arm Circumference (MUAC) screening outcome: {assessment}."


def NABEE(bee: float):
    return f"Basal Energy Expenditure (BEE) target threshold: {bee} kcal/day."


def NAREE(ree: float):
    return f"Resting Energy Expenditure (REE) benchmark index: {ree} kcal/day."


def NAPAL(pal: float):
    return f"Physical Activity Level (PAL) coefficient reference: {pal}."


def NAMET(met: float):
    return f"Metabolic Equivalent of Task (MET) intensity: {met}."


def NAHeartRateReserve(hrr: int):
    return f"Your safe calculated heart rate reserve parameters: {hrr} bpm."


def NAMaxHeartRate(mhr: int):
    return f"Maximum safe recommended heart rate limit: {mhr} bpm."


def NATargetHeartRate(thr: int):
    return f"Target structural heart rate working zone: {thr} bpm."


def NACalorieDeficit(cal: float):
    return f"Target caloric target intake value to achieve weight loss goals: {cal} kcal/day."


def NACalorieSurplus(cal: float):
    return f"Target caloric target intake value to achieve weight gain goals: {cal} kcal/day."


def NAProteinNeed(prot: float):
    return f"Minimum daily targeted structural Protein requirement intake: {prot} g/day."


def NAFatNeed(fat: float):
    return f"Essential daily quality lipid structural (Fat) requirements: {fat} g/day."


def NACarbNeed(carb: float):
    return f"Daily structural carbohydrate loading requirements: {carb} g/day."


def NAWaterNeed(water: float):
    return f"Target water consumption quota adjusted for training loads: {water} liters/day."


def NAIdealWater(water: float):
    return f"Theoretical structural framework baseline water limits: {water} liters/day."


def NALeanBodyPercentage(lbp: float):
    return f"Total lean muscle tissue mass percentage: {lbp}%."


def NAFatPercentage(fp: float):
    return f"Total structural framework adiposity tracking values: {fp}%."


def NAMusclePercentage(mp: float):
    return f"Skeletal muscle structural tracking density tissue values: {mp}%."


def NABoneMassEstimate(bm: float):
    return f"Estimated structural framework bone mineral content profile metrics: {bm} kg."


def NABMIPrime(bp: float):
    return f"BMI Prime baseline metrics index tracker value: {bp} (Proximity to 1.0 indicates optimal tracking values)."


def NACorpulenceIndex(ci: float):
    return f"Expanded structural framework index rating corpulence metric values: {ci}."


def NARelativeFatMass(rfm: float):
    return f"Relative Fat Mass (RFM) calculated index values: {rfm}%."


def NABodyRoundnessIndex(bri: float):
    return f"Body Roundness Index (BRI) evaluation framework profile: {bri}."


def NAABodyRoundness(bri: float):
    return f"Streamlined Body Roundness Index evaluation system value metrics: {bri}."


def NAVisceralAdiposityIndex(vai: float):
    return f"Visceral Adiposity Index (VAI): {vai}. Higher indices suggest potential cardiovascular risk trends."


def NALipidAccumulationProduct(lap: float):
    return f"Lipid Accumulation Product (LAP) monitoring indexes profile: {lap}."


def NAFatMass(fm: float):
    return f"Total structural framework absolute weight fat capacities: {fm} kg."


def NALeanMass(lm: float):
    return f"Total structural framework absolute weight lean mass profile values: {lm} kg."


def INSTRUCT(function_name="all", write_file=False):
    guidelines = {
        "BMI": """1. BMI
Syntax: BMI(weight, height)
Example: BMI(60, 1.75)
Advice: NABMI(BMI)
""",

        "BMR": """2. BMR
Syntax: BMR(gender, weight, height, age)
Example: BMR('male', 70, 1.75, 25)
Advice: NABMR(gender, BMR)
""",

        "TDEE": """3. TDEE
Syntax: TDEE(gender, weight, height, age, activity_index)
Example: TDEE('male', 70, 1.75, 25, 3)
Advice: NATDEE(gender, TDEE)
""",

        "WHR": """4. WHR
Syntax: WHR(gender, waist_circ, hip_circ)
Example: WHR('female', 70, 90)
Advice: NAWHR(WHR)
""",

        "LBM": """5. LBM
Syntax: LBM(gender, weight, height)
Example: LBM('male', 70, 1.75)
Advice: NALBM(LBM)
""",

        "FFMI": """6. FFMI
Syntax: FFMI(gender, weight, height)
Example: FFMI('male', 70, 1.75)
Advice: NAFFMI(FFMI)
""",

        "RFM": """7. RFM
Syntax: RFM(waist_circ, height)
Example: RFM(70, 1.75)
Advice: NARFM(RFM)
""",

        "BFP": """8. BFP
Syntax: BFP(gender, weight, height, age)
Example: BFP('male', 70, 1.75, 25)
Advice: NABFP(BFP)
""",

        "BBW": """9. BBW
Syntax: BBW(weight)
Example: BBW(70)
Advice: NABBW(BBW)
""",

        "IBW": """10. IBW
Syntax: IBW(gender, height)
Example: IBW('male', 1.75)
Advice: NAIBW(IBW)
""",

        "MA": """11. MA
Syntax: MA(gender, weight, height, age)
Example: MA('male', 70, 1.75, 25)
Advice: NAMA(MA)
""",

        "VFR": """12. VFR
Syntax: VFR(waist_circ, hip_circ)
Example: VFR(70, 90)
Advice: NAVFR(VFR)
""",

        "BSA": """13. BSA
Syntax: BSA(height, weight)
Example: BSA(1.75, 70)
Advice: NABSA(BSA)
""",

        "VO2MAX": """14. VO2MAX
Syntax: VO2MAX(max_heart_rate, resting_heart_rate)
Example: VO2MAX(200, 70)
Advice: NAVO2MAX(VO2MAX)
""",

        "HSI": """15. HSI
Syntax: HSI(gender, weight, height, age, cholesterol, blood_pressure)
Example: HSI('male', 70, 1.75, 25, 200, 120)
Advice: NAHSI(HSI)
""",

        "MMI": """16. MMI
Syntax: MMI(gender, weight, height)
Example: MMI('male', 70, 1.75)
Advice: NAMMI(MMI)
""",

        "BFM": """17. BFM
Syntax: BFM(gender, weight, height, age)
Example: BFM('male', 70, 1.75, 25)
Advice: NABFM(BFM)
""",

        "ABSI": """18. ABSI
Syntax: ABSI(waist_circ, weight, height)
Example: ABSI(80, 70, 1.75)
Advice: NAABSI(ABSI)
""",

        "AVI": """19. AVI
Syntax: AVI(waist_circ, hip_circ)
Example: AVI(80, 95)
Advice: NAAVI(AVI)
""",

        "BAI": """20. BAI
Syntax: BAI(hip_circ, height)
Example: BAI(95, 1.75)
Advice: NABAI(BAI)
""",

        "CI": """21. CI
Syntax: CI(weight, height, waist_circ)
Example: CI(70, 1.75, 80)
Advice: NACI(CI)
""",

        "WHTR": """22. WHtR
Syntax: WHtR(waist_circ, height)
Example: WHtR(80, 1.75)
Advice: NAWHtR(WHtR)
""",

        "PONDERALINDEX": """23. PonderalIndex / CorpulenceIndex
Syntax: PonderalIndex(weight, height)
Example: PonderalIndex(70, 1.75)
Advice: NAPonderalIndex(PonderalIndex)
""",

        "FMI": """24. FMI
Syntax: FMI(gender, weight, height, age)
Example: FMI('male', 70, 1.75, 25)
Advice: NAFMI(FMI)
""",

        "FFM": """25. FFM
Syntax: FFM(gender, weight, height)
Example: FFM('male', 70, 1.75)
Advice: NAFFM(FFM)
""",

        "FMR": """26. FMR
Syntax: FMR(gender, weight, height, age)
Example: FMR('male', 70, 1.75, 25)
Advice: NAFMR(FMR)
""",

        "TBW": """27. TBW
Syntax: TBW(gender, weight, height, age)
Example: TBW('male', 70, 1.75, 25)
Advice: NATBW(TBW)
""",

        "ECW": """28. ECW
Syntax: ECW(gender, weight, height, age)
Example: ECW('male', 70, 1.75, 25)
Advice: NAECW(ECW)
""",

        "ICW": """29. ICW
Syntax: ICW(gender, weight, height, age)
Example: ICW('male', 70, 1.75, 25)
Advice: NAICW(ICW)
""",

        "BCM": """30. BCM
Syntax: BCM(gender, weight, height, age)
Example: BCM('male', 70, 1.75, 25)
Advice: NABCM(BCM)
""",

        "SMI": """31. SMI
Syntax: SMI(gender, weight, height)
Example: SMI('male', 70, 1.75)
Advice: NASMI(SMI)
""",

        "ASMI": """32. ASMI
Syntax: ASMI(gender, weight, height)
Example: ASMI('male', 70, 1.75)
Advice: NAASMI(ASMI)
""",

        "MAMC": """33. MAMC
Syntax: MAMC(muac, TSF)
Example: MAMC(28, 12)
Advice: NAMAMC(MAMC)
""",

        "MUAC_ASSESSMENT": """34. MUAC_Assessment
Syntax: MUAC_Assessment(gender, muac)
Example: MUAC_Assessment('male', 25)
Advice: NAMUAC(MUAC_Assessment)
""",

        "BEE": """35. BEE
Syntax: BEE(gender, weight, height, age)
Example: BEE('male', 70, 1.75, 25)
Advice: NABEE(BEE)
""",

        "REE": """36. REE
Syntax: REE(gender, weight, height, age)
Example: REE('male', 70, 1.75, 25)
Advice: NAREE(REE)
""",

        "PAL": """37. PAL
Syntax: PAL(gender, weight, height, age, activity_index_R)
Example: PAL('male', 70, 1.75, 25, 3)
Advice: NAPAL(PAL)
""",

        "MET": """38. MET
Syntax: MET(vo2_rate)
Example: MET(42.5)
Advice: NAMET(MET)
""",

        "MAXHEARTRATE": """39. MaxHeartRate
Syntax: MaxHeartRate(age)
Example: MaxHeartRate(25)
Advice: NAMaxHeartRate(MaxHeartRate)
""",

        "HEARTRATERESERVE": """40. HeartRateReserve
Syntax: HeartRateReserve(resting_heart_rate, age)
Example: HeartRateReserve(65, 25)
Advice: NAHeartRateReserve(HeartRateReserve)
""",

        "TARGETHEARTRATE": """41. TargetHeartRate
Syntax: TargetHeartRate(resting_heart_rate, age, intensity)
Example: TargetHeartRate(65, 25, 0.7)
Advice: NATargetHeartRate(TargetHeartRate)
""",

        "CALORIEDEFICIT": """42. CalorieDeficit
Syntax: CalorieDeficit(tdee, deficit_amount)
Example: CalorieDeficit(2500, 500)
Advice: NACalorieDeficit(CalorieDeficit)
""",

        "CALORIESURPLUS": """43. CalorieSurplus
Syntax: CalorieSurplus(tdee, surplus_amount)
Example: CalorieSurplus(2500, 300)
Advice: NACalorieSurplus(CalorieSurplus)
""",

        "PROTEINNEED": """44. ProteinNeed
Syntax: ProteinNeed(weight, activity_level)
Example: ProteinNeed(70, 'medium')
Advice: NAProteinNeed(ProteinNeed)
""",

        "FATNEED": """45. FatNeed
Syntax: FatNeed(tdee, calorie_percentage)
Example: FatNeed(2500, 0.25)
Advice: NAFatNeed(FatNeed)
""",

        "CARBNEED": """46. CarbNeed
Syntax: CarbNeed(tdee, p_protein_g, p_fat_g)
Example: CarbNeed(2500, 140, 70)
Advice: NACarbNeed(CarbNeed)
""",

        "WATERNEED": """47. WaterNeed
Syntax: WaterNeed(weight, workout_minutes)
Example: WaterNeed(70, 45)
Advice: NAWaterNeed(WaterNeed)
""",

        "IDEALWATER": """48. IdealWater
Syntax: IdealWater(weight)
Example: IdealWater(70)
Advice: NAIdealWater(IdealWater)
""",

        "LEANBODYPERCENTAGE": """49. LeanBodyPercentage
Syntax: LeanBodyPercentage(gender, weight, height)
Example: LeanBodyPercentage('male', 70, 1.75)
Advice: NALeanBodyPercentage(LeanBodyPercentage)
""",

        "FATPERCENTAGE": """50. FatPercentage
Syntax: FatPercentage(gender, weight, height, age)
Example: FatPercentage('male', 70, 1.75, 25)
Advice: NAFatPercentage(FatPercentage)
""",

        "MUSCLEPERCENTAGE": """51. MusclePercentage
Syntax: MusclePercentage(gender, weight, height)
Example: MusclePercentage('male', 70, 1.75)
Advice: NAMusclePercentage(MusclePercentage)
""",

        "BONEMASSESTIMATE": """52. BoneMassEstimate
Syntax: BoneMassEstimate(gender, weight, height)
Example: BoneMassEstimate('male', 70, 1.75)
Advice: NABoneMassEstimate(BoneMassEstimate)
""",

        "BMIPRIME": """53. BMIPrime
Syntax: BMIPrime(weight, height)
Example: BMIPrime(70, 1.75)
Advice: NABMIPrime(BMIPrime)
""",

        "BODYROUNDNESSINDEX": """54. BodyRoundnessIndex / ABodyRoundness
Syntax: BodyRoundnessIndex(waist_circ, height)
Example: BodyRoundnessIndex(80, 1.75)
Advice: NABodyRoundnessIndex(BodyRoundnessIndex)
""",

        "VISCERALADIPOSITYINDEX": """55. VisceralAdiposityIndex
Syntax: VisceralAdiposityIndex(gender, weight, height, waist_circ, tg, hdl)
Example: VisceralAdiposityIndex('male', 70, 1.75, 80, 1.1, 1.2)
Advice: NAVisceralAdiposityIndex(VisceralAdiposityIndex)
""",

        "LIPIDACCUMULATIONPRODUCT": """56. LipidAccumulationProduct
Syntax: LipidAccumulationProduct(gender, waist_circ, tg)
Example: LipidAccumulationProduct('male', 80, 1.1)
Advice: NALipidAccumulationProduct(LipidAccumulationProduct)
"""
    }

    alias_mapping = {
        "CORPULENCEINDEX": "PONDERALINDEX",
        "CORPULENCE_INDEX": "PONDERALINDEX",
        "FATMASS": "BFM",
        "LEANMASS": "LBM",
        "ABODYROUNDNESS": "BODYROUNDNESSINDEX",
        "RELATIVEFATMASS_EXT": "RFM"
    }

    key = function_name.upper()
    if key in alias_mapping:
        key = alias_mapping[key]

    if key == "ALL":
        content = "C_HEALTHY USER DOCUMENTATION GUIDE\n\n" + "\n".join(guidelines.values())
    else:
        if key not in guidelines:
            return f"No documentation records matching function query target: '{function_name}'"
        content = guidelines[key]

    if write_file:
        file_name = "user_documentation_guide.txt"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Documentation resource written successfully to output path destination: {os.path.abspath(file_name)}"
    return content

# ---------------------------------------------------- 
# Copyright by NTC++ 06/07/2026
# ----------------------------------------------------
