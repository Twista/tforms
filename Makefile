VENV_BIN ?= venv/bin/activate

# run tests
tests::
	. $(VENV_BIN); \
	py.test tests
	
install_dev: install
	. $(VENV_BIN); \
	pip install -r requirements_dev.txt

install::
	pip install requirements.txt
