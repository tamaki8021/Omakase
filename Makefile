.PHONY: init migrate upgrade up down build

# alembitの初期化
init:
    docker compose exec backend poetry run alembic init migrations

# マイグレーションファイルを作成する
migrate:
    docker compose exec backend poetry run alembic revision --autogenerate -m "$(m)"

# マイグレーションファイルを実行する
upgrade:
    docker compose exec backend poetry run alembic upgrade head

# dockerのコンテナを立ち上げるコマンド
up:
    docker compose up -d

# dockerのコンテナを終了するコマンド
down:
    docker compose down

# dockerのコンテナをビルドするコマンド
build:
    docker compose build

# dockerのコンテナログを確認するコマンド
logs:
		docker compose logs -f