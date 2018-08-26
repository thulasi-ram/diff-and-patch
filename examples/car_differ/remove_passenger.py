from diff_and_patch.delta import Delta
from diff_and_patch.diff.diff_item import DiffItem


class RemovePassengerDiff(DiffItem):

    def deltas(self):
        removed_passengers = self.rhs.passengers - self.lhs.passengers
        return [Delta(self,
                      passenger,
                      None,
                      ) for passenger in removed_passengers
                ]
