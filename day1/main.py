"""Main file for solving the puzzle for day 1"""
from pathlib import Path


class Calibration:

    def __init__(self, calibration_string: str):
        self.calibration_string = calibration_string
        self.calibration_value = self._set_calibration_value()

    def _set_calibration_value(self):
        print(self.calibration_string)
        return 1


class Calibrator:

    def __init__(self):
        self.memory: list[Calibration] = []

    def read_input(self, input:list[str]):
        print(input)
        pass

    def read_input_file(self, file_path:Path):
        pass

    def get_total_calibrate_value(self):
        pass

