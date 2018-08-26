from examples.car_differ.remove_passenger import RemovePassengerDiff

from diff_and_patch.patch.patch_item import PatchItem


class RemovePassengerPatch(PatchItem):

    @classmethod
    def diff_class(cls):
        return RemovePassengerDiff

    def apply(self):
        # do some thing
        # service.remove_passenger(self.delta.lhs)
        pass
