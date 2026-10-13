from src import config

def test_root_is_project_root():
    assert (config.ROOT / "pyproject.toml").exists()