#!/usr/bin/env python3

import argparse
from collections import defaultdict, OrderedDict
import csv
import json
import os
import sys
import re

root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

free_response_fields = [
    "What are you biggest challenges or pain points when using containers, or reasons that you don’t use them?",
    "What can containers not do that you wish they could? What features would you like to see?",
]

multiple_choice_fields = [
    "In what context",
    "What container registries",
]

regex = "(" + "|".join(multiple_choice_fields) + ")"

skips = [
    "Completion time",
    "ID",
    "Timestamp",
    "Start time",
    "Email",
    "Name",
    "What platforms do you actually use? (you knew this was coming!)",
]


# 1 and >50 are fine as is.
date_to_number = {
    "5-Feb": "2-5",
    "10-Jun": "6-10",
    "Nov-50": "11-50",
}


def get_parser():
    parser = argparse.ArgumentParser(description="Prepare csv data file")

    parser.add_argument("input", help="input csv script")
    parser.add_argument(
        "--delim",
        dest="delim",
        help="File separator (defaults to tab for tsv)",
        default=",",
    )
    parser.add_argument(
        "--outdir",
        dest="outdir",
        help="Output directory (defaults to _data, must be relative to scripts folder)",
        default=os.path.join(root, "_data"),
    )
    return parser


def write_json(filename, obj):
    """
    write json to file, with pretty print
    """
    with open(filename, "w") as fd:
        fd.write(json.dumps(obj, indent=4))
    return filename


def read_rows(filepath, newline="", delim="\t"):
    """
    read in the data rows of a csv file.
    """
    with open(filepath, newline=newline) as infile:
        reader = csv.reader(infile, delimiter=delim)
        data = [row for row in reader]
    return data


def validate_rows(rows):
    """
    ensure that rows are defined (not an empty list) and each is equal length
    """
    if not rows:
        sys.exit("The data file is empty.")
    length = len(rows[0])
    if any([len(x) != length for x in rows]):
        sys.exit("All rows must have equal length.")


def rows_to_dict(rows):
    """
    Given a tsv format, convert to dictionary. We could easily do that with
    pandas or similar but I'd rather not add an extra dependency.
    """
    # Header (and keys) are the first row
    header = rows.pop(0)
    print(f"Found a total of {len(header)} questions.")
    data = {}

    for idx, key in enumerate(header):
        # Yes, the data export really has hanging empty spaces. Thanks Microsoft!
        question_type = "single_choice"
        key = key.strip()
        if key in skips:
            continue
        if (
            "check all that apply" in key
            or key in multiple_choice_fields
            or re.search(regex, key)
        ):
            question_type = "multiple_choice"
        elif key in free_response_fields:
            question_type = "free_response"

        # Remove newlines, etc.
        key = key.split("\n")[0]

        # special case multiple choice
        if question_type == "multiple_choice":
            values = []
            for row in rows:
                for entry in row[idx].split(";"):
                    if not entry:
                        continue
                    entry = entry.strip()
                    values = values + [entry]
        else:
            values = [x[idx].strip() for x in rows if x[idx]]
        # Remove any [] from the key
        key = key.replace("[", "").replace("]", "").strip()
        counts = defaultdict(lambda: 0)
        for value in values:
            counts[value] += 1

        # Sort counts, important for likert scales
        counts = dict(OrderedDict(sorted(dict(counts).items())))
        data[key] = {"question_type": question_type}
        if question_type == "free_response":
            data[key]["values"] = values
        else:
            data[key]["counts"] = counts

    return data


def main():
    """
    main entrypoint for generating data output file
    """

    parser = get_parser()

    # If an error occurs while parsing the arguments, the interpreter will exit with value 2
    args, extra = parser.parse_known_args()

    for name in [args.input, args.outdir]:
        if not name or not os.path.exists(name):
            sys.exit(f"{name} does not exist.")

    # Read rows and ensure that all are equal length
    rows = read_rows(args.input, delim=args.delim)
    validate_rows(rows)

    # Organize results by header fields as keys, add counts
    data = rows_to_dict(rows)

    # Output file is same name with json, but not in raw folder
    basename = "%s.json" % os.path.basename(os.path.splitext(args.input)[0])
    filename = os.path.join(args.outdir, basename)
    print("Writing output to %s" % filename)
    write_json(filename, data)


if __name__ == "__main__":
    main()
