.DEFAULT_GOAL := check
PYTHON_INTERPRETER = python3
PROJECT_NAME := wellzestahealth-bots

################################################################################
# COMMANDS                                                                     #
################################################################################

setup: check
	@echo "---> Running setup.."
	@conda env create -q -f environment.yml --name $(PROJECT_NAME)
	@echo "---> To complete setup please run \n---> source activate $(PROJECT_NAME)"

install:
	@echo "---> Installing dependencies.."
	@conda env update -q -f environment.yml --name $(PROJECT_NAME)

scheduler:
	@echo "---> Starting cron"
	@python3 src/executors/scheduler.py

clean:
	@echo "---> Cleaning environment.."
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -path '*/tmp/*.pickle' -delete
	find . -path '*/.ipynb_checkpoints/*' -delete
	find . -type d -name ".ipynb_checkpoints" -empty -delete

autocorrect:
	@echo "---> Processing autocorrect"
	@autopep8 --in-place --aggressive --aggressive --global-config .flake8 $(shell find . -name '*.py')

lint:
	@echo "---> Processing lint.."
	@flake8 src

check:
	@echo "---> Checking environment.."
	@python3 check.py

