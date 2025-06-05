{% macro generate_schema_name(custom_schema_name, node) -%}

    {%- set default_schema = target.schema -%}

    {# 
        This macro overrides the default dbt behavior for schema (dataset) generation.

        By default, dbt concatenates target.schema and custom_schema_name (e.g., 'your_dev_schema_staging').
        This override ensures that if a custom_schema_name is provided (via +schema in dbt_project.yml),
        it is used directly without being prefixed by the target.schema.

        If no custom_schema_name is provided, it falls back to the target.schema from profiles.yml.
    #}

    {%- if custom_schema_name is none -%}
        {{ default_schema }}
    {%- else -%}
        {{ custom_schema_name | trim }}
    {%- endif -%}

{%- endmacro %}