DATASET_PATH := data/dataset.csv

init:
	pip3 install -r requirements.txt

collect:
	mkdir -p data
	wget -O $(DATASET_PATH) https://raw.githubusercontent.com/digital-land/brownfield-land-collection/main/dataset/brownfield-land.csv

render:
	digital-land --pipeline-name brownfield-land render --dataset-path $(DATASET_PATH)

local:
	digital-land --pipeline-name brownfield-land render --dataset-path $(DATASET_PATH) --local

build: clean collect render

clean:
	rm -r ./docs/
	mkdir docs
