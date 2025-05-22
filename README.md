# ⚽ projeto-fut-portf

Pipeline de dados multi-cloud com AWS, Databricks e Power BI usando dados públicos de jogadores de futebol.  
Este projeto simula um fluxo de engenharia de dados completo, desde a ingestão até a visualização final, com foco em performance, organização e escalabilidade.

---

## 📌 Objetivo

Construir um pipeline de ponta a ponta para análise de mercado de jogadores, organizando e transformando dados públicos em insights visuais de alto impacto.

---

## 🧱 Arquitetura do Pipeline

```mermaid
graph TD
A[Kaggle Dataset (CSV)] --> B[S3 - dados brutos]
B --> C[Glue Crawler]
C --> D[Glue Data Catalog]
D --> E[Athena - consulta SQL]
E --> F[Databricks - transformação PySpark]
F --> G[Exportação .csv]
G --> H[Power BI - visualização final]
