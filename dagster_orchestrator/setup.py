from setuptools import find_packages, setup

setup(
    name="dagster_orchestrator",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "dagster_orchestrator": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-core<1.10",
        "dbt-bigquery<1.10",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)