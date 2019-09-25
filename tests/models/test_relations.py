from bbb import db
from bbb.models.relations import *
from .test_db_fixtures import one_plant, one_bug, one_location

def test_plant_bug_relations(one_plant,one_bug):
    one_plant.bugs.append(one_bug)
    assert len(one_plant.bugs) > 0
    assert len(one_bug.plants) > 0
    assert 'Greenus' in one_bug.plants[0].name
    assert 'Buzzie' in one_plant.bugs[0].name

def test_plant_location_relations(one_plant,one_location):
    one_plant.locations.append(one_location)
    assert 'Greenus' in one_location.plants[0].name
    assert 'Here' in one_plant.locations[0].name

def test_double_relations(one_plant,one_bug):
    one_plant.bugs.append(one_bug)
    one_bug.plants.append(one_plant)
    print(one_bug.plants)
    assert len(one_bug.plants) == 2