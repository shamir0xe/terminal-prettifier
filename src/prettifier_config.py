import enum
import os.path
import os
from ..libs.PythonLibrary.buffer_io import FileReader
from ..libs.PythonLibrary.files import File
from ..libs.PythonLibrary.enums import Errors
from ..libs.PythonLibrary.utils import debug_text
from .colors import Colors
from .string_types import StringTypes



class PrettifierConfig:
    class ConfigTypes(enum.Enum):
        SwitcherConfig = 'SC'
        SpecialName = 'SN'

    def __init__(self, file_name=None):
        if file_name is None:
            file_name = os.path.join(os.path.dirname(os.path.realpath('__file__')), '.prettifier_cfg')
        # print('file: {}'.format(file_name))
        if not File.is_file(file_name):
            raise Exception(Errors.FileNotFound)
        self.f = FileReader(file_name)
        self.__switcher = {}
        self.__special_names = {}
        self.__retrieve_config()

    def __retrieve_config(self):
        color_values = set(color for color in Colors)
        while not self.f.end_of_buffer():
            f = self.f
            cf_type, key, value = f.read(), f.read(), f.read()
            if cf_type == PrettifierConfig.ConfigTypes.SwitcherConfig.value:
                self.__switcher[StringTypes[key]] = Colors[value]
            elif cf_type == PrettifierConfig.ConfigTypes.SpecialName.value:
                self.__special_names[key.lower(
                )] = Colors[value] if value in color_values else value
            else:
                debug_text('Bad Config File: [%, %, %]', cf_type, key, value)

    def get(self, config_type):
        sw = {
            PrettifierConfig.ConfigTypes.SwitcherConfig: self.__switcher,
            PrettifierConfig.ConfigTypes.SpecialName: self.__special_names
        }
        return sw.get(config_type, 'bad input')
