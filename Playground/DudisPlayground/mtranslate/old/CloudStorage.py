# Imports the Google Cloud client library
from google.cloud import storage
from oauth2client.client import GoogleCredentials
#credentials = GoogleCredentials.get_application_default()

#GOOGLE_APPLICATION_CREDENTIALS = "C:\Users\dudia\Desktop\FinalProject\TCBProject-b48d2e8a3caf.json"

key = 'AIzaSyCEi5n57fVrP-WKQOu6p5L0_Dj3QLgwp1g'
# Instantiates a client
storage_client = storage.Client('tcbproject-164714')


# Creates the new bucket
bucket = storage_client.get_bucket("tcb_bucket")

print bucket

blob_name = "test_blob3"

blob = bucket.blob(blob_name,chunk_size=None, encryption_key=None)

blob.upload_from_string("aaa1")


blob = bucket.get_blob("test_blob3")

print blob.download_as_string(client=None)

print "cool"


