from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"

MLFLOW_DB = ROOT / "mlflow.db"
MLFLOW_ARTIFACTS = ROOT / "mlartifacts"
TRACKING_URI = f"sqlite:///{MLFLOW_DB.as_posix()}"
EXPERIMENT_NAME = "earnings-tone"

load_dotenv(ROOT / ".env")   # reads secrets from .env if it exists