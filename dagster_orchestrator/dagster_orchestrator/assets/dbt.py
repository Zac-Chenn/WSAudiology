from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets
from ..resources import dbt_core_project

@dbt_assets(
    manifest=dbt_core_project.manifest_path,
)
def dbt_core_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()