import random
import mlflow
from src.tracking import tracked_run

with tracked_run("dummy-check", params={"model": "none", "seed": 0}, tags={"stage": "setup"}):
    mlflow.log_metric("fake_accuracy", random.random())