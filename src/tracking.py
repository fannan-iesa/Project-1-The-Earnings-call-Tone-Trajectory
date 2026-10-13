import subprocess
from contextlib import contextmanager

import mlflow

from src import config


def _git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=config.ROOT, text=True, stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return "unknown"


def init_experiment(name: str = config.EXPERIMENT_NAME) -> None:
    mlflow.set_tracking_uri(config.TRACKING_URI)
    if mlflow.get_experiment_by_name(name) is None:
        config.MLFLOW_ARTIFACTS.mkdir(exist_ok=True)
        mlflow.create_experiment(name, artifact_location=config.MLFLOW_ARTIFACTS.as_uri())
    mlflow.set_experiment(name)


@contextmanager
def tracked_run(run_name: str, params: dict | None = None, tags: dict | None = None):
    init_experiment()
    with mlflow.start_run(run_name=run_name) as run:
        if params:
            mlflow.log_params(params)
        mlflow.set_tags({"git_commit": _git_commit(), **(tags or {})})
        yield run