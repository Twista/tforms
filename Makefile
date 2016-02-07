VENV_BIN ?= venv/bin/activate

# run tests
tests::
	. $(VENV_BIN); \
	py.test tests --cov=tforms --cov-report term-missing
	
install_dev: install
	. $(VENV_BIN); \
	pip install -r requirements_dev.txt

install::
	pip install requirements.txt
