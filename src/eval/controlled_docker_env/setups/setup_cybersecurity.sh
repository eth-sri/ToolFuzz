#!/bin/bash

root_dir=$1

mkdir -p ${root_dir}/01_Threat_Intelligence/Reports
mkdir -p ${root_dir}/01_Threat_Intelligence/IOCs
mkdir -p ${root_dir}/01_Threat_Intelligence/Threat_Actors
mkdir -p ${root_dir}/02_Vulnerability_Assessment/Scans
mkdir -p ${root_dir}/02_Vulnerability_Assessment/Patches
mkdir -p ${root_dir}/02_Vulnerability_Assessment/Risk_Assessment
mkdir -p ${root_dir}/03_Incident_Response/Incidents
mkdir -p ${root_dir}/03_Incident_Response/Forensics
mkdir -p ${root_dir}/03_Incident_Response/Recovery
mkdir -p ${root_dir}/04_Compliance_and_Audit/Policies
mkdir -p ${root_dir}/04_Compliance_and_Audit/Audits
mkdir -p ${root_dir}/04_Compliance_and_Audit/Regulations
mkdir -p ${root_dir}/05_Training_and_Awareness/Training_Materials
mkdir -p ${root_dir}/05_Training_and_Awareness/Awareness_Campaigns
mkdir -p ${root_dir}/06_Tools_and_Scripts/Tools
mkdir -p ${root_dir}/06_Tools_and_Scripts/Scripts

touch ${root_dir}/01_Threat_Intelligence/Reports/daily_threat_report.pdf
touch ${root_dir}/01_Threat_Intelligence/Reports/weekly_threat_report.pdf
touch ${root_dir}/01_Threat_Intelligence/IOCs/IOC_list.csv
touch ${root_dir}/01_Threat_Intelligence/IOCs/IOC_analysis.docx
touch ${root_dir}/01_Threat_Intelligence/Threat_Actors/actor_profile_A.pdf
touch ${root_dir}/01_Threat_Intelligence/Threat_Actors/actor_profile_B.pdf
touch ${root_dir}/02_Vulnerability_Assessment/Scans/network_scan_report.pdf
touch ${root_dir}/02_Vulnerability_Assessment/Scans/web_scan_report.pdf
touch ${root_dir}/02_Vulnerability_Assessment/Patches/patch_notes_A.docx
touch ${root_dir}/02_Vulnerability_Assessment/Patches/patch_notes_B.docx
touch ${root_dir}/02_Vulnerability_Assessment/Risk_Assessment/risk_assessment_report.pdf
touch ${root_dir}/02_Vulnerability_Assessment/Risk_Assessment/risk_mitigation_plan.docx
touch ${root_dir}/03_Incident_Response/Incidents/incident_report_A.pdf
touch ${root_dir}/03_Incident_Response/Incidents/incident_report_B.pdf
touch ${root_dir}/03_Incident_Response/Forensics/forensic_report_A.pdf
touch ${root_dir}/03_Incident_Response/Forensics/forensic_report_B.pdf
touch ${root_dir}/03_Incident_Response/Recovery/recovery_plan_A.docx
touch ${root_dir}/03_Incident_Response/Recovery/recovery_plan_B.docx
touch ${root_dir}/04_Compliance_and_Audit/Policies/data_protection_policy.pdf
touch ${root_dir}/04_Compliance_and_Audit/Policies/access_control_policy.pdf
touch ${root_dir}/04_Compliance_and_Audit/Audits/audit_report_A.pdf
touch ${root_dir}/04_Compliance_and_Audit/Audits/audit_report_B.pdf
touch ${root_dir}/04_Compliance_and_Audit/Regulations/GDPR_compliance_checklist.pdf
touch ${root_dir}/04_Compliance_and_Audit/Regulations/PCI_DSS_compliance_checklist.pdf
touch ${root_dir}/05_Training_and_Awareness/Training_Materials/phishing_training.ppt
touch ${root_dir}/05_Training_and_Awareness/Training_Materials/password_security_training.ppt
touch ${root_dir}/05_Training_and_Awareness/Awareness_Campaigns/cybersecurity_poster.pdf
touch ${root_dir}/05_Training_and_Awareness/Awareness_Campaigns/cybersecurity_newsletter.pdf
touch ${root_dir}/06_Tools_and_Scripts/Tools/network_monitoring_tool.zip
touch ${root_dir}/06_Tools_and_Scripts/Tools/malware_analysis_tool.zip
touch ${root_dir}/06_Tools_and_Scripts/Scripts/automate_patch_deployment.py
touch ${root_dir}/06_Tools_and_Scripts/Scripts/network_scan_script.py