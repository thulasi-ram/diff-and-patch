from diff_and_patch.delta import Delta
from diff_and_patch.diff.diff_item import DiffItem


class ChangeEngineDiff(DiffItem):

    def deltas(self):
        return Delta(self,
                     self.lhs.engine,
                     self.rhs.engine,
                     )
