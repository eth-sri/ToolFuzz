# Running the docker evaluation

1. Building the docker image. From this directory run: ```bash
docker build -t eval_container .```
2. Running the docker image. ```bash
docker run eval_container```

There are few helpful scripts to run evaluations in this directory:

1. run_envs.sh - script which will run docker containers in parallel for a list of different environments
2. run_subgroup1..4.sh - in order to have even faster evaluation these scripts run the evaluations on subgroups of the testing environments.
3. run_all.sh - will run all of the candidate tool description against all environments sequentially.

## Base structures

## Accountant file structure

This is the accountant base structure on which all tasks are based on.

The base structure that these containers work with is:

```
.
├── archive
│   ├── clients
│   │   ├── archived_client_A_2021.zip
│   │   └── archived_client_B_2021.zip
│   ├── reports
│   │   ├── archived_annual_report_2021.pdf
│   │   └── archived_monthly_report_2021.pdf
│   └── templates
│       ├── old_invoice_template.docx
│       └── old_payroll_template.xlsx
├── clients
│   ├── client_A
│   │   ├── 2023
│   │   │   ├── financial_statements
│   │   │   │   ├── balance_sheet.pdf
│   │   │   │   └── profit_loss_statement.pdf
│   │   │   ├── invoices
│   │   │   │   ├── invoice_001.pdf
│   │   │   │   └── invoice_002.pdf
│   │   │   ├── payroll
│   │   │   │   ├── employee_payroll_feb.csv
│   │   │   │   └── employee_payroll_jan.csv
│   │   │   └── tax
│   │   │       ├── Q1
│   │   │       │   ├── tax_filing.pdf
│   │   │       │   └── tax_receipt.pdf
│   │   │       ├── Q2
│   │   │       │   ├── tax_filing.pdf
│   │   │       │   └── tax_receipt.pdf
│   │   │       ├── Q3
│   │   │       │   ├── tax_filing.pdf
│   │   │       │   └── tax_receipt.pdf
│   │   │       └── Q4
│   │   │           ├── tax_filing.pdf
│   │   │           └── tax_receipt.pdf
│   │   └── 2024
│   │       ├── financial_statements
│   │       │   ├── balance_sheet.pdf
│   │       │   └── profit_loss_statement.pdf
│   │       ├── invoices
│   │       │   ├── invoice_001.pdf
│   │       │   └── invoice_002.pdf
│   │       ├── payroll
│   │       │   ├── employee_payroll_feb.csv
│   │       │   └── employee_payroll_jan.csv
│   │       └── tax
│   │           ├── Q1
│   │           │   ├── tax_filing.pdf
│   │           │   └── tax_receipt.pdf
│   │           ├── Q2
│   │           │   ├── tax_filing.pdf
│   │           │   └── tax_receipt.pdf
│   │           ├── Q3
│   │           │   ├── tax_filing.pdf
│   │           │   └── tax_receipt.pdf
│   │           └── Q4
│   │               ├── tax_filing.pdf
│   │               └── tax_receipt.pdf
│   └── client_B
│       ├── 2023
│       │   ├── financial_statements
│       │   │   ├── balance_sheet.pdf
│       │   │   └── profit_loss_statement.pdf
│       │   ├── invoices
│       │   │   ├── invoice_001.pdf
│       │   │   └── invoice_002.pdf
│       │   ├── payroll
│       │   │   ├── employee_payroll_feb.csv
│       │   │   └── employee_payroll_jan.csv
│       │   └── tax
│       │       ├── Q1
│       │       │   ├── tax_filing.pdf
│       │       │   └── tax_receipt.pdf
│       │       ├── Q2
│       │       │   ├── tax_filing.pdf
│       │       │   └── tax_receipt.pdf
│       │       ├── Q3
│       │       │   ├── tax_filing.pdf
│       │       │   └── tax_receipt.pdf
│       │       └── Q4
│       │           ├── tax_filing.pdf
│       │           └── tax_receipt.pdf
│       └── 2024
│           ├── financial_statements
│           │   ├── balance_sheet.pdf
│           │   └── profit_loss_statement.pdf
│           ├── invoices
│           │   ├── invoice_001.pdf
│           │   └── invoice_002.pdf
│           ├── payroll
│           │   ├── employee_payroll_feb.csv
│           │   └── employee_payroll_jan.csv
│           └── tax
│               ├── Q1
│               │   ├── tax_filing.pdf
│               │   └── tax_receipt.pdf
│               ├── Q2
│               │   ├── tax_filing.pdf
│               │   └── tax_receipt.pdf
│               ├── Q3
│               │   ├── tax_filing.pdf
│               │   └── tax_receipt.pdf
│               └── Q4
│                   ├── tax_filing.pdf
│                   └── tax_receipt.pdf
├── reports
│   ├── annual_reports
│   │   └── annual_report_2023.pdf
│   ├── monthly_reports
│   │   ├── february_2023.pdf
│   │   └── january_2023.pdf
│   └── quarterly_reports
│       ├── Q1_report_2023.pdf
│       └── Q2_report_2023.pdf
├── templates
│   ├── invoice_templates
│   │   ├── advanced_invoice_template.docx
│   │   └── basic_invoice_template.docx
│   ├── payroll_templates
│   │   ├── monthly_payroll_template.xlsx
│   │   └── weekly_payroll_template.xlsx
│   └── tax_templates
│       ├── corporate_tax_template.docx
│       └── standard_tax_template.docx
```

### Art base structure

```

├── 01_PreProduction
│   ├── 01_Concepts
│   │   ├── Character_Designs
│   │   │   ├── character_sketch_v1.jpg
│   │   │   └── character_sketch_v2.jpg
│   │   ├── Environment_Designs
│   │   │   └── environment_sketch_v1.jpg
│   │   └── Styleframes
│   │       └── styleframe_concept.jpg
│   ├── 02_Script
│   │   ├── Drafts
│   │   │   └── script_draft.txt
│   │   └── Final
│   │       └── final_script.txt
│   ├── 03_Storyboards
│   │   └── storyboard_scene1.jpg
│   ├── 04_Animatic
│   │   └── animatic_v1.mp4
│   └── 05_References
│       └── reference_image.jpg
├── 02_Production
│   ├── 01_Modeling
│   │   ├── Characters
│   │   │   └── character_model_v1.obj
│   │   └── Environments
│   │       └── environment_model_v1.obj
│   ├── 02_Texturing
│   │   ├── Characters
│   │   │   └── character_texture_v1.png
│   │   └── Environments
│   │       └── environment_texture_v1.png
│   ├── 03_Rigging
│   │   ├── Characters
│   │   │   └── character_rig_v1.blend
│   │   └── Props
│   │       └── prop_rig_v1.blend
│   ├── 04_Animation
│   │   ├── Blocking
│   │   │   └── blocking_scene1_v1.mov
│   │   ├── Final
│   │   │   └── final_animation_scene1.mov
│   │   └── Rough
│   │       └── rough_animation_scene1_v1.mov
│   ├── 05_Lighting
│   │   └── lighting_setup_scene1.blend
│   ├── 06_Effects
│   │   └── effects_scene1_v1.blend
│   └── 07_Rendering
│       ├── Comps
│       │   └── scene1_comp_v1.psd
│       └── Render_Layers
│           └── scene1_layer1.exr
├── 03_PostProduction
│   ├── 01_Compositing
│   │   └── scene1_composite_v1.exr
│   ├── 02_Color_Grading
│   │   └── scene1_color_grade_v1.dpx
│   ├── 03_Sound_Design
│   │   ├── Foley
│   │   │   └── footsteps_foley.wav
│   │   └── Music
│   │       └── background_music.mp3
│   ├── 04_VFX
│   │   └── scene1_vfx_v1.mov
│   └── 05_Final_Output
│       └── final_output.mp4
├── 04_Assets
│   ├── Backgrounds
│   │   └── background_image.jpg
│   ├── Characters
│   │   └── character_asset.obj
│   ├── Props
│   │   └── prop_asset.obj
│   └── Textures
│       └── wood_texture.png
├── 05_Documents
│   ├── Budget
│   │   └── budget_plan.xlsx
│   ├── Deliverables
│   │   └── deliverables_checklist.txt
│   ├── Production_Schedule
│   │   └── schedule.xlsx
│   └── Project_Notes
│       └── meeting_notes.txt
└── 06_Renders
    ├── Archive
    │   └── scene1_old_render.mp4
    ├── Final
    │   └── scene1_final_render.mp4
    └── Previews
        └── scene1_preview.mp4
```

### Logistics for concerts tour

```
.
├── Accommodations
│   ├── Check_In_Check_Out_Schedule.xlsx
│   ├── Hotel_Bookings
│   │   ├── Hotel_Venue_1_Confirmation.pdf
│   │   ├── Hotel_Venue_2_Confirmation.pdf
│   │   └── Hotel_Venue_N_Confirmation.pdf
│   └── Rooming_List.xlsx
├── Equipment
│   ├── Inventory_List.xlsx
│   ├── Rental_Agreements
│   │   ├── Lighting_Equipment_Contract.pdf
│   │   ├── Sound_Equipment_Contract.pdf
│   │   └── Staging_Equipment_Contract.pdf
│   └── Technical_Requirements.docx
├── Post_Tour
│   ├── Debrief_Report.docx
│   ├── Feedback
│   │   ├── Crew_Feedback.xlsx
│   │   └── Venue_Feedback.xlsx
│   ├── Financial_Report.xlsx
│   └── Lessons_Learned.docx
├── Staffing
│   ├── Contact_Information.xlsx
│   ├── Crew_List.xlsx
│   ├── Roles_and_Responsibilities.docx
│   └── Scheduling
│       ├── Crew_Schedule.xlsx
│       └── Shift_Rotation.docx
├── Tour_Overview
│   ├── Budget.xlsx
│   ├── Contact_List.xlsx
│   ├── Logistics_Plan.docx
│   └── Tour_Schedule.docx
├── Transportation
│   ├── Maps
│   │   ├── Route_Map.pdf
│   │   └── Venue_Maps
│   │       ├── Venue_1_Map.pdf
│   │       ├── Venue_2_Map.pdf
│   │       └── Venue_N_Map.pdf
│   ├── Schedules
│   │   ├── Arrival_Schedule.xlsx
│   │   └── Departure_Schedule.xlsx
│   ├── Travel_Arrangements.docx
│   └── Vehicle_Contracts
│       ├── Bus_Contract.pdf
│       ├── Equipment_Van_Contract.pdf
│       └── Truck_Contract.pdf
└── Venues
    ├── Venue_1
    │   ├── Contact_Info.docx
    │   ├── Contracts
    │   │   └── Venue_1_Contract.pdf
    │   ├── Layouts
    │   │   ├── Seating_Chart.pdf
    │   │   └── Stage_Layout.pdf
    │   └── Technical_Specs.docx
    ├── Venue_2
    │   ├── Contact_Info.docx
    │   ├── Contracts
    │   │   └── Venue_2_Contract.pdf
    │   ├── Layouts
    │   │   ├── Seating_Chart.pdf
    │   │   └── Stage_Layout.pdf
    │   └── Technical_Specs.docx
    ├── Venue_3
    │   ├── Contact_Info.docx
    │   ├── Contracts
    │   │   └── Venue_3_Contract.pdf
    │   ├── Layouts
    │   │   ├── Seating_Chart.pdf
    │   │   └── Stage_Layout.pdf
    │   └── Technical_Specs.docx
    ├── Venue_4
    │   ├── Contact_Info.docx
    │   ├── Contracts
    │   │   └── Venue_4_Contract.pdf
    │   ├── Layouts
    │   │   ├── Seating_Chart.pdf
    │   │   └── Stage_Layout.pdf
    │   └── Technical_Specs.docx
    └── Venue_5
        ├── Contact_Info.docx
        ├── Contracts
        │   └── Venue_5_Contract.pdf
        ├── Layouts
        │   ├── Seating_Chart.pdf
        │   └── Stage_Layout.pdf
        └── Technical_Specs.docx
```

Questions for meeting:

1. The following prompt I don't like:
   `Could you locate and move all 2023 financial statements for Client A into an archive folder?`- I think it is testing
   planning more than the tool itself. (opinions?)

Failing environment prompt creations:
Error for field: Virtual Reality (VR) and Augmented Reality (AR)
Failed to parse Prompts from completion {"prompt": "Move the VR Designs to the VR Assets Folder", "shell_script": "
mv \"$PROJECT_NAME/01_PreProduction/01_Concepts/VR_Designs/*\" \"$PROJECT_NAME/04_Assets/VR_Assets/\""}. Got: 1
validation error for Prompts
prompts
Field required [type=missing, input_value={'prompt': 'Move the VR D.../04_Assets/VR_Assets/"'}, input_type=dict]
For further information visit https://errors.pydantic.dev/2.9/v/missing
For troubleshooting, visit: https://python.langchain.com/docs/troubleshooting/errors/OUTPUT_PARSING_FAILURE
Generating environments for fields.:  88%|████████▊ | 37/42 [48:52<06:30, 78.19s/it]Error for field: Forensic Science
Failed to parse Prompts from completion {"prompt": "Move the DNA sample from Case 001 in Open Cases to the corresponding
case in Closed Cases", "shell_script": "mv '01_Case_Files/01_Open_Cases/Case_001/Evidence/DNA_Samples/sample_001.dna' '
01_Case_Files/02_Closed_Cases/Case_001/Evidence/DNA_Samples/'"}. Got: 1 validation error for Prompts
prompts
Field required [type=missing, input_value={'prompt': 'Move the DNA ...Evidence/DNA_Samples/'"}, input_type=dict]

## Validating our baseline:

- [ ] setup_accountant
- [x] setup_agriculture_and_precision_farming
- [ ] setup_art
- [ ] setup_artificial_intelligence
- [ ] setup_astronomy_and_space_exploration
- [x] setup_biotechnology
- [x] setup_computer_science
- [ ] setup_construction_and_architecture
- [x] setup_cybersecurity
- [x] setup_data_science
- [ ] setup_e-commerce_and_retail
- [x] setup_economics_and_market_research
- [x] setup_education_and_e-learning
- [ ] setup_energy_and_utilities
- [ ] setup_engineering_(mechanical,_electrical,_civil,_etc.)
- [x] setup_entertainment_and_media
- [x] setup_environmental_science
- [x] setup_finance_and_banking
- [x] setup_forensic_science
- [x] setup_geology_and_geophysics
- [x] setup_government_and_public_administration
- [x] setup_graphic_design_and_animation
- [x] setup_healthcare_and_medicine
- [x] setup_history_and_archival_science
- [x] setup_hospitality_and_tourism
- [x] setup_human_resources_and_recruitment
- [x] setup_journalism_and_digital_media
- [x] setup_law_and_legal_analytics
- [x] setup_linguistics_and_natural_language_processing
- [x] setup_logistics
- [x] setup_logistics_and_supply_chain_management
- [x] setup_machine_learning
- [x] setup_manufacturing_and_automation
- [x] setup_meteorology_and_climate_science
- [x] setup_music_production_and_sound_engineering
- [x] setup_pharmaceuticals_and_drug_development
- [x] setup_psychology_and_neuroscience
- [x] setup_real_estate
- [ ] setup_robotics -1
- [x] setup_social_media_and_digital_marketing
- [x] setup_sports_science_and_analytics
- [ ] setup_telecommunications -
- [x] setup_transportation_(autonomous_vehicles,_traffic_management)
- [x] setup_video_game_development
- [x] setup_virtual_reality_(vr)_and_augmented_reality_(ar)

# Results:

Default description of terminal and agent with Gpt-4o-mini
Agent has information on what the working directory is.

| Description         | Number of Success | Number of Failures | Total Number | Agent Model | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------|-------------------|--------------------|--------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Default description | 57                | 110                | 167          | GPT-4o-mini | Run shell commands on this {_get_platform()} machine.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| GPT-4 just descr    | 52                | 114                | 166          | GPT-4o-mini | The 'terminal' tool allows you to execute shell commands on a Linux machine. The 'commands' parameter, which is required, accepts a list of shell commands to be executed. This list can be provided as a single string or as an array of strings. The commands are deserialized using the json.loads function.                                                                                                                                                                                                                                                                                                                                                                                                                |
| GPT-4 descr + src   | 47                | 120                | 167          | GPT-4o-mini | The 'terminal' tool is designed to execute shell commands on a Linux machine. It accepts a list of commands as input, either as a single string or an array of strings. If the 'ask_human_input' attribute is set to true, the tool will prompt the user for confirmation before executing any command generated by the language model in the bash shell. The tool returns the final output of the executed commands. In case of an error during command execution, the error is logged and the tool returns 'None'.                                                                                                                                                                                                           |
| GPT-4 fuzz examples | 51                | 114                | 165          | GPT-4o-mini | The 'terminal' tool is designed to execute shell commands on a Linux machine. It accepts a list of commands as input, which can be either a single string or an array of strings. The commands are then deserialized using json.loads. The tool also includes an optional feature to prompt the user for confirmation before executing a command generated by the language model in the bash shell. The tool's functionality is encapsulated in the ShellTool class, which includes methods for running the commands and handling any exceptions that may occur during execution. Please note that the tool requires precise command inputs to function correctly, as it does not interpret or modify the commands in any way. |

| Description         | Number of Success | Number of Failures | Total Number | Agent Model | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------|-------------------|--------------------|--------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Default description | 53                | 124                | 177          | GPT-4o-mini | Run shell commands on this {_get_platform()} machine.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| GPT-4 just descr    | 53                | 123                | 176          | GPT-4o-mini | The 'terminal' tool allows you to execute shell commands on a Linux machine. The 'commands' parameter, which is required, accepts a list of shell commands to be executed. This list can be provided as a single string or as an array of strings. The commands are deserialized using the json.loads function.                                                                                                                                                                                                                                                                                                                                                                                                                |
| GPT-4 descr + src   | 44                | 132                | 176          | GPT-4o-mini | The 'terminal' tool is designed to execute shell commands on a Linux machine. It accepts a list of commands as input, either as a single string or an array of strings. If the 'ask_human_input' attribute is set to true, the tool will prompt the user for confirmation before executing any command generated by the language model in the bash shell. The tool returns the final output of the executed commands. In case of an error during command execution, the error is logged and the tool returns 'None'.                                                                                                                                                                                                           |
| GPT-4 fuzz examples | 42                | 135                | 177          | GPT-4o-mini | The 'terminal' tool is designed to execute shell commands on a Linux machine. It accepts a list of commands as input, which can be either a single string or an array of strings. The commands are then deserialized using json.loads. The tool also includes an optional feature to prompt the user for confirmation before executing a command generated by the language model in the bash shell. The tool's functionality is encapsulated in the ShellTool class, which includes methods for running the commands and handling any exceptions that may occur during execution. Please note that the tool requires precise command inputs to function correctly, as it does not interpret or modify the commands in any way. |

description="The 'terminal' tool allows you to execute shell commands on a Linux machine. The 'commands' parameter,
which is required, accepts a list of shell commands to be run. This list can be provided as a single string or as an
array of strings. The commands are deserialized using the json.loads function."

description="The 'terminal' tool is designed to execute shell commands on a Linux machine. It accepts a list of commands
as input, either as a single string or an array of strings. If the 'ask_human_input' attribute is set to true, the tool
will prompt the user for confirmation before executing any command generated by the language model in the bash shell.
The tool returns the final output of the executed commands. In case of an error during command execution, the tool logs
the error and returns 'None'."

[1] description="The 'terminal' tool is designed to execute shell commands on a Linux machine. The 'commands' parameter
is required and should contain the shell commands to be run. This parameter accepts either a single string or an array
of strings. Each string should represent a valid shell command. For instance, to check the disk space used in a
directory, the command 'du -sh /directory_path' should be used. To list files in a directory, use 'ls /directory_path'.
To list all files, including hidden ones, use 'ls -a'. Please note that the tool will prompt for user confirmation
before executing a command generated by the language model in the bash shell if the 'ask_human_input' attribute is set
to True. The tool returns the final output of the executed commands."

[2] description="This tool allows you to execute shell commands on a Linux machine. The 'commands' parameter is required
and it should contain the shell commands to be executed. The commands can be provided as a single string or as an array
of strings. Each string should represent a complete shell command. For example, to check the disk usage in a specific
directory, the command should be 'du -sh /directory_name'. To list all files, the command should be 'ls -la'. Please
note that the commands are deserialized using json.loads, so they should be properly formatted as valid JSON strings or
arrays."

| Description         | Number of Success | Number of Failures | Total Number | Agent Model | Description |
|---------------------|-------------------|--------------------|--------------|-------------|-------------|
| GPT-4 fuzz examples | 48                | 126                | 174          | GPT-4o-mini | (1) w/ src  |
| GPT-4 fuzz examples | 51                | 126                | 177          | GPT-4o-mini | (2) no/ src |

## Rerun of experiments with system prompt instead of Human prompt for meat info on where the model is located:

System prompt: You should know that you are operating in the home directory: /, but the workspace is in
/agentworkspace/workfiles.

**Descriptions**:

0. Default
1. GPT-4 just description given and asked to improve it
2. GPT-4 description and source code given
3. GPT-4 fuzz examples

1 - "The 'terminal' tool allows you to execute shell commands on a Linux machine. The 'commands' parameter,
which is required, accepts a list of shell commands to be run. This list can be provided as a single string or as an
array of strings. The commands are deserialized using the json.loads function."

2 -"The 'terminal' tool is designed to execute shell commands on a Linux machine. It accepts a list of commands
as input, either as a single string or an array of strings. If the 'ask_human_input' attribute is set to true, the tool
will prompt the user for confirmation before executing any command generated by the language model in the bash shell.
The tool returns the final output of the executed commands. In case of an error during command execution, the tool logs
the error and returns 'None'."

3 - "This tool allows you to execute shell commands on a Linux machine. The 'commands' parameter is required
and it should contain the shell commands to be executed. The commands can be provided as a single string or as an array
of strings. Each string should represent a complete shell command. For example, to check the disk usage in a specific
directory, the command should be 'du -sh /directory_name'. To list all files, the command should be 'ls -la'. Please
note that the commands are deserialized using json.loads, so they should be properly formatted as valid JSON strings or
arrays."

4 - The 'terminal' tool allows you to execute shell commands on a Linux machine. The 'commands' parameter is required
and accepts either a single string or an array of strings, each representing a shell command to be executed. The
commands are deserialized using json.loads. If the 'ask_human_input' attribute is set to true, the tool will prompt for
user confirmation before executing a command generated by the language model in the bash shell. Please note that the
tool may not correctly interpret or execute complex commands or those that require specific contextual understanding. It
is recommended to use simple, direct commands for optimal results.

| Description         | Number of Success | Number of Failures | Total Number    | Agent Model |
|---------------------|-------------------|--------------------|-----------------|-------------|
| Default             | 48                | 130                | 178             | GPT-4o-mini |
| GPT-4 descr         | 51                | 126                | 177 + 1 (crash) | GPT-4o-mini |
| GPT-4 descr + src   | 46                | 132                | 178             | GPT-4o-mini |
| GPT-4 fuzz examples | 56                | 122                | 178             | GPT-4o-mini |
| GPT-4 fuzz ex + src |                   |                    |                 | GPT-4o-mini |

### Benchmarks without the system prompt:

| Description         | Number of Success | Number of Failures | Total Number    | Agent Model |
|---------------------|-------------------|--------------------|-----------------|-------------|
| Default             | 35                | 139                | 174 + 4 (crash) | GPT-4o-mini |
| GPT-4 descr         | 33                | 141                | 174 + 4 (crash) | GPT-4o-mini |
| GPT-4 descr + src   | 33                | 143                | 176 + 2 (crash) | GPT-4o-mini |
| GPT-4 fuzz examples | 33                | 143                | 176 + 2 (crash) | GPT-4o-mini |
| GPT-4 fuzz ex + src | 34                | 141                | 175 + 2 (crash) | GPT-4o-mini |

### Benchmarks with the system prompt:

sys prompt -> "You are an AI agent operating in the home directory: /, the workspace of your user is
in/agentworkspace/workfiles."

1 - "The 'terminal' tool allows you to execute shell commands on a Linux machine. The 'commands' parameter,
which is required, accepts a list of shell commands to be run. This list can be provided as a single string or as an
array of strings. The commands are deserialized using the json.loads function."

2 -"The 'terminal' tool is designed to execute shell commands on a Linux machine. It accepts a list of commands
as input, either as a single string or an array of strings. If the 'ask_human_input' attribute is set to true, the tool
will prompt the user for confirmation before executing any command generated by the language model in the bash shell.
The tool returns the final output of the executed commands. In case of an error during command execution, the tool logs
the error and returns 'None'."

3 - "This tool allows you to execute shell commands on a Linux machine. The 'commands' parameter is required
and it should contain the shell commands to be executed. The commands can be provided as a single string or as an array
of strings. Each string should represent a complete shell command. For example, to check the disk usage in a specific
directory, the command should be 'du -sh /directory_name'. To list all files, the command should be 'ls -la'. Please
note that the commands are deserialized using json.loads, so they should be properly formatted as valid JSON strings or
arrays."

4 - The 'terminal' tool allows you to execute shell commands on a Linux machine. The 'commands' parameter is required
and accepts either a single string or an array of strings, each representing a shell command to be executed. The
commands are deserialized using json.loads. If the 'ask_human_input' attribute is set to true, the tool will prompt for
user confirmation before executing a command generated by the language model in the bash shell. Please note that the
tool may not correctly interpret or execute complex commands or those that require specific contextual understanding. It
is recommended to use simple, direct commands for optimal results.

| Description         | Number of Success | Number of Failures | Total Number | Agent Model |
|---------------------|-------------------|--------------------|--------------|-------------|
| Default             | 45                | 133                | 178          | GPT-4o-mini |
| GPT-4 descr         | 53                | 123                | 176 + 2      | GPT-4o-mini |
| GPT-4 descr + src   | 42                | 135                | 177 + 1      | GPT-4o-mini |
| GPT-4 fuzz examples | 45                | 120                | 165 + 13     | GPT-4o-mini |
| GPT-4 fuzz ex + src | 46                | 130                | 176 + 2      | GPT-4o-mini |

### Benchmarks with the system prompt and better model

sys prompt -> "You are an AI agent operating in the home directory: /, the workspace of your user is
in/agentworkspace/workfiles."

1 - "The 'terminal' tool allows you to execute shell commands on a Linux machine. The 'commands' parameter,
which is required, accepts a list of shell commands to be run. This list can be provided as a single string or as an
array of strings. The commands are deserialized using the json.loads function."

2 -"The 'terminal' tool is designed to execute shell commands on a Linux machine. It accepts a list of commands
as input, either as a single string or an array of strings. If the 'ask_human_input' attribute is set to true, the tool
will prompt the user for confirmation before executing any command generated by the language model in the bash shell.
The tool returns the final output of the executed commands. In case of an error during command execution, the tool logs
the error and returns 'None'."

3 - "This tool allows you to execute shell commands on a Linux machine. The 'commands' parameter is required
and it should contain the shell commands to be executed. The commands can be provided as a single string or as an array
of strings. Each string should represent a complete shell command. For example, to check the disk usage in a specific
directory, the command should be 'du -sh /directory_name'. To list all files, the command should be 'ls -la'. Please
note that the commands are deserialized using json.loads, so they should be properly formatted as valid JSON strings or
arrays."

4 - The 'terminal' tool allows you to execute shell commands on a Linux machine. The 'commands' parameter is required
and accepts either a single string or an array of strings, each representing a shell command to be executed. The
commands are deserialized using json.loads. If the 'ask_human_input' attribute is set to true, the tool will prompt for
user confirmation before executing a command generated by the language model in the bash shell. Please note that the
tool may not correctly interpret or execute complex commands or those that require specific contextual understanding. It
is recommended to use simple, direct commands for optimal results.

| Description         | Number of Success | Number of Failures | Total Number | Agent Model |
|---------------------|-------------------|--------------------|--------------|-------------|
| Default             | 56                | 116                | 172+6        | GPT-4o      |
| GPT-4 descr         | 50                | 125                | 175+2        | GPT-4o      |
| GPT-4 descr + src   | 45                | 131                | 176+2        | GPT-4o      |
| GPT-4 fuzz examples | 62                | 108                | 170+8        | GPT-4o      |
| GPT-4 fuzz ex + src | 51                | 124                | 175+2        | GPT-4o      |

### Benchmarks with no workspace location in system prompt and better model

| Description         | Number of Success | Number of Failures | Total Number | Agent Model |
|---------------------|-------------------|--------------------|--------------|-------------|
| Default             | 46                | 105                | 151          | GPT-4o      |
| GPT-4 descr         | 49                | 109                | 158          | GPT-4o      |
| GPT-4 descr + src   | 38                | 125                | 163          | GPT-4o      |
| GPT-4 fuzz examples | 40                | 113                | 153          | GPT-4o      |
| GPT-4 fuzz ex + src | 41                | 127                | 168          | GPT-4o      |
| GPT-4 fuzz ex + src | 28                | 30                 | 58           | GPT-4o      |
| GPT-4 fuzz          | 49                | 129                | 178          | GPT-4o      |
| GPT-4 custom        | 58                | 120                | 178          | GPT-4o      |
| GPT-4 custom 2      | 61                | 117                | 178          | GPT-4o      |
| GPT-4 custom 3      | 70                | 108                | 178          | GPT-4o      |
| GPT-4 custom 4      | 93                | 85                 | 178          | GPT-4o      |

### Benchmarks with generated prompts:

| Description | Number of Success | Number of Failures | Total Number | Agent Model | Pas rate |
|-------------|-------------------|--------------------|--------------|-------------|----------|
| Default     | 47                | 131                | 178          | GPT-4o      | 26.4%    |
| 1.16 gen    | 54                | 124                | 178          | GPT-4o      | 30.3%    |
| 1.26 gen    | 45                | 133                | 178          | GPT-4o      | 25.2%    |
| 2.31 gen    | 56                | 121                | 178          | GPT-4o      | 31.5%    |
| 2.11 gen    | 65                | 114                | 178          | GPT-4o      | 36.4%    |
| 2.42 gen    | 57                | 121                | 178          | GPT-4o      | 32.0%    |

## Benchmarks for File Toolkit

| Description     | Number of Success | Number of Failures | Total Number | Agent Model | Pas rate |
|-----------------|-------------------|--------------------|--------------|-------------|----------|
| Default         | 33                | 145                | 178          | GPT-4o      | 18.5%    |
| Generation      |                   |                    |              |             |          |
| Default env fix | 85                | 99                 | 184          | GPT-4o      | 46.19%   |
| Env fix gen 0   | 89                | 95                 | 184          | GPT-4o      | 48.3%    |
| Env fix gen 19  | 66                | 118                | 184          | GPT-4o      | 35.8%    |
| Env fix gen 18  | 77                | 107                | 184          | GPT-4o      | 41.8%    |
| Env fix gen 14  | 81                | 103                | 184          | GPT-4o      | 44.0%    |
| Env fix gen 11  | 54                | 130                | 187          | GPT-4o      | 29.3%    |

### env fix gen 11

| Category                               | Pass | Fails |
|----------------------------------------|------|-------|
| government_and_public_administration   | 1    | 4     |
| data_science                           | 2    | 3     |
| computer_science                       | 3    | 3     |
| entertainment_and_media                | 1    | 9     |
| manufacturing_and_automation           | 2    | 3     |
| economics_and_market_research          | 1    | 4     |
| journalism_and_digital_media           | 3    | 3     |
| machine_learning                       | 1    | 5     |
| meteorology_and_climate_science        | 4    | 6     |
| environmental_science                  | 4    | 1     |
| video_game_development                 | 1    | 7     |
| hospitality_and_tourism                | 1    | 4     |
| social_media_and_digital_marketing     | 1    | 4     |
| finance_and_banking                    | 1    | 7     |
| cybersecurity                          | 2    | 4     |
| construction_and_architecture          | 0    | 5     |
| history_and_archival_science           | 2    | 4     |
| education_and_e-learning               | 1    | 4     |
| real_estate                            | 0    | 5     |
| logistics_and_supply_chain_management  | 1    | 4     |
| graphic_design_and_animation           | 2    | 3     |
| pharmaceuticals_and_drug_development   | 1    | 4     |
| human_resources_and_recruitment        | 0    | 5     |
| sports_science_and_analytics           | 3    | 4     |
| psychology_and_neuroscience            | 2    | 4     |
| agriculture_and_precision_farming      | 4    | 6     |
| geology_and_geophysics                 | 3    | 2     |
| music_production_and_sound_engineering | 3    | 7     |
| biotechnology                          | 3    | 2     |
| law_and_legal_analytics                | 1    | 4     |

### Default desc Run:

| Category                               | Pass | Fails |
|----------------------------------------|------|-------|
| computer_science                       | 4    | 2     |
| data_science                           | 3    | 2     |
| logistics_and_supply_chain_management  | 4    | 1     |
| hospitality_and_tourism                | 2    | 3     |
| government_and_public_administration   | 2    | 3     |
| machine_learning                       | 3    | 3     |
| human_resources_and_recruitment        | 0    | 5     |
| cybersecurity                          | 3    | 3     |
| finance_and_banking                    | 2    | 6     |
| agriculture_and_precision_farming      | 6    | 4     |
| construction_and_architecture          | 0    | 5     |
| real_estate                            | 1    | 4     |
| manufacturing_and_automation           | 2    | 3     |
| economics_and_market_research          | 3    | 2     |
| education_and_e-learning               | 1    | 4     |
| pharmaceuticals_and_drug_development   | 3    | 2     |
| sports_science_and_analytics           | 6    | 1     |
| history_and_archival_science           | 3    | 3     |
| video_game_development                 | 3    | 5     |
| psychology_and_neuroscience            | 6    | 0     |
| geology_and_geophysics                 | 2    | 3     |
| graphic_design_and_animation           | 2    | 3     |
| meteorology_and_climate_science        | 6    | 4     |
| law_and_legal_analytics                | 0    | 5     |
| music_production_and_sound_engineering | 2    | 8     |
| biotechnology                          | 3    | 2     |
| entertainment_and_media                | 3    | 7     |
| environmental_science                  | 3    | 2     |
| journalism_and_digital_media           | 5    | 1     |
| social_media_and_digital_marketing     | 2    | 3     |

### Run with prompt 0:

| Category                               | Pass | Fails |
|----------------------------------------|------|-------|
| education_and_e-learning               | 1    | 4     |
| journalism_and_digital_media           | 5    | 1     |
| human_resources_and_recruitment        | 0    | 5     |
| history_and_archival_science           | 5    | 1     |
| video_game_development                 | 2    | 6     |
| government_and_public_administration   | 3    | 2     |
| machine_learning                       | 2    | 4     |
| manufacturing_and_automation           | 3    | 2     |
| cybersecurity                          | 1    | 5     |
| economics_and_market_research          | 1    | 4     |
| data_science                           | 4    | 1     |
| pharmaceuticals_and_drug_development   | 3    | 2     |
| sports_science_and_analytics           | 5    | 2     |
| computer_science                       | 4    | 2     |
| real_estate                            | 1    | 4     |
| meteorology_and_climate_science        | 4    | 6     |
| environmental_science                  | 3    | 2     |
| geology_and_geophysics                 | 2    | 3     |
| entertainment_and_media                | 5    | 5     |
| construction_and_architecture          | 3    | 2     |
| law_and_legal_analytics                | 0    | 5     |
| biotechnology                          | 4    | 1     |
| logistics_and_supply_chain_management  | 2    | 3     |
| psychology_and_neuroscience            | 5    | 1     |
| graphic_design_and_animation           | 3    | 2     |
| agriculture_and_precision_farming      | 7    | 3     |
| social_media_and_digital_marketing     | 3    | 2     |
| hospitality_and_tourism                | 3    | 2     |
| music_production_and_sound_engineering | 3    | 7     |
| finance_and_banking                    | 2    | 6     |

## Terminal final benchmarks:

Prompt 0: 43 successful, 100 errors, 143 total, 30.07% pass rate
Prompt 1: 62 successful, 81 errors, 143 total, 43.36% pass rate
Prompt 2: 23 successful, 120 errors, 143 total, 16.08% pass rate
Prompt 3: 52 successful, 91 errors, 143 total, 36.36% pass rate
Prompt 4: 35 successful, 108 errors, 143 total, 24.48% pass rate
Prompt 5: 36 successful, 107 errors, 143 total, 25.17% pass rate
Prompt 6: 35 successful, 108 errors, 143 total, 24.48% pass rate
Prompt 7: 30 successful, 113 errors, 143 total, 20.98% pass rate
Prompt 8: 58 successful, 85 errors, 143 total, 40.56% pass rate
Prompt 9: 33 successful, 110 errors, 143 total, 23.08% pass rate
Prompt 10: 44 successful, 99 errors, 143 total, 30.77% pass rate
Prompt 11: 34 successful, 109 errors, 143 total, 23.78% pass rate
Prompt 12: 46 successful, 97 errors, 143 total, 32.17% pass rate
Prompt 13: 29 successful, 114 errors, 143 total, 20.28% pass rate
Prompt 14: 32 successful, 111 errors, 143 total, 22.38% pass rate
Prompt 15: 31 successful, 112 errors, 143 total, 21.68% pass rate
Prompt 16: 39 successful, 104 errors, 143 total, 27.27% pass rate
Prompt 17: 34 successful, 109 errors, 143 total, 23.78% pass rate
Prompt 18: 47 successful, 96 errors, 143 total, 32.87% pass rate
Prompt 19: 52 successful, 91 errors, 143 total, 36.36% pass rate
Total pass rate @top 1: 43.36%
Total pass rate @top 5: 37.90%
Total pass rate @top 10: 33.50%
Total pass rate: 27.80%
Prompt def: 31 successful, 113 errors, 144 total, 21.53% pass rate


**Total pass rate @top 1:** 43.36%

**Total pass rate @top 5:** 37.90%

**Total pass rate @top 10:** 33.50%

**Total pass rate all 20:** 27.80%

**Default prompt pass rate:** 21.53%

## File management toolkit:

Prompt 0: 65 successful, 80 errors, 145 total, 44.83% pass rate
Prompt 1: 72 successful, 91 errors, 163 total, 44.17% pass rate
Prompt 2: 80 successful, 83 errors, 163 total, 49.08% pass rate
Prompt 3: 74 successful, 89 errors, 163 total, 45.40% pass rate
Prompt 4: 76 successful, 87 errors, 163 total, 46.63% pass rate
Prompt 5: 71 successful, 92 errors, 163 total, 43.56% pass rate
Prompt 6: 67 successful, 96 errors, 163 total, 41.10% pass rate
Prompt 7: 71 successful, 92 errors, 163 total, 43.56% pass rate
Prompt 8: 74 successful, 89 errors, 163 total, 45.40% pass rate
Prompt 9: 78 successful, 85 errors, 163 total, 47.85% pass rate
Prompt 10: 67 successful, 96 errors, 163 total, 41.10% pass rate
Prompt 11: 81 successful, 82 errors, 163 total, 49.69% pass rate
Prompt 12: 74 successful, 89 errors, 163 total, 45.40% pass rate
Prompt 13: 75 successful, 88 errors, 163 total, 46.01% pass rate
Prompt 14: 77 successful, 86 errors, 163 total, 47.24% pass rate
Prompt 15: 73 successful, 90 errors, 163 total, 44.79% pass rate
Prompt 16: 68 successful, 95 errors, 163 total, 41.72% pass rate
Prompt 17: 99 successful, 123 errors, 222 total, 44.59% pass rate
Prompt 18: 74 successful, 89 errors, 163 total, 45.40% pass rate
Prompt 19: 55 successful, 108 errors, 163 total, 33.74% pass rate

**Total pass rate @top 1:** 49.69%

**Total pass rate @top 5:** 48.10%

**Total pass rate @top 10:** 46.81%

**Total pass rate at 20:** 44.56%

**Default description pass rate:** 45.4%