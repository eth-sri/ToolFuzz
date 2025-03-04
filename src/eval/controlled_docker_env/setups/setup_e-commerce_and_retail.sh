#!/bin/bash

root_dir=$1

mkdir -p ${root_dir}/archive/products
mkdir -p ${root_dir}/archive/sales
mkdir -p ${root_dir}/archive/templates

mkdir -p ${root_dir}/products/product_A/2023/product_images
mkdir -p ${root_dir}/products/product_A/2023/product_reviews
mkdir -p ${root_dir}/products/product_A/2023/sales/Q1
mkdir -p ${root_dir}/products/product_A/2023/sales/Q2
mkdir -p ${root_dir}/products/product_A/2023/sales/Q3
mkdir -p ${root_dir}/products/product_A/2023/sales/Q4

mkdir -p ${root_dir}/products/product_A/2024/product_images
mkdir -p ${root_dir}/products/product_A/2024/product_reviews
mkdir -p ${root_dir}/products/product_A/2024/sales/Q1
mkdir -p ${root_dir}/products/product_A/2024/sales/Q2
mkdir -p ${root_dir}/products/product_A/2024/sales/Q3
mkdir -p ${root_dir}/products/product_A/2024/sales/Q4

mkdir -p ${root_dir}/products/product_B/2023/product_images
mkdir -p ${root_dir}/products/product_B/2023/product_reviews
mkdir -p ${root_dir}/products/product_B/2023/sales/Q1
mkdir -p ${root_dir}/products/product_B/2023/sales/Q2
mkdir -p ${root_dir}/products/product_B/2023/sales/Q3
mkdir -p ${root_dir}/products/product_B/2023/sales/Q4

mkdir -p ${root_dir}/products/product_B/2024/product_images
mkdir -p ${root_dir}/products/product_B/2024/product_reviews
mkdir -p ${root_dir}/products/product_B/2024/sales/Q1
mkdir -p ${root_dir}/products/product_B/2024/sales/Q2
mkdir -p ${root_dir}/products/product_B/2024/sales/Q3
mkdir -p ${root_dir}/products/product_B/2024/sales/Q4

mkdir -p ${root_dir}/reports/annual_reports
mkdir -p ${root_dir}/reports/monthly_reports
mkdir -p ${root_dir}/reports/quarterly_reports

mkdir -p ${root_dir}/templates/product_description_templates
mkdir -p ${root_dir}/templates/sales_report_templates
mkdir -p ${root_dir}/templates/review_templates

# Create files

# Note: This script does not create the actual files as it would be too long. You can use the 'touch' command to create each file.