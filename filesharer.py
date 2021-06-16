from filestack import Client
import xml.etree.ElementTree as et


class FileSharer:
    # Get the api key
    credentials = et.parse('credentials.xml').getroot()
    apiKey = credentials[0].text

    def __init__(self, filepath, api_key=apiKey):
        self.api_key = api_key
        self.filepath = filepath

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return  new_filelink.url

