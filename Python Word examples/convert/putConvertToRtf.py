import spirecloudword
from spirecloudword.configuration import Configuration as WordConfiguration

appId = "your id"
appKey = "your key"

configuration = WordConfiguration(appId, appKey)
api = spirecloudword.api.convert_api.ConvertApi(configuration)
file_name = "Template.docx"
target_format = "rtf"
inputFolder = "input"
outputFilePath = "output/ConvertToRtf.rtf"
result = api.convert_document(file_name, target_format, folder=inputFolder, dest_file_path=outputFilePath)


