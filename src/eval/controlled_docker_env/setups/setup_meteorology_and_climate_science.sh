#!/bin/bash

root_dir=$1

mkdir -p ${root_dir}/archive/climate_reports
mkdir -p ${root_dir}/archive/weather_data
mkdir -p ${root_dir}/archive/research_papers
mkdir -p ${root_dir}/current/climate_reports
mkdir -p ${root_dir}/current/weather_data
mkdir -p ${root_dir}/current/research_papers
mkdir -p ${root_dir}/forecasts/short_term
mkdir -p ${root_dir}/forecasts/long_term
mkdir -p ${root_dir}/models/climate_models/model1
mkdir -p ${root_dir}/models/climate_models/model2
mkdir -p ${root_dir}/models/weather_models/model1
mkdir -p ${root_dir}/models/weather_models/model2
mkdir -p ${root_dir}/resources/books
mkdir -p ${root_dir}/resources/databases
mkdir -p ${root_dir}/resources/websites

touch ${root_dir}/archive/climate_reports/archived_climate_report_2021.pdf
touch ${root_dir}/archive/climate_reports/archived_climate_report_2020.pdf
touch ${root_dir}/archive/weather_data/archived_weather_data_2021.csv
touch ${root_dir}/archive/weather_data/archived_weather_data_2020.csv
touch ${root_dir}/archive/research_papers/old_research_paper1.pdf
touch ${root_dir}/archive/research_papers/old_research_paper2.pdf
touch ${root_dir}/current/climate_reports/climate_report_2022.pdf
touch ${root_dir}/current/climate_reports/climate_report_2023.pdf
touch ${root_dir}/current/weather_data/weather_data_2022.csv
touch ${root_dir}/current/weather_data/weather_data_2023.csv
touch ${root_dir}/current/research_papers/research_paper1.pdf
touch ${root_dir}/current/research_papers/research_paper2.pdf
touch ${root_dir}/forecasts/short_term/forecast_1.pdf
touch ${root_dir}/forecasts/short_term/forecast_2.pdf
touch ${root_dir}/forecasts/long_term/forecast_1.pdf
touch ${root_dir}/forecasts/long_term/forecast_2.pdf
touch ${root_dir}/models/climate_models/model1/model1_code.py
touch ${root_dir}/models/climate_models/model1/model1_data.csv
touch ${root_dir}/models/climate_models/model2/model2_code.py
touch ${root_dir}/models/climate_models/model2/model2_data.csv
touch ${root_dir}/models/weather_models/model1/model1_code.py
touch ${root_dir}/models/weather_models/model1/model1_data.csv
touch ${root_dir}/models/weather_models/model2/model2_code.py
touch ${root_dir}/models/weather_models/model2/model2_data.csv
touch ${root_dir}/resources/books/book1.pdf
touch ${root_dir}/resources/books/book2.pdf
touch ${root_dir}/resources/databases/database1.csv
touch ${root_dir}/resources/databases/database2.csv
touch ${root_dir}/resources/websites/website1.txt
touch ${root_dir}/resources/websites/website2.txt
