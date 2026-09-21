package := 'dj_sentry'

install:
    uv sync --group dev

update:
    uv sync --all-groups

upgrade:
    uv sync --all-groups --upgrade

lint:
    uv run ruff check .

fmt:
    uv run ruff check --fix .
    uv run ruff format dj_sentry

release major_minor_patch: && changelog
    uv version --bump {{major_minor_patch}}

changelog:
    uv run python scripts/write_changelog.py
    cat CHANGELOG.md >> CHANGELOG.md.new
    rm CHANGELOG.md
    mv CHANGELOG.md.new CHANGELOG.md
    $EDITOR CHANGELOG.md

publish:
    git commit -am "Release $(uv version --short --color=never)"
    git push
    git tag "v$(uv version --short --color=never)"
    git push origin "v$(uv version --short --color=never)"
