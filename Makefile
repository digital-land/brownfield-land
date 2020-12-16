include makerules/makerules.mk
include makerules/render.mk

DATASET_PATH := data/dataset.csv

collect:
	mkdir -p data
	wget -O $(DATASET_PATH) https://raw.githubusercontent.com/digital-land/brownfield-land-collection/main/dataset/brownfield-land.csv

local: clean
	digital-land --pipeline-name brownfield-land render --dataset-path $(DATASET_PATH) --local

build: clean collect render

clean::
	rm -r ./docs/
	mkdir docs
