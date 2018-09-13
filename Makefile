
.PHONY: install_requirements_dev
install_requirements_dev: ## install pip requirements for development
	pip install -r requirements_dev.txt
	pip install -e .

.PHONY: start
start: ## start the server in the dev
	FLASK_APP=app.app.py FLASK_ENV=development flask run --host=0.0.0.0 --port=5000
