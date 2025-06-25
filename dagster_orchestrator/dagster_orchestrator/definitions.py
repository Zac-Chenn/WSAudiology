import dagster as dg
from dagster import Definitions
from dagster_dbt import DbtCliResource

from dagster_orchestrator.assets import airbyte, dbt

from dagster_orchestrator.schedules import schedules
from dagster_orchestrator.resources import dbt_core_project

airbyte_assets = dg.load_assets_from_modules([airbyte])
dbt_assets = dg.load_assets_from_modules([dbt])

defs = Definitions(
    assets=[*dbt_assets, *airbyte_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=dbt_core_project),
    },
)
