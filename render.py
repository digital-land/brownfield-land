#!/usr/bin/env python3

import sys
import csv
from collections import OrderedDict

from digital_land_frontend.jinja import setup_jinja
from digital_land_frontend.render import render
from digital_land_frontend.jinja_filters.organisation_mapper import OrganisationMapper

docs = "docs"
dataset_csv = "data/dataset.csv"
data_type = "brownfield land"

organisation_mapper = OrganisationMapper()

env = setup_jinja()
env.globals["urlRoot"] = "/brownfield-land/"

index_template = env.get_template("index.html")
row_template = env.get_template("row.html")

ids = set()

translations = str.maketrans({"/": "-", " ": "", "(": "", ")": "", "'": ""})


def get_id(row, idx):
    id = row["site"].translate(translations)
    if not row["site"] or row["site"] in ids:
        id = f"{row['resource']}:{idx}"
    ids.add(id)
    return id


def by_organisation(rows):
    by_organisation = {}
    by_organisation.setdefault(
        "no-organisation", {"name": "No organisation", "rows": []}
    )
    for row in rows:
        if row["organisation"]:
            o = {
                "name": organisation_mapper.get_by_key(row["organisation"]),
                "rows": [],
            }
            by_organisation.setdefault(row["organisation"], o)
            by_organisation[row["organisation"]]["rows"].append(row)
        else:
            by_organisation["no-organisation"]["rows"].append(row)

    result = OrderedDict(sorted(by_organisation.items(), key=lambda x: x[1]["name"]))
    result.move_to_end("no-organisation")
    return result


def render_pages():
    failing = []
    rows = []
    for idx, row in enumerate(csv.DictReader(open(dataset_csv)), start=1):
        row["id"] = get_id(row, idx)

        try:
            render(
                f"{row['id']}/index.html", row_template, row=row, data_type=data_type
            )
            rows.append(row)
        except Exception as e:
            failing.append((row["organisation"], idx, e))

    index = {
        "count": len(rows),
        "organisation": by_organisation(rows),
    }

    render("index.html", index_template, index=index, data_type=data_type)
    print(failing)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--local":
        env.globals["urlRoot"] = "/"

    render_pages()