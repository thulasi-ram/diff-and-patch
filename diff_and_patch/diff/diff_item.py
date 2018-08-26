import abc


class DiffItem(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, differ, **kwargs):
        self.differ = differ
        self.kwargs = kwargs

    @abc.abstractmethod
    def deltas(self):
        pass

    @property
    def lhs(self):
        return self.differ.lhs

    @property
    def rhs(self):
        return self.differ.rhs

    def __repr__(self):
        return "{kls} ({d}, {k})".format(kls=self.__class__.__name__,
                                         d=self.differ,
                                         k=self.kwargs,
                                         )

    def __str__(self):
        return str(self.__class__.__name__)
