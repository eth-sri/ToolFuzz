#!/bin/bash

root_dir=$1

mkdir -p $root_dir/archive/bookings
mkdir -p $root_dir/archive/reports
mkdir -p $root_dir/archive/templates
mkdir -p $root_dir/bookings/booking_A/2023/booking_details
mkdir -p $root_dir/bookings/booking_A/2023/customer_feedback
mkdir -p $root_dir/bookings/booking_A/2023/event_plan
mkdir -p $root_dir/bookings/booking_A/2024/booking_details
mkdir -p $root_dir/bookings/booking_A/2024/customer_feedback
mkdir -p $root_dir/bookings/booking_A/2024/event_plan
mkdir -p $root_dir/bookings/booking_B/2023/booking_details
mkdir -p $root_dir/bookings/booking_B/2023/customer_feedback
mkdir -p $root_dir/bookings/booking_B/2023/event_plan
mkdir -p $root_dir/bookings/booking_B/2024/booking_details
mkdir -p $root_dir/bookings/booking_B/2024/customer_feedback
mkdir -p $root_dir/bookings/booking_B/2024/event_plan
mkdir -p $root_dir/reports/annual_reports
mkdir -p $root_dir/reports/monthly_reports
mkdir -p $root_dir/reports/quarterly_reports
mkdir -p $root_dir/templates/booking_templates
mkdir -p $root_dir/templates/feedback_templates
mkdir -p $root_dir/templates/event_plan_templates

touch $root_dir/archive/bookings/archived_booking_A_2021.zip
touch $root_dir/archive/bookings/archived_booking_B_2021.zip
touch $root_dir/archive/reports/archived_annual_report_2021.pdf
touch $root_dir/archive/reports/archived_monthly_report_2021.pdf
touch $root_dir/archive/templates/old_menu_template.docx
touch $root_dir/archive/templates/old_event_plan_template.xlsx
touch $root_dir/bookings/booking_A/2023/booking_details/booking_confirmation.pdf
touch $root_dir/bookings/booking_A/2023/booking_details/booking_invoice.pdf
touch $root_dir/bookings/booking_A/2023/customer_feedback/feedback_form.pdf
touch $root_dir/bookings/booking_A/2023/customer_feedback/feedback_summary.docx
touch $root_dir/bookings/booking_A/2023/event_plan/event_schedule.pdf
touch $root_dir/bookings/booking_A/2023/event_plan/event_layout.pdf
touch $root_dir/bookings/booking_A/2024/booking_details/booking_confirmation.pdf
touch $root_dir/bookings/booking_A/2024/booking_details/booking_invoice.pdf
touch $root_dir/bookings/booking_A/2024/customer_feedback/feedback_form.pdf
touch $root_dir/bookings/booking_A/2024/customer_feedback/feedback_summary.docx
touch $root_dir/bookings/booking_A/2024/event_plan/event_schedule.pdf
touch $root_dir/bookings/booking_A/2024/event_plan/event_layout.pdf
touch $root_dir/bookings/booking_B/2023/booking_details/booking_confirmation.pdf
touch $root_dir/bookings/booking_B/2023/booking_details/booking_invoice.pdf
touch $root_dir/bookings/booking_B/2023/customer_feedback/feedback_form.pdf
touch $root_dir/bookings/booking_B/2023/customer_feedback/feedback_summary.docx
touch $root_dir/bookings/booking_B/2023/event_plan/event_schedule.pdf
touch $root_dir/bookings/booking_B/2023/event_plan/event_layout.pdf
touch $root_dir/bookings/booking_B/2024/booking_details/booking_confirmation.pdf
touch $root_dir/bookings/booking_B/2024/booking_details/booking_invoice.pdf
touch $root_dir/bookings/booking_B/2024/customer_feedback/feedback_form.pdf
touch $root_dir/bookings/booking_B/2024/customer_feedback/feedback_summary.docx
touch $root_dir/bookings/booking_B/2024/event_plan/event_schedule.pdf
touch $root_dir/bookings/booking_B/2024/event_plan/event_layout.pdf
touch $root_dir/reports/annual_reports/annual_report_2023.pdf
touch $root_dir/reports/monthly_reports/february_2023.pdf
touch $root_dir/reports/monthly_reports/january_2023.pdf
touch $root_dir/reports/quarterly_reports/Q1_report_2023.pdf
touch $root_dir/reports/quarterly_reports/Q2_report_2023.pdf
touch $root_dir/templates/booking_templates/advanced_booking_template.docx
touch $root_dir/templates/booking_templates/basic_booking_template.docx
touch $root_dir/templates/feedback_templates/monthly_feedback_template.xlsx
touch $root_dir/templates/feedback_templates/weekly_feedback_template.xlsx
touch $root_dir/templates/event_plan_templates/corporate_event_plan_template.docx
touch $root_dir/templates/event_plan_templates/standard_event_plan_template.docx
