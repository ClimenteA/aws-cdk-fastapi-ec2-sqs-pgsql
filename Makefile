run:
	python main.py

migrate:
	python migrate.py

drop-sqlite:
	rm -rf migrations
	rm alembic.ini
	rm database.sqlite