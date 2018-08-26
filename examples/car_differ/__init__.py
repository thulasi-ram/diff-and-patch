from examples.car_differ.add_passenger import AddPassengerDiff
from examples.car_differ.change_engine import ChangeEngineDiff
from examples.car_differ.remove_passenger import RemovePassengerDiff

from diff_and_patch.diff.differ import Differ


class CarDiffer(Differ):

    def __init__(self, old_car, new_car):
        self.old_car = old_car
        self.new_car = new_car
        super(CarDiffer, self).__init__(lhs=old_car, rhs=new_car)

    diffs = [
        ChangeEngineDiff,
        AddPassengerDiff,
        RemovePassengerDiff,
    ]
