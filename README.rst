==============
Diff & Patch
==============

A simple python package which serves as a framework for diffing and patching complex objects. Inspired by Shreyas Kulkarni and git diff and patch.

Quick links
===========
    PyPi: `https://pypi.org/project/diff-and-patch/ <https://pypi.org/project/diff-and-patch/>`_


    Source: `https://github.com/thulasi-ram/diff-and-patch <https://github.com/thulasi-ram/diff-and-patch>`_


    Docs: `https://github.com/thulasi-ram/diff-and-patch <https://github.com/thulasi-ram/diff-and-patch>`_

Quick Usage
===========

See `examples <https://github.com/thulasi-ram/diff-and-patch/examples>`_


::

    from examples.car import Car, Engine, Passenger
    from examples.update_car_service import UpdateCarService

    engine = Engine(model='RAWWR')
    John = Passenger('John')
    Doe = Passenger('Doe')
    old_car = Car(
        engine=engine,
        passengers=[John, Doe],
    )

    new_engine = Engine(model='SUPER_RAWWR')
    Anne = Passenger('Anne')
    new_car = Car(
        engine=engine,
        passengers=[John, Doe, Anne],
    )

    UpdateCarService(old_car).update(new_car)
