# Imports the Google Cloud client library
from google.cloud import storage
key = 'AIzaSyCEi5n57fVrP-WKQOu6p5L0_Dj3QLgwp1g'
from oauth2client.client import GoogleCredentials
#credentials = GoogleCredentials.get_application_default()

#GOOGLE_APPLICATION_CREDENTIALS = "C:\Users\dudia\Desktop\FinalProject\TCBProject-b48d2e8a3caf.json"
def WriteClassifyToStorge(name,classify,vector,count):
    comp_name = name
    model = classify
    tfidf = vector
    count_v = count
    # Instantiates a client
    storage_client = storage.Client('tcbproject-164714')
    # Creates the new bucket
    bucket = storage_client.get_bucket("tcb_bucket")
    print bucket
    blob_name = "classify_"+comp_name
    blob = bucket.blob(blob_name,chunk_size=None, encryption_key=None)
    blob.upload_from_string(classify)
    blob_name = "vector_"+comp_name
    blob = bucket.blob(blob_name,chunk_size=None, encryption_key=None)
    blob.upload_from_string(tfidf)
    blob_name = "count_"+comp_name
    blob = bucket.blob(blob_name,chunk_size=None, encryption_key=None)
    blob.upload_from_string(count_v)
