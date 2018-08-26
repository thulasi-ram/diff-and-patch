class Delta(object):

    def __init__(self, diff_item, current_state, new_state, **kwargs):
        self.diff_item = diff_item
        self.current_state = current_state
        self.new_state = new_state
        self.kwargs = kwargs

    def __repr__(self):
        return "{kls} ({s})".format(kls=self.__class__.__name__,
                                    s=self.__str__()
                                    )

    def __str__(self):
        return "{d}({c} -> {n})".format(d=str(self.diff_item).replace('Diff', ''),
                                        c=self.current_state,
                                        n=self.new_state,
                                        )
