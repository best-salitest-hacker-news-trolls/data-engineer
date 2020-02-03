# -*- coding: utf-8 -*-
"""HN Big Query Test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IkqEtbf2Q-WBaUu7Iw0MYRL18jIF7uYN
"""

from google.cloud import bigquery

pip install --upgrade google-cloud-storage

def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)

import os
# have this as a JSON on local machine, will upload to slack
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="HN.json"

client = bigquery.Client()

# loading HN data set
# this method returns a dataset reference, not the dataset
hn_dataset_ref = client.dataset('hacker_news', project='bigquery-public-data')

type(hn_dataset_ref)

# load the real dataset
hn_dset = client.get_dataset(hn_dataset_ref)

type(hn_dset)

[x.table_id for x in client.list_tables(hn_dset)]

hn_full = client.get_table(hn_dset.table('full'))

type(hn_full)

hn_full.schema

schema_subset = [col for col in hn_full.schema if col.name in ('id','by', 'author', 'text')]
results = [x for x in client.list_rows(hn_full, start_index=100, selected_fields=schema_subset, max_results=10)]

for i in results:
    print(dict(i))

import google.cloud.bigquery.magics

google.cloud.bigquery.magics.context.use_bqstorage_api=True

from google.cloud import bigquery_storage_v1beta1

bqstorageclient = bigquery_storage_v1beta1.BigQueryStorageClient()

hn_comments = client.get_table(hn_dset.table('comments'))
hn_comments.schema

query_string = "SELECT Id FROM `bigquery-public-data.hacker_news.comments`"
dataframe = (
    client.query(query_string)
    .result()
    .to_dataframe(bqstorage_client=bqstorageclient)
)
print(dataframe.head())

len(dataframe)

query_string_2 = "SELECT author FROM `bigquery-public-data.hacker_news.comments`"
dataframe_2 = (
    client.query(query_string_2)
    .result()
    .to_dataframe(bqstorage_client=bqstorageclient)
)
print(dataframe_2.head())

len(dataframe_2)

query_string_3 = "SELECT text FROM `bigquery-public-data.hacker_news.comments`"
dataframe_3 = (
    client.query(query_string_3)
    .result()
    .to_dataframe(bqstorage_client=bqstorageclient)
)
print(dataframe_3.head())

