import os
from dotenv import load_dotenv
from pathlib import Path

from dagster_airbyte import AirbyteResource
from dagster_dbt import DbtProject

load_dotenv()

# ---------------- Airbyte configs ----------------
AIRBYTE_CONNECTION_ID = os.environ.get("AIRBYTE_CONNECTION_ID", "68be26be-9e14-42d4-9ab4-31f7d7e853ce")

airbyte_host = os.getenv("AIRBYTE_HOST", "localhost")
airbyte_port = os.getenv("AIRBYTE_PORT", "8000")
airbyte_username = os.getenv("AIRBYTE_USERNAME")
airbyte_password = os.getenv("AIRBYTE_PASSWORD")

airbyte_resource = AirbyteResource(
        host=airbyte_host,
        port=airbyte_port,
        # If using basic auth, include username and password:
        username=airbyte_username,
        password=airbyte_password,
)

# ---------------- dbt configs ----------------
dbt_core_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..", "dbt_core").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),

    # add path to dbt profile.yml
    profiles_dir=str(Path(os.path.expanduser("~/.dbt"))),
)
dbt_core_project.prepare_if_dev()