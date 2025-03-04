#!/bin/bash

root_dir=$1

mkdir -p $root_dir/01_Course_Development/01_Course_Outlines
mkdir -p $root_dir/01_Course_Development/02_Course_Content
mkdir -p $root_dir/01_Course_Development/03_Assessments
mkdir -p $root_dir/01_Course_Development/04_Multimedia
mkdir -p $root_dir/02_Learning_Management_System/01_Course_Uploads
mkdir -p $root_dir/02_Learning_Management_System/02_Student_Data
mkdir -p $root_dir/02_Learning_Management_System/03_Analytics
mkdir -p $root_dir/03_Student_Communication/01_Emails
mkdir -p $root_dir/03_Student_Communication/02_Discussion_Boards
mkdir -p $root_dir/03_Student_Communication/03_Virtual_Classrooms
mkdir -p $root_dir/04_Professional_Development/01_Webinars
mkdir -p $root_dir/04_Professional_Development/02_Conferences
mkdir -p $root_dir/04_Professional_Development/03_Certifications
mkdir -p $root_dir/05_Resources/01_Articles
mkdir -p $root_dir/05_Resources/02_Books
mkdir -p $root_dir/05_Resources/03_Websites

touch $root_dir/01_Course_Development/01_Course_Outlines/course_outline_v1.docx
touch $root_dir/01_Course_Development/01_Course_Outlines/course_outline_v2.docx
touch $root_dir/01_Course_Development/02_Course_Content/module1_content.docx
touch $root_dir/01_Course_Development/02_Course_Content/module2_content.docx
touch $root_dir/01_Course_Development/03_Assessments/quiz1_questions.docx
touch $root_dir/01_Course_Development/03_Assessments/quiz2_questions.docx
touch $root_dir/01_Course_Development/04_Multimedia/video1.mp4
touch $root_dir/01_Course_Development/04_Multimedia/audio1.mp3
touch $root_dir/02_Learning_Management_System/01_Course_Uploads/course1_upload.zip
touch $root_dir/02_Learning_Management_System/01_Course_Uploads/course2_upload.zip
touch $root_dir/02_Learning_Management_System/02_Student_Data/student1_data.csv
touch $root_dir/02_Learning_Management_System/02_Student_Data/student2_data.csv
touch $root_dir/02_Learning_Management_System/03_Analytics/course1_analytics.pdf
touch $root_dir/02_Learning_Management_System/03_Analytics/course2_analytics.pdf
touch $root_dir/03_Student_Communication/01_Emails/student1_email.docx
touch $root_dir/03_Student_Communication/01_Emails/student2_email.docx
touch $root_dir/03_Student_Communication/02_Discussion_Boards/discussion1_transcript.docx
touch $root_dir/03_Student_Communication/02_Discussion_Boards/discussion2_transcript.docx
touch $root_dir/03_Student_Communication/03_Virtual_Classrooms/virtual_class1_transcript.docx
touch $root_dir/03_Student_Communication/03_Virtual_Classrooms/virtual_class2_transcript.docx
touch $root_dir/04_Professional_Development/01_Webinars/webinar1.mp4
touch $root_dir/04_Professional_Development/01_Webinars/webinar2.mp4
touch $root_dir/04_Professional_Development/02_Conferences/conference1_notes.docx
touch $root_dir/04_Professional_Development/02_Conferences/conference2_notes.docx
touch $root_dir/04_Professional_Development/03_Certifications/certification1.pdf
touch $root_dir/04_Professional_Development/03_Certifications/certification2.pdf
touch $root_dir/05_Resources/01_Articles/article1.pdf
touch $root_dir/05_Resources/01_Articles/article2.pdf
touch $root_dir/05_Resources/02_Books/book1.pdf
touch $root_dir/05_Resources/02_Books/book2.pdf
touch $root_dir/05_Resources/03_Websites/website1_link.txt
touch $root_dir/05_Resources/03_Websites/website2_link.txt
