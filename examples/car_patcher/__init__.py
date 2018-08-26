from diff_and_patch.patch.patcher import Patcher


class CarPatcher(Patcher):

    patches = [GstinPatch,
               SoftBlockPatch,
               GuestDetailsPatch,
               ]