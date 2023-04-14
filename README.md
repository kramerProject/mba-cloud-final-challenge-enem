## Description

This a practical activity part of the MBA in Data Engineering from XPE. The job consists in ingesting the
[ENEM_2020](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-
abertos/microdados/enem) microdata in a structure of Data Lake on AWS. After that, use the Spark Operator to, within Kubernetes, convert the data to the parquet format and write the results in another layer of the Data Lake. Finally make the data available for querying in AWS Athena.

## About the source

Created in 1998, the National High School Examination (Enem) aims to assess student performance at the end of basic schooling. Students who are completing or who have completed high school in previous years can participate in the exam. The job collects data about this students.
## What was Done

- [X] Create a Kubernetes cluster to carry out the activities
- [X] Perform Spark Operator installation and configuration
- [X] Use AIRFLOW to orchestrate the jobs
- [X] Create an image for the ingestion and processing jobs
- [X] Use SparkOperator on Kubernetes to transform data into
parquet format and write them in the staging zone or silver zone of your data
lake
- [X] Perform sql querys to extract Data information


## Architecture

![AWS Terraform v1](/img/arq.png)
