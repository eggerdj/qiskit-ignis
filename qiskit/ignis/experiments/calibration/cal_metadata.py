from typing import Union, List, Dict
from dataclasses import dataclass


@dataclass
class CalibrationMetadata:
    """
    CalibrationMetadata defines the structure of the meta data that describes
    calibration experiments. Calibration analysis routines will
    use variables of this class to tie together the results from
    different quantum circuits.
    """

    # The name of the calibration experiment.
    name: str = None

    # Name of the pulse schedule that was used in the calibration experiment.
    pulse_schedule_name: str = None

    # A dictionary of x-values the structure of this dict will
    # depend on the experiment being run.
    x_values: Dict[str, Union[int, float, complex]] = None

    # The series of the Experiment to which the circuit is
    # attached to. E.g. 'X' or 'Y' for Ramsey measurements.
    series: Union[str, int, float] = None

    # ID of the experiment to which this circuit is attached.
    exp_id: str = None

    # Physical qubits used.
    qubits: List[int] = None

    # Mapping of qubit index and classical register index.
    # The key is the qubit index and value is the classical bit index.
    # This mapping is automatically generated at BaseCalibrationExperiment class.
    register_map: Dict[int, int] = None

    def __init__(self,
                 name: str = None,
                 pulse_schedule_name: str = None,
                 x_values: Dict[str, Union[int, float, complex]] = None,
                 series: Union[str, int, float] = None,
                 exp_id: str = None,
                 qubits: List[int] = None,
                 register_map: Dict[Union[str, int], int] = None):
        self.name = name
        self.pulse_schedule_name = pulse_schedule_name
        self.x_values = x_values
        self.series = series
        self.exp_id = exp_id
        self.qubits = qubits

        if register_map:
            self.register_map = {}
            for key, value in register_map.items():
                self.register_map[int(key)] = int(value)

    def to_dict(self) -> dict:
        """Export the meta data to a dict structure."""
        return {
            'name': self.name,
            'series': self.series,
            'x_values': self.x_values,
            'pulse_schedule_name': self.pulse_schedule_name,
            'exp_id': self.exp_id,
            'qubits': self.qubits,
            'register_map': self.register_map
        }
