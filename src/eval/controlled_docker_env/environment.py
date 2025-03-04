from typing import List
from pydantic import BaseModel
import yaml


class Environment(BaseModel):
    setup_file: str
    prompt_file: str
    ground_truth_directory: str


class Environments(BaseModel):
    environments: List[Environment]

    @classmethod
    def load(cls, file):
        with open(file, "r") as f:
            data = yaml.safe_load(f)
        return cls(**data)
