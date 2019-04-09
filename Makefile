PACKAGE_ROOT=src/knot_cloud_websocket
TEST_ROOT=tests
DOCS_ROOT=docs

TEST=pytest
LINT=pylint
APIDOC=sphinx-apidoc

test:
	$(TEST) $(TEST_ROOT)
lint:
	$(LINT) $(PACKAGE_ROOT)
api-doc:
	$(APIDOC) -f -o $(DOCS_ROOT)/source $(PACKAGE_ROOT)
