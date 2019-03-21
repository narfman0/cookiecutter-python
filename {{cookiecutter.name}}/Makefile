default: test

clean: clean-build clean-pyc

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

init:
	pipenv install

init-dev:
	pipenv install -d

run-test:
	pipenv run pytest --flake8 --black --cov={{ cookiecutter.package }} --cov-report term-missing tests/

release: clean ## package and upload a release
	pipenv run python setup.py sdist bdist_wheel
	pipenv run twine upload

t: run-test
test: init-dev t
