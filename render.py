#!/usr/bin/env python3

import csv

from digital_land_frontend.jinja import setup_jinja
from digital_land_frontend.render import render
from digital_land_frontend.jinja_filters.organisation_mapper import OrganisationMapper

docs = "docs"
dataset_csv = "data/dataset.csv"

env = setup_jinja()
env.globals["urlRoot"] = "/brownfield-land"

index_template = env.get_template("index.html")
row_template = env.get_template("row.html")

ids = set()


def get_id(row, idx):
    id = row["site"]
    if row["site"] is None or row["site"] in ids:
        id = f"{row['resource']}:{idx}"
    ids.add(id)
    return id


for idx, row in enumerate(csv.DictReader(open(dataset_csv)), start=1):
    row["id"] = get_id(row, idx)

    try:
        render(f"{row['site']}/index.html", row_template, row=row)
    except Exception as e:
        print(e)
        print(row["organisation"], idx)
