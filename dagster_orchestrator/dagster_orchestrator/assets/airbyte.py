import dagster as dg
import os
from dagster import AssetExecutionContext
from ..resources import airbyte_resource, AIRBYTE_CONNECTION_ID
from dagster_airbyte import load_assets_from_airbyte_instance

airbyte_assets = load_assets_from_airbyte_instance(
    airbyte_resource,
)