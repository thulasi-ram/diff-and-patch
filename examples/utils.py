# -*- coding: utf-8 -*-


class Container(object):
    """
    Container for list of guests and a dict at the same time.
    Provides a convenience method to access all objects inside by id/set item by id as well.

    Eg:
    >>> class Guests(Container): pass
    >>> class Guest(object): pass
    >>> guest1 = Guest('G1', 'John', 'john@gmail.com', '122345678')
    >>> guest2 = Guest('G2', 'Doe', 'doe@gmail.com', '122345678')
    >>> _guests = [guest1, guest2]
    >>> guests = Guests(guests=_guests)
    >>> guests['G123'] == guest1 # evaluates True
    """

    def __init__(self, items):
        self.items = frozenset(items)
        self.item_map = {item.uid: item for item in self.items}

    def __getitem__(self, item_id):
        return self.item_map[item_id]

    def __setitem__(self, item_id, item):
        self.items = frozenset(list(self.items).append(item))
        self.item_map[item_id] = item

    def __iter__(self):
        return iter(self.items)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return hash(self) == hash(other)
        return NotImplemented

    def __ne__(self, other):
        equivalent = self.__eq__(other)
        if equivalent is not NotImplemented:
            return not equivalent
        return NotImplemented

    def __hash__(self):
        return hash(self.items)

    def __len__(self):
        return len(self.items)

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            other_item_ids = [item.uid for item in other.items]
            return [item for item in self.items if item.uid not in other_item_ids]
        return NotImplemented

    def intersection(self, other):
        if isinstance(other, self.__class__):
            other_item_ids = [item.uid for item in other.items]
            return [item for item in self.items if item.uid in other_item_ids]
        raise RuntimeError("Intersection is supported only for {kls} objects".format(kls=self.__class__.__name__))

    def __repr__(self):
        return '<{kls} ({rs})>'.format(kls=self.__class__.__name__,
                                       rs=self.items,
                                       )

    def __str__(self):
        return self.__repr__()
