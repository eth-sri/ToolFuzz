#!/bin/bash

root_dir=$1

mkdir -p ${root_dir}/01_Field_Data/01_Soil_Samples
mkdir -p ${root_dir}/01_Field_Data/02_Weather_Data
mkdir -p ${root_dir}/01_Field_Data/03_Crop_Yields
mkdir -p ${root_dir}/02_Precision_Farming_Tools/01_Drones
mkdir -p ${root_dir}/02_Precision_Farming_Tools/02_Sensors
mkdir -p ${root_dir}/02_Precision_Farming_Tools/03_Satellite_Images
mkdir -p ${root_dir}/03_Analysis_Reports/01_Soil_Analysis
mkdir -p ${root_dir}/03_Analysis_Reports/02_Weather_Analysis
mkdir -p ${root_dir}/03_Analysis_Reports/03_Crop_Yield_Analysis
mkdir -p ${root_dir}/04_Farming_Strategies/01_Irrigation
mkdir -p ${root_dir}/04_Farming_Strategies/02_Fertilization
mkdir -p ${root_dir}/04_Farming_Strategies/03_Pest_Control
mkdir -p ${root_dir}/05_Archives/01_Old_Data
mkdir -p ${root_dir}/05_Archives/02_Old_Reports
mkdir -p ${root_dir}/06_Templates/01_Report_Templates
mkdir -p ${root_dir}/06_Templates/02_Strategy_Templates

touch ${root_dir}/01_Field_Data/01_Soil_Samples/soil_sample_001.csv
touch ${root_dir}/01_Field_Data/01_Soil_Samples/soil_sample_002.csv
touch ${root_dir}/01_Field_Data/02_Weather_Data/weather_data_2023.csv
touch ${root_dir}/01_Field_Data/02_Weather_Data/weather_data_2024.csv
touch ${root_dir}/01_Field_Data/03_Crop_Yields/crop_yield_2023.csv
touch ${root_dir}/01_Field_Data/03_Crop_Yields/crop_yield_2024.csv
touch ${root_dir}/02_Precision_Farming_Tools/01_Drones/drone_flight_data_001.csv
touch ${root_dir}/02_Precision_Farming_Tools/01_Drones/drone_flight_data_002.csv
touch ${root_dir}/02_Precision_Farming_Tools/02_Sensors/sensor_data_001.csv
touch ${root_dir}/02_Precision_Farming_Tools/02_Sensors/sensor_data_002.csv
touch ${root_dir}/02_Precision_Farming_Tools/03_Satellite_Images/satellite_image_001.jpg
touch ${root_dir}/02_Precision_Farming_Tools/03_Satellite_Images/satellite_image_002.jpg
touch ${root_dir}/03_Analysis_Reports/01_Soil_Analysis/soil_analysis_2023.pdf
touch ${root_dir}/03_Analysis_Reports/02_Weather_Analysis/weather_analysis_2023.pdf
touch ${root_dir}/03_Analysis_Reports/03_Crop_Yield_Analysis/crop_yield_analysis_2023.pdf
touch ${root_dir}/04_Farming_Strategies/01_Irrigation/irrigation_plan_2023.pdf
touch ${root_dir}/04_Farming_Strategies/01_Irrigation/irrigation_plan_2024.pdf
touch ${root_dir}/04_Farming_Strategies/02_Fertilization/fertilization_plan_2023.pdf
touch ${root_dir}/04_Farming_Strategies/02_Fertilization/fertilization_plan_2024.pdf
touch ${root_dir}/04_Farming_Strategies/03_Pest_Control/pest_control_plan_2023.pdf
touch ${root_dir}/04_Farming_Strategies/03_Pest_Control/pest_control_plan_2024.pdf
touch ${root_dir}/05_Archives/01_Old_Data/old_soil_samples.zip
touch ${root_dir}/05_Archives/01_Old_Data/old_weather_data.zip
touch ${root_dir}/05_Archives/01_Old_Data/old_crop_yields.zip
touch ${root_dir}/05_Archives/02_Old_Reports/old_soil_analysis.zip
touch ${root_dir}/05_Archives/02_Old_Reports/old_weather_analysis.zip
touch ${root_dir}/05_Archives/02_Old_Reports/old_crop_yield_analysis.zip
touch ${root_dir}/06_Templates/01_Report_Templates/soil_analysis_template.docx
touch ${root_dir}/06_Templates/01_Report_Templates/weather_analysis_template.docx
touch ${root_dir}/06_Templates/01_Report_Templates/crop_yield_analysis_template.docx
touch ${root_dir}/06_Templates/02_Strategy_Templates/irrigation_plan_template.docx
touch ${root_dir}/06_Templates/02_Strategy_Templates/fertilization_plan_template.docx
touch ${root_dir}/06_Templates/02_Strategy_Templates/pest_control_plan_template.docx
