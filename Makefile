include makerules/makerules.mk
include makerules/render.mk

DATASET_PATH := data/dataset.csv
DATASET := brownfield-land

collect:
	mkdir -p data
	wget -O $(DATASET_PATH) https://raw.githubusercontent.com/digital-land/$(DATASET)-collection/main/dataset/$(DATASET).csv

local: clean
	digital-land --pipeline-name $(DATASET) render --dataset-path $(DATASET_PATH) --local

build: clean collect render

clean::
	rm -rf ./docs/
	mkdir docs
