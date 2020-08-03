clean:
	rm -r immutaform/__pycache__
	rm -r tests/__pycache__
	rm -r .pytest_cache

test:
	pytest tests
