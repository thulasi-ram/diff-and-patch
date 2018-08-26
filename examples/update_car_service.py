# -*- coding: utf-8 -*-
import logging

from examples.car_differ import CarDiffer
from examples.car_patcher import CarPatcher

from diff_and_patch.validator import Validator

logger = logging.getLogger(__name__)


class UpdateCarService(object):

    def __init__(self, car, **kwargs):
        self.car = car
        self.kwargs = kwargs

    def update(self, new_car):
        old_car = self.car

        differ = CarDiffer(old_car=old_car, new_car=new_car)
        patcher = CarPatcher(current_car=old_car, new_car=new_car)

        deltas = differ.diff()

        Validator.validate_all(deltas)
        patcher.patch(deltas)
