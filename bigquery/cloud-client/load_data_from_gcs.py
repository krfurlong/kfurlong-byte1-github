#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Loads data into BigQuery from an object in Google Cloud Storage.

For more information, see the README.rst.

Example invocation:
    $ python load_data_from_gcs.py example_dataset example_table \\
        gs://example-bucket/example-data.csv

The dataset and table should already exist.
"""

import argparse

from google.cloud import bigquery


def load_data_from_gcs(dataset_id, table_id, source):
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    job = bigquery_client.load_table_from_uri(source, table_ref)

    job.result()  # Waits for job to complete

    print('Loaded {} rows into {}:{}.'.format(
        job.output_rows, dataset_id, table_id))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('dataset_id')
    parser.add_argument('table_id')
    parser.add_argument(
        'source', help='The Google Cloud Storage object to load. Must be in '
        'the format gs://bucket_name/object_name')

    args = parser.parse_args()

    load_data_from_gcs(
        args.dataset_id,
        args.table_id,
        args.source)
