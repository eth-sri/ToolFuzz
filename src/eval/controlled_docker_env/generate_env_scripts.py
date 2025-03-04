import os
from typing import List

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from tqdm import tqdm

from src.eval.toolfuzz.utils.setup import init_model

GENERATE_FILE_STRUCTURE = """
Can you generate a file structure for specialist working in the field of: {field}.
Here is example of one for accountant:
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
└── templates
   ├── invoice_templates
   │   ├── advanced_invoice_template.docx
   │   └── basic_invoice_template.docx
   ├── payroll_templates
   │   ├── monthly_payroll_template.xlsx
   │   └── weekly_payroll_template.xlsx
   └── tax_templates
       ├── corporate_tax_template.docx
       └── standard_tax_template.docx

Here is example for artistic person:
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

Now please generate something similar for a profession in the field of {field}.

{format_instructions}
"""

FIELDS = [
    "Computer Science",
    "Data Science",
    "Artificial Intelligence",
    "Machine Learning",
    "Cybersecurity",
    "Finance and Banking",
    "Healthcare and Medicine",
    "Biotechnology",
    "Engineering (Mechanical, Electrical, Civil, etc.)",
    "Education and E-learning",
    "Entertainment and Media",
    "Graphic Design and Animation",
    "Video Game Development",
    "Meteorology and Climate Science",
    "Astronomy and Space Exploration",
    "E-commerce and Retail",
    "Logistics and Supply Chain Management",
    "Transportation (Autonomous Vehicles, Traffic Management)",
    "Agriculture and Precision Farming",
    "Construction and Architecture",
    "Real Estate",
    "Telecommunications",
    "Robotics",
    "Law and Legal Analytics",
    "Government and Public Administration",
    "Environmental Science",
    "Manufacturing and Automation",
    "Psychology and Neuroscience",
    "Social Media and Digital Marketing",
    "Journalism and Digital Media",
    "Music Production and Sound Engineering",
    "Virtual Reality (VR) and Augmented Reality (AR)",
    "Pharmaceuticals and Drug Development",
    "Human Resources and Recruitment",
    "Energy and Utilities",
    "Geology and Geophysics",
    "Forensic Science",
    "Linguistics and Natural Language Processing",
    "Economics and Market Research",
    "History and Archival Science",
    "Hospitality and Tourism",
    "Sports Science and Analytics"
]

GENERATE_FILE_STRUCTURE_BASH = """
Given the file structure:
{file_structure}

Output only a JSON object containing the bash shell script as a single string, create each file separately.
This script has to create all the files listed in the file structure.
Please define a root_dir=$1 variable within the shell script.

{format_instructions}
"""

GENERATE_PROMPTS_AND_SCRIPTS = """
Given the file structure:
{file_structure}

Can you generate prompts for an agent tool {agent_tool}?
After the prompt write up to 3 commands that will do the action required in the prompt given that the file structure already exists, so just the commands that modify it in the way the prompt asks.

Some examples from other categories:
"prompt": "Move the Final Script to the Deliverables Folder",
"shell_script": "cp \"$PROJECT_NAME/01_PreProduction/02_Script/Final/final_script.txt\" \"$PROJECT_NAME/05_Documents/Deliverables/final_script.txt\""

"prompt": "Archive Outdated Concept Art",
"shell_script": "mkdir -p \"$PROJECT_NAME/04_ASSETS/Archive\"\nmv \"$PROJECT_NAME/01_PreProduction/01_Concepts/Character_Designs/character_sketch_v1.jpg\" \"$PROJECT_NAME/04_Assets/Archive/character_sketch_v1.jpg\""

"prompt": "Move Final Character Models to the Characters Asset Folder",
"shell_script": "mv \"$PROJECT_NAME/02_Production/01_Modeling/Characters/character_model_v1.png\" \"$PROJECT_NAME/04_Assets/Characters/character_model.png\""

"prompt": "Backup Current Staffing Documents to folder CloudBackup for cloud storage upload later",
"shell_script": "mkdir -p \"$ROOT_DIR/CloudBackup\"\ncp \"$ROOT_DIR/Staffing/*\" \"$ROOT_DIR/CloudBackup\""

"prompt": "Move the first three venues to Archive folder",
"shell_script": "mkdir -p \"$ROOT_DIR/Archive\"\nmv \"$ROOT_DIR/Venues/Venue_1\" \"$ROOT_DIR/Archive\"\nmv \"$ROOT_DIR/Venues/Venue_2\" \"$ROOT_DIR/Archive\"\nmv \"$ROOT_DIR/Venues/Venue_3\" \"$ROOT_DIR/Archive\""

"prompt": "Copy the maps for each venue to its folder alongside the Transportation folder",
"shell_script": "cp \"$ROOT_DIR/Transportation/Venue_Maps/Venue_1_Map.pdf\" \"$ROOT_DIR/Venue_1/\"\ncp \"$ROOT_DIR/Transportation/Venue_Maps/Venue_2_Map.pdf\" \"$ROOT_DIR/Venue_2/\""

"prompt": "Locate the Q4 tax filings for Client B from 2024 and move them to a 'Finalized Tax Filings' folder.",
"shell_script": "mkdir -p \"$ROOT_DIR/clients/client_B/Finalized Tax Fillings\"\nmv \"$ROOT_DIR/clients/client_B/2024/tax/Q4/tax_filing.pdf\" \"$ROOT_DIR/clients/client_B/Finalized Tax Fillings/\""

"prompt": "Please find and delete the old payroll templates that are no longer in use.",
"shell_script": "rm \"$ROOT_DIR/archive/templates/old_payroll_template.xlsx\""

"prompt": "Can you identify and delete any invoice templates marked as 'basic' in the templates folder?",
"shell_script": "rm \"$ROOT_DIR/templates/invoice_templates/basic_invoice_template.docx\""

{format_instructions}
"""

GIT_COMMANDS = """
git config --global user.email "test@test.com"
git config --global user.name "Test Test"
git -C "$root_dir" init
git -C "$root_dir" add -A
git -C "$root_dir" commit -m "initial commit"

"""


class FileStructure(BaseModel):
    file_structure: str = Field(description="The string of tree like file structure.")


class ShellScript(BaseModel):
    shell_script: str = Field(
        description="The full contents of the shell script which can create the given file structure.")


class Prompt(BaseModel):
    prompt: str = Field(description="The generated prompt for the tool.")
    shell_script: str = Field(description="Shell script which does what the prompt is asking for.")


class Prompts(BaseModel):
    prompts: List[Prompt] = Field(description="The list of prompts and their scripts.")


def save_expected_tree(tree: str, field: str):
    field = field.replace(' ', '_')
    directory = '.setups'

    with open(f'{directory}/expected_tree_{field.lower()}.txt', 'w') as f:
        f.write(tree)


def save_setup(script: str, field: str):
    field = field.replace(' ', '_')
    directory = '.setups'
    with open(f'{directory}/setup_{field.lower()}.sh', 'w') as f:
        f.write(script)


def save_prompts(prompts: List[Prompt], field: str):
    field = field.replace(' ', '_')
    root_dir = '.'
    gt_dir = f'{root_dir}/ground_truths'
    env_setup_dir = f'{root_dir}/setups'
    prompt_dir = f'{root_dir}/prompts/{field.lower()}'

    if not os.path.exists(f'{gt_dir}/setup_{field.lower()}'):
        os.mkdir(f'{gt_dir}/setup_{field.lower()}')
    if not os.path.exists(f'{prompt_dir}'):
        os.mkdir(f'{prompt_dir}')

    # Read normal script:
    with open(f'{env_setup_dir}/setup_{field.lower()}.sh', 'r') as f:
        setup_script = f.read()

    for i, prompt in enumerate(prompts):
        with open(f'{gt_dir}/setup_{field.lower()}/prompt{i}_gt.sh', 'w') as f:
            setup_script += '\n\n' + f"# Prompt for script:\n" + f"# {prompt.prompt}\n\n" + prompt.shell_script + '\n' + GIT_COMMANDS
            f.write(setup_script)
        with open(f'{prompt_dir}/prompt{i}.txt', 'w') as f:
            f.write(prompt.prompt)


def main():
    llm = init_model('gpt-4')

    fs_parser = PydanticOutputParser(pydantic_object=FileStructure)
    fs_prompt = PromptTemplate(template=GENERATE_FILE_STRUCTURE, input_variables=['field'],
                               partial_variables={"format_instructions": fs_parser.get_format_instructions()})
    file_struct_chain = fs_prompt | llm | fs_parser

    sh_sc_parser = PydanticOutputParser(pydantic_object=ShellScript)
    sh_sc_prompt = PromptTemplate(template=GENERATE_FILE_STRUCTURE_BASH, input_variables=['file_structure'],
                                  partial_variables={"format_instructions": sh_sc_parser.get_format_instructions()})
    shell_script_chain = sh_sc_prompt | llm | sh_sc_parser

    prompts_parser = PydanticOutputParser(pydantic_object=Prompts)
    prompts_prompt = PromptTemplate(template=GENERATE_PROMPTS_AND_SCRIPTS,
                                    input_variables=['file_structure', 'agent_tool'],
                                    partial_variables={"format_instructions": prompts_parser.get_format_instructions()})
    prompts_chain = prompts_prompt | llm | prompts_parser

    # Dry run:
    for field in tqdm(FIELDS, desc='Generating environments for fields.'):
        try:
            fs = file_struct_chain.invoke({'field': field})

            ss = shell_script_chain.invoke({'file_structure': fs.file_structure})

            prompts = prompts_chain.invoke({'file_structure': fs.file_structure,
                                            'agent_tool': 'Tool which can execute bash commands in the terminal.'})
            save_expected_tree(fs.file_structure, field)
            save_setup(ss.shell_script, field)
            save_prompts(prompts.prompts, field)
        except Exception as e:
            print(f"Error for field: {field}")
            print(e)


if __name__ == '__main__':
    main()
