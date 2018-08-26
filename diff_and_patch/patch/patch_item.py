import abc

from diff_and_patch.delta import Delta


class PatchItem(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, patcher, delta, **kwargs):
        self.patcher = patcher
        assert isinstance(delta, Delta)
        self.delta = delta
        self.kwargs = kwargs

    @classmethod
    @abc.abstractmethod
    def diff_class(cls):
        pass

    @abc.abstractmethod
    def apply(self):
        pass

    def __repr__(self):
        return "{p}: {c} -> {n}".format(p=self.__class__.__name__,
                                        c=self.delta.current_state,
                                        n=self.delta.new_state,
                                        )

    def __str__(self):
        return self.__repr__()
