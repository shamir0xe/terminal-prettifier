from __future__ import annotations
import enum
import os.path
import os
from ..libs.PythonLibrary.buffer_io import FileReader
from ..libs.PythonLibrary.files import File
from ..libs.PythonLibrary.enums import Errors
from ..libs.PythonLibrary.utils import debug_text
from .colors import Colors
from .string_types import StringTypes


MAX_DEPTH = 3
class PrettifierConfig:
    class ConfigTypes(enum.Enum):
        SwitcherConfig = 'SC'
        SpecialName = 'SN'

    def __init__(self):
        self \
            .__initialize() \
            .__read_file() \
            .__retrieve_config()

    def __initialize(self) -> PrettifierConfig:
        self.__switcher = {}
        self.__special_names = {}
        self.f = None
        return self

    def __read_file(self) -> PrettifierConfig:
        base_dir = os.path.dirname(os.path.realpath('__file__'))
        file_name = ''
        depth = 0
        while not File.is_file(file_name) and depth < MAX_DEPTH:
            file_name = os.path.join(base_dir, '.prettifier_cfg')
            base_dir = os.path.join(base_dir, '..')
            depth += 1
        if depth >= MAX_DEPTH:
            raise Exception(Errors.FileNotFound)
        self.f = FileReader(file_name)
        return self

    def __retrieve_config(self) -> None:
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

