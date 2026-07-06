import os
from setuptools import setup, find_packages

long_description = ""
if os.path.exists("README.md"):
    with open("README.md", encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="C_healthy",
    version="0.3.0",
    description="A library for calculating body index and and give advice",
    url="https://github.com/trgchinhh/LibraryChealthy",
    author="Nguyen Truong Chinh",
    author_email="chinhcuber@gmail.com",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "__version__", "INSTRUCT",

        "BMI", "BMR", "TDEE", "WHR", "LBM", "BFP",
        "BBW", "IBW", "MA", "RFM", "VFR", "BSA",
        "FFMI", "HSI", "MMI", "BFM", "ABSI", "AVI",
        "BAI", "CI", "WHtR", "FMI", "FFM", "FMR",
        "TBW", "ECW", "ICW", "BCM", "SMI", "BEE",
        "REE", "PAL", "MET", "VO2MAX", "ASMI", "MAMC",
        "PonderalIndex", "MaxHeartRate", "TargetHeartRate",
        "HeartRateReserve", "CalorieDeficit", "CalorieSurplus",
        "MUAC_Assessment", "ProteinNeed", "FatNeed",
        "CarbNeed", "WaterNeed", "IdealWater",
        "LeanBodyPercentage", "FatPercentage", "MusclePercentage",
        "BoneMassEstimate", "BMIPrime", "CorpulenceIndex",
        "RelativeFatMass_Ext", "BodyRoundnessIndex", "ABodyRoundness",
        "VisceralAdiposityIndex", "LipidAccumulationProduct",
        "FatMass", "LeanMass", "GenderTest",

        
        "NABMI", "NABMR", "NATDEE", "NAWHR", "NALBM", "NABFP",
        "NABBW", "NAIBW", "NAMA", "NAVFR", "NABSA", "NAMMI",
        "NABFM", "NAAVI", "NABAI", "NACI", "NAFFM", "NAFMR",
        "NATBW", "NAECW", "NAICW", "NABCM", "NASMI", "NABEE",
        "NAREE", "NAPAL", "NAMET", "NAFFMI", "NARFM", "NAABSI",
        "NAWHtR", "NAFMI", "NAASMI", "NAMAMC", "NAMUAC",
        "NAMaxHeartRate", "NATargetHeartRate", "NACalorieDeficit",
        "NACalorieSurplus", "NAProteinNeed", "NAFatNeed",
        "NACarbNeed", "NAWaterNeed", "NAIdealWater",
        "NAPonderalIndex", "NAVO2MAX", "NAHeartRateReserve",
        "NALeanBodyPercentage", "NAFatPercentage", "NAMusclePercentage",
        "NABoneMassEstimate", "NABMIPrime", "NACorpulenceIndex",
        "NARelativeFatMass", "NABodyRoundnessIndex", "NAABodyRoundness",
        "NAVisceralAdiposityIndex", "NALipidAccumulationProduct", "NAFatMass",
        "NALeanMass", "NAHSI",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
