from dataclasses import dataclass

@dataclass
class Config:
    project_name: str = "EEG-Quantum-Net"
    data_dir: str = "data"
    artifacts_dir: str = "artifacts"
    models_dir: str = "artifacts/models"
    figures_dir: str = "artifacts/figures"
    reports_dir: str = "artifacts/reports"

cfg = Config()