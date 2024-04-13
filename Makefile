SCRIPT_PATH = ./scripts

setup:
	@echo "Setting up environment"
	@$(SCRIPT_PATH)/setup.sh

lint:
	@echo "Running lint"
	@$(SCRIPT_PATH)/lint.sh

format:
	@echo "Running format"
	@$(SCRIPT_PATH)/format.sh

unit_test:
	@echo "Running unit tests"
	@$(SCRIPT_PATH)/coverage-report.sh

