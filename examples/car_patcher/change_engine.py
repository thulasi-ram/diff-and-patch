from examples.car_differ.change_engine import ChangeEngineDiff

from diff_and_patch.diff.diff_item import DiffItem


class ChangeEnginePatch(DiffItem):

    @classmethod
    def diff_class(cls):
        return ChangeEngineDiff

    def apply(self):
        # do some thing
        # service.change_passenger(self.delta.rhs)
        pass
