runserver:
	python school_budget_ui/app.py
dump_dependencies:
	pipenv run pip freeze > requirements.txt