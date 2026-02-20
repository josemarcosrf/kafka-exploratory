.PHONY: app format lint lint-fix clean up

app:
	faststream run app:app

format:
	PYTHONDONTWRITEBYTECODE=1 uv run ruff format .

lint:
	PYTHONDONTWRITEBYTECODE=1 uv run ruff check .

lint-fix:
	PYTHONDONTWRITEBYTECODE=1 uv run ruff check . --fix

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	rm -rf .coverage htmlcov/ .pytest_cache/ dist/ build/ *.egg-info/

up:
	docker compose up -d