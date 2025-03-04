#!/bin/bash

root_dir=$1

# Create the root directory
mkdir -p "${root_dir}"

# Create the subdirectories and files
mkdir -p "${root_dir}/Tour_Overview"
touch "${root_dir}/Tour_Overview/Tour_Schedule.docx"
touch "${root_dir}/Tour_Overview/Budget.xlsx"
touch "${root_dir}/Tour_Overview/Contact_List.xlsx"
touch "${root_dir}/Tour_Overview/Logistics_Plan.docx"

# Create Venues structure
for i in 1 2 3 4 5; do # Adjust the number for more venues
    VENUE_DIR="${root_dir}/Venues/Venue_${i}"
    mkdir -p "$VENUE_DIR/Contracts"
    touch "$VENUE_DIR/Contracts/Venue_${i}_Contract.pdf"
    mkdir -p "$VENUE_DIR/Layouts"
    touch "$VENUE_DIR/Layouts/Stage_Layout.pdf"
    touch "$VENUE_DIR/Layouts/Seating_Chart.pdf"
    touch "$VENUE_DIR/Technical_Specs.docx"
    touch "$VENUE_DIR/Contact_Info.docx"
done

# Create Transportation structure
mkdir -p "${root_dir}/Transportation/Vehicle_Contracts"
touch "${root_dir}/Transportation/Travel_Arrangements.docx"
touch "${root_dir}/Transportation/Vehicle_Contracts/Bus_Contract.pdf"
touch "${root_dir}/Transportation/Vehicle_Contracts/Truck_Contract.pdf"
touch "${root_dir}/Transportation/Vehicle_Contracts/Equipment_Van_Contract.pdf"
mkdir -p "${root_dir}/Transportation/Schedules"
touch "${root_dir}/Transportation/Schedules/Departure_Schedule.xlsx"
touch "${root_dir}/Transportation/Schedules/Arrival_Schedule.xlsx"
mkdir -p "${root_dir}/Transportation/Maps/Venue_Maps"
touch "${root_dir}/Transportation/Maps/Route_Map.pdf"
touch "${root_dir}/Transportation/Maps/Venue_Maps/Venue_1_Map.pdf"
touch "${root_dir}/Transportation/Maps/Venue_Maps/Venue_2_Map.pdf"
touch "${root_dir}/Transportation/Maps/Venue_Maps/Venue_N_Map.pdf"

# Create Accommodations structure
mkdir -p "${root_dir}/Accommodations/Hotel_Bookings"
touch "${root_dir}/Accommodations/Hotel_Bookings/Hotel_Venue_1_Confirmation.pdf"
touch "${root_dir}/Accommodations/Hotel_Bookings/Hotel_Venue_2_Confirmation.pdf"
touch "${root_dir}/Accommodations/Hotel_Bookings/Hotel_Venue_N_Confirmation.pdf"
touch "${root_dir}/Accommodations/Rooming_List.xlsx"
touch "${root_dir}/Accommodations/Check_In_Check_Out_Schedule.xlsx"

# Create Equipment structure
mkdir -p "${root_dir}/Equipment/Rental_Agreements"
touch "${root_dir}/Equipment/Inventory_List.xlsx"
touch "${root_dir}/Equipment/Rental_Agreements/Sound_Equipment_Contract.pdf"
touch "${root_dir}/Equipment/Rental_Agreements/Lighting_Equipment_Contract.pdf"
touch "${root_dir}/Equipment/Rental_Agreements/Staging_Equipment_Contract.pdf"
touch "${root_dir}/Equipment/Technical_Requirements.docx"

# Create Staffing structure
mkdir -p "${root_dir}/Staffing/Scheduling"
touch "${root_dir}/Staffing/Crew_List.xlsx"
touch "${root_dir}/Staffing/Roles_and_Responsibilities.docx"
touch "${root_dir}/Staffing/Contact_Information.xlsx"
touch "${root_dir}/Staffing/Scheduling/Crew_Schedule.xlsx"
touch "${root_dir}/Staffing/Scheduling/Shift_Rotation.docx"

# Create Post_Tour structure
mkdir -p "${root_dir}/Post_Tour/Feedback"
touch "${root_dir}/Post_Tour/Debrief_Report.docx"
touch "${root_dir}/Post_Tour/Financial_Report.xlsx"
touch "${root_dir}/Post_Tour/Lessons_Learned.docx"
touch "${root_dir}/Post_Tour/Feedback/Venue_Feedback.xlsx"
touch "${root_dir}/Post_Tour/Feedback/Crew_Feedback.xlsx"
