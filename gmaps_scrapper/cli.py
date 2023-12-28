# -*- coding: utf-8 -*-

import csv
from typing import Optional


ind = {"most_relevant": 0, "newest": 1, "highest_rating": 2, "lowest_rating": 3}
HEADER = [
    "id_review",
    "caption",
    "relative_date",
    "retrieval_date",
    "rating",
    "username",
    "n_review_user",
    "n_photo_user",
    "url_user",
]
HEADER_W_SOURCE = [
    "id_review",
    "caption",
    "relative_date",
    "retrieval_date",
    "rating",
    "username",
    "n_review_user",
    "n_photo_user",
    "url_user",
    "url_source",
]


def csv_writer(source_field: Optional[str], ind_sort_by: str, path: str = "data/"):
    """Write the result into CSV file.

    Args:
        source_field (Optional[str]): _description_
        ind_sort_by (str): _description_
        path (str, optional): _description_. Defaults to 'data/'.

    Returns:
        _type_: _description_
    """
    outfile = ind_sort_by + "_gm_reviews.csv"
    targetfile = open(path + outfile, mode="w", encoding="utf-8", newline="\n")
    writer = csv.writer(targetfile, quoting=csv.QUOTE_MINIMAL)

    if source_field:
        h = HEADER_W_SOURCE
    else:
        h = HEADER
    writer.writerow(h)

    return writer
