# ⚽ Projeto Fut-Portf

Pipeline de dados multi-cloud com AWS, Databricks e Power BI usando dados de jogadores de futebol.

## 🔗 Stack utilizada
- **AWS S3**: armazenamento de arquivos `.csv`
- **AWS Glue + Athena**: catalogação e consulta SQL
- **Azure Databricks (Community Edition)**: transformação com PySpark
- **Power BI**: visualização final
- **Python + Boto3**: automação do upload

## 🔍 Objetivo
Construir um pipeline de ponta a ponta para análise de mercado de jogadores por nacionalidade, a partir de dados públicos do Kaggle.

## 📊 Dashboard final
![Dashboard](imgs/dashboard_preview.png)

## 📁 Estrutura
- `notebooks/`: notebook Databricks com transformação PySpark
- `scripts/`: script Python para upload em S3
- `powerbi/`: painel `.pbix`
- `imgs/`: imagem do painel final
