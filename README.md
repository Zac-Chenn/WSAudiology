# WSAudiology
![Static Badge](https://img.shields.io/badge/Extract_Load-Airbyte-purple)
![GCP](https://img.shields.io/badge/Cloud-Google_Cloud_Platform-blue)
![GCS](https://img.shields.io/badge/Data_Lake-Google_Cloud_Storage-blue)
![BigQuery](https://img.shields.io/badge/Data_Warehouse-BigQuery-blue)
![dbt](https://img.shields.io/badge/Transform-dbt-orange)
![Airflow](https://img.shields.io/badge/Orchestration-Dagster-yellow)

## Company Overview

WSAudiology (WSA) is a global leader in the hearing aid industry, dedicated to improving the quality of life for millions of people with hearing needs worldwide. Formed in 2019 through the merger of Sivantos Group and Widex, the company brings together over 170 years of combined experience and a rich history of pioneering innovation in hearing care.

## Problem Statement
WSAudiology (WSA) currently utilizes Teamtailor as its Applicant Tracking System (ATS) to manage all recruitment activities. However, the data within Teamtailor lacks sufficient accessibility for direct extraction and analysis by business stakeholders.

This prevents key stakeholders from gaining critical, timely insights into recruitment efficiency, talent pipeline health, and workforce planning, leading to up to 100 hours annually spent on manual data extraction and hindering data-driven talent acquisition decisions.

To address this, the present project aims to establish a robust data pipeline that can efficiently extract and load recruitment data from Teamtailor. This pipeline will transform the raw data into usable, actionable insights, empowering business stakeholders with the necessary information to enhance recruitment effectiveness, strategically build talent pipelines, and proactively support long-term workforce planning.

## Table of Contents
- [WSAudiology](#wsaudiology)
  - [Company Overview](#company-overview)
  - [Problem Statement](#problem-statement)
  - [Table of Contents](#table-of-contents)
  - [Tech Stack](#tech-stack)
  - [Project Architecture](#project-architecture)
  - [Insights \& Visualization](#insights--visualization)
    - [Executive Reporting](#executive-reporting)
    - [Recruitment Efficency](#recruitment-efficency)
    - [Candidate Experience](#candidate-experience)

## Tech Stack
<div style="display: flex; flex-wrap: wrap; gap: 5px;">
<img height="32" width="32" src="https://cdn.simpleicons.org/python" />
<img height="32" width="32" src="https://cdn.simpleicons.org/docker" /> 
<img height="32" width="32" src="https://cdn.simpleicons.org/googlecloud" /> 
<img height="32" width="32" src="https://cdn.simpleicons.org/googlecloudstorage" /> 
<img height="32" width="32" src="https://cdn.simpleicons.org/googlebigquery" /> 
<img height="32" width="32" src="https://cdn.simpleicons.org/terraform" /> 
<img height="32" width="32" src="https://cdn.simpleicons.org/dbt" /> 
<img height="32" width="32" src="https://cdn.prod.website-files.com/605e01bc25f7e19a82e74788/624d9c4a092d197522e0ef75_Airbyte_icon_color.svg" /> 
</div>

---
- **Containerization Platform:** Docker  
  
    Docker provides standardized, consistent environments, simplifying deployment and ensuring consistency between development and production.

- **Cloud Platform:** Google Cloud Platform (GCP)  
   
    GCP offers reliable and scalable infrastructure and services, ideal for data-intensive cloud-native solutions.

- **Infrastructure as Code:** Terraform  
  
    Terraform manages GCP resources programmatically, ensuring repeatable, version-controlled, and consistent infrastructure deployment.

- **Workflow Orchestration:** Dagster 
  
    Dagster orchestrates data pipelines as "software-defined assets," providing clear lineage, observability, and robust data governance for reliable workflows.

- **Data Transformation:** dbt-core
  
    dbt-core enables powerful data transformation and modeling in SQL, ensuring data quality and consistency with modular design and testing.

- **Storage & Warehousing:** Google Cloud Storage (GCS), BigQuery  
  
    GCS provides high-performance data lake storage, while BigQuery offers serverless, cost-effective, petabyte-scale data warehousing with automatic scaling.

- **Visualization:** PowerBI  
  
    PowerBI provides rich data visualization capabilities, directly connecting to BigQuery data sources to create interactive dashboards. 

## Project Architecture
![Project Architecture](images/Tech%20Stack.png)


## Insights & Visualization


### Executive Reporting

![Active Requisitions](images/photo_1_2025-06-25_00-59-36.jpg)

![Active Jobs](images/photo_2_2025-06-25_00-59-36.jpg)

![Hired Candidate](images/photo_3_2025-06-25_00-59-36.jpg)

### Recruitment Efficency
![Time to Hire](images/photo_4_2025-06-25_00-59-36.jpg)

### Candidate Experience
![Candidate Survey](images/photo_5_2025-06-25_00-59-36.jpg)


