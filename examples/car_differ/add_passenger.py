from diff_and_patch.delta import Delta
from diff_and_patch.diff.diff_item import DiffItem


class AddPassengerDiff(DiffItem):

    def deltas(self):
        added_passengers = self.lhs.passengers - self.rhs.passengers
        return [Delta(self,
                      None,
                      passenger,
                      ) for passenger in added_passengers
                ]
