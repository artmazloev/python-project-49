install:
	uv sync

brain-games:
	uv run brain-games

package-install:
	uv tool install --reinstall dist/*.whl

make lint:
	uv run ruff check brain_games
