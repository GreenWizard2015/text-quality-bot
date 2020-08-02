import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials  

class CGoogleAPI(object):
  def __init__(self, credentialsFile):
    self.CREDENTIALS_FILE = credentialsFile
  
  def discovery(self, service, version, scope):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(self.CREDENTIALS_FILE, scope)
    httpAuth = credentials.authorize(httplib2.Http())    
    return apiclient.discovery.build(service, version, http=httpAuth, cache_discovery=False)
  
  def documents_service(self):
    # todo: Реализовать кеширование (с повторной авторизацией при необходимости)
    return self.discovery(
      'docs', 'v1',
      scope=['https://www.googleapis.com/auth/documents.readonly']
    ).documents()

  def document(self, docId):
    return self.documents_service().get(documentId=docId).execute()