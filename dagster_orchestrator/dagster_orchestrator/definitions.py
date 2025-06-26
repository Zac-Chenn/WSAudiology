import dagster as dg
from dagster import Definitions, define_asset_job, ScheduleDefinition
from dagster_dbt import DbtCliResource

from dagster_orchestrator.assets import airbyte, dbt
from dagster_orchestrator.jobs import extract_load, transform
from dagster_orchestrator.schedules import schedules
from dagster_orchestrator.resources import dbt_core_project

# ------------------ define assets ------------------
airbyte_assets = dg.load_assets_from_modules([airbyte])
dbt_assets = dg.load_assets_from_modules([dbt])

# ------------------ define jobs ------------------
all_jobs = [extract_load, transform]

defs = Definitions(
    assets = [*dbt_assets, *airbyte_assets],
    schedules=[
        ScheduleDefinition(
          job= define_asset_job("all_assets", selection="*"),
          cron_schedule='@daily'
        )],
    resources = {
        "dbt": DbtCliResource(project_dir=dbt_core_project),
    },
)
