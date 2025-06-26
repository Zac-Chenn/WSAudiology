import dagster as dg

airbyte_assets = dg.AssetSelection.assets(["airbyte_assets"])
dbt_assets = dg.AssetSelection.assets(["dbt_core_dbt_assets"])

extract_load = dg.define_asset_job(
    name = "extract_load",
    selection = airbyte_assets
)

transform = dg.define_asset_job(
    name = "transform",
    selection = dbt_assets
)