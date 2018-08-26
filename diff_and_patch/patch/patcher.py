import logging

from diff_and_patch.exceptions import PartialSuccess
from diff_and_patch.patch.patch_item import PatchItem
from diff_and_patch.utils import fully_qualified_name

logger = logging.getLogger(__name__)


class Patcher(object):
    patches = []

    def __init__(self):
        self._diff_patch_registry = {}
        self._patch_items = []
        self.patched_items = []
        self._deltas = []

        for patch in self.patches:
            assert issubclass(patch, PatchItem)
            diff_class_name = fully_qualified_name(patch.diff_class())
            self._diff_patch_registry[diff_class_name] = patch
            self._patch_items.append(patch)

    def patch(self, deltas):
        self._deltas = deltas

        for delta in self._deltas:
            diff_class_name = fully_qualified_name(delta.diff_item)
            try:
                patch = self._diff_patch_registry[diff_class_name]
            except KeyError:
                raise ValueError('No patch registered for {c}'.format(c=diff_class_name))
            patch = patch(self, delta)
            self.apply(patch)

    def apply(self, patch):
        def pretty_string(items):
            return '\n'.join(['{}. {}'.format(i[0], str(i[1])) for i in enumerate(items, 1)])

        try:
            logger.info("Applying {p}".format(p=patch))
            patch.apply()
            self.patched_items.append(patch.delta)
        except Exception as e:
            err_msg = 'Error applying {p} due to {e}'.format(p=patch, e=e.message)
            logger.exception(err_msg)
            if self.patched_items:
                raise PartialSuccess(err_msg, successes=self.patched_items, errors=self.pending_items)
            raise
        finally:
            logger.info("*" * 50)
            logger.info("Items patched:\n{i}\n".format(i=pretty_string(self.patched_items) or None))
            logger.info("Items pending:\n{p}\n".format(p=pretty_string(self.pending_items) or None))
            logger.info("*" * 50)

    @property
    def pending_items(self):
        return [item for item in self._deltas if item not in self.patched_items]

    def __repr__(self):
        return "{kls}: ({p})".format(kls=self.__class__.__name__,
                                     p=",".join([str(i) for i in self._patch_items]))

    def __str__(self):
        return str(self.__class__.__name__)
