import spirecloudword
from spirecloudword import *

appId = "your id"
appKey = "your key"
baseUrl = "https://api.e-iceblue.cn"
configuration = Configuration(appId, appKey, baseUrl)
api = spirecloudword.api.fields_api.FieldsApi(configuration)

file_name = "Template.docx"
paragraph_path = "sections/0/paragraphs/0"
filed_code = "EQ 3/f(3,4)"
extra_add = {
    'folder': 'input',
    'index_in_paragraph': 0,
    'dest_file_path': 'output/AddField_EQ.docx'}
api.add_field(file_name, paragraph_path, filed_code, **extra_add)






