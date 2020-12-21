DATASET=brownfield-land

include makerules/makerules.mk
include makerules/render.mk

collect::
	mkdir -p $(DATASET_DIR)
	curl 'https://raw.githubusercontent.com/digital-land/$(DATASET)-collection/main/dataset/$(DATASET).csv' > $(DATASET_PATH)

# TBD: remove this rule
# -- templates should have relative links to ensure we are testing deployed pages locally
local::
	@rm -rf $(DOCS_DIR)
	@mkdir $(DOCS_DIR)
	digital-land --pipeline-name $(DATASET) render --dataset-path $(DATASET_PATH) --local
