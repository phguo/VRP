publish:
	pip install twine
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -rf dist
