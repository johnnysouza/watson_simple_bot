import json
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('GJkISmm-EazZHlgpmlrarOLrSNzXJThxuQjk96LDAErr')
assistant = AssistantV1(
   version='2020-04-01',
   authenticator = authenticator
)

assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com/instances/ed413263-400f-438c-80d2-6091bbbfd889')

response=assistant.list_all_logs(
   filter='language::pt-br,workspace_id::df288b32-1c13-4546-a9b2-d335d1d3a87b'
).get_result()
    
with open('output.json', 'w', encoding='UTF-8') as output:
   json.dump(response, output, indent=2)