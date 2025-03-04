from pydantic import BaseModel


class EvaluateResult(BaseModel):
    success: bool
    prompt: str
    output: str
    env_setup: str
    prompt_file: str
    env_gt_dir: str
    field: str
