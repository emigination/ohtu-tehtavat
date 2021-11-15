from urllib import request
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed_content = toml.loads(content)['tool']['poetry']
        name = parsed_content['name']
        descr = parsed_content['description']
        dep = parsed_content['dependencies']
        dev_dep = parsed_content['dev-dependencies']
        return Project(name, descr, dep, dev_dep)
