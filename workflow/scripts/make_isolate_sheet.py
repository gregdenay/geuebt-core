#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


# if not calling for snakemake rule
try:
    sys.stderr = open(snakemake.log[0], "w")
except NameError:
    pass


import json
from datetime import datetime


def main(validation, calling, charak, pathout):
    with open(validation, "r") as fi:
        vali = json.load(fi)
    with open(calling, "r") as fi:
        call = json.load(fi)
    with open(charak, "r") as fi:
        char = json.load(fi)
    vali["created_at"] = datetime.now().strftime('%Y-%m-%d')
    vali["qc_metrics"]["cgmlst_missing_fraction"] = call["qc_metrics"]["cgmlst_missing_fraction"]
    vali["characterization"] = char["characterization"]
    vali["cgmlst"] = call["cgmlst"]
    with open(pathout, "w") as fi:
        json.dump(vali, fi, indent=4)


if __name__ == '__main__':
    main(
        snakemake.input['validation'],
        snakemake.input['calling'],
        snakemake.input['charak'],
        snakemake.output['isolate_sheet']
    )
