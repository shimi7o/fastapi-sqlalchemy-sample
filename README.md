# fastapi-sqlalchemy-sample

## セットアップ

```shell
cd app
pip install -r requirements.txt
cd db
alembic upgrade head
```

## サーバー起動

```shell
uvicorn main:app --reload --port 81
```