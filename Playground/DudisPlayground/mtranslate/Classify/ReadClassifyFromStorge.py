# Imports the Google Cloud client library
from google.cloud import storage
key = 'AIzaSyCEi5n57fVrP-WKQOu6p5L0_Dj3QLgwp1g'
from oauth2client.client import GoogleCredentials
#credentials = GoogleCredentials.get_application_default()

#GOOGLE_APPLICATION_CREDENTIALS = "C:\Users\dudia\Desktop\FinalProject\TCBProject-b48d2e8a3caf.json"

def ReadClassifyFromStorge(company_name):
    # Instantiates a client
    comp_name = company_name
    storage_client = storage.Client('tcbproject-164714')
    bucket = storage_client.get_bucket("tcb_bucket")
    blob_class = bucket.get_blob("classify_"+comp_name)
    blob_classdata = blob_class.download_as_string(client=None)
    blob_vector = bucket.get_blob("vector_"+comp_name)
    blob_vectordata = blob_vector.download_as_string(client=None)
    blob_count = bucket.get_blob("count_"+comp_name)
    blob_countdata = blob_count.download_as_string(client=None)
    dict = {'classify': blob_classdata,'vector': blob_vectordata,'count': blob_countdata}
    return dict