## setup

1. clone
```
$ git clone [url]
```

2. backendのリポジトリへ移動
```
$ cd backend
```

3. venvの仮想環境を作成
```
$ python3 -m venv env
```

4. 仮想環境の有効化
```
# Linux, maxOS
$ source ./env/bin/activate

# Windows PowerShell
$ .\env\Scripts\Activate.ps1

# Windows bash
$ source ./env/Scripts/activate
```

5. パッケージインストール
```
$ pip3 install -r requirements.txt
```

6. 起動(仮想環境有効化時)
```
$ uvicorn main:app --reload
```

## commands
```
# 仮想環境の停止
$ deactivate

# requirements.txtの作成
$ pip3 freeze > requirements.txt 

# 一括インストール
$ pip3 install -r requirements.txt

# "backend" コンテナの中で "poetry add sqlalchemy aiomysql" を実行
$ docker-compose exec backend poetry add sqlalchemy aiomysql

# alembicを初期化
$ docker compose exec backend poetry run alembic init migrations
```