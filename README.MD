# LangGraph Expense tracker

## Summary

Small project exploring the possibilitys of LangGraph.
It lets you sent pictures of invoices, it structures and categorize the expenses and puts them in a database. 


## Project structure

```shell
.
├── LICENCE.txt
├── README.MD
├── config.yaml
├── data
│   └── walmart-bon.jpeg
├── documents
│   ├── api_documentation.png
│   ├── langgraph.png
│   ├── openapi.json
│   └── pg_admin_screenshot.png
├── env.example
├── requirements.txt
└── src
    ├── api
    │   ├── __init__.py
    │   ├── category_routes.py
    │   ├── expenses_routes.py
    │   ├── payment_methods_routes.py
    │   └── run_api.py
    ├── chain
    │   ├── __init__.py
    │   ├── graphstate.py
    │   ├── helpers
    │   │   ├── __init__.py
    │   │   └── get_payment_methods_and_categories.py
    │   └── nodes
    │       ├── __init__.py
    │       ├── categorizer.py
    │       ├── correct.py
    │       ├── db_entry.py
    │       ├── humancheck.py
    │       ├── imageencoder.py
    │       └── jsonparser.py
    └── database
        ├── __init__.py
        ├── create_categories_and_payment_methods.py
        ├── create_tables.py
        └── db_connection.py

9 directories, 30 files
```
