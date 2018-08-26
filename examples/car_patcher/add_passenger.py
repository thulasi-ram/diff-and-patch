from examples.car_differ.add_passenger import AddPassengerDiff

from diff_and_patch.patch.patch_item import PatchItem


class AddPassengerPatch(PatchItem):

    @classmethod
    def diff_class(cls):
        return AddPassengerDiff

    def apply(self):
        # do some thing
        # service.add_passenger(self.delta.rhs)
        pass
