from bbb.models.genus import Genus
from bbb.models.species import Species
from bbb.models.flora import Flora
from .test_db_fixtures import one_plant

def test_add_plant():
    g1 = Genus(name='Greenus')
    s1 = Species(name='plantus')
    p1 = Flora(genus=g1,species=s1)
    g1.plants.append(p1)
    assert p1.genus.name == 'Greenus'
    assert p1.species.name == 'plantus'
    assert len(g1.plants) == 1

def test_description():
    p1 = Flora(desc='SCF')
    assert p1.desc == 'SCF'

def test_germination_code():
    p1 = Flora(germination_code='wet')
    assert p1.germination_code == 'wet'

def test_plant_fixture(one_plant):
    assert 'Greenus' in one_plant.genus.name
    assert 'plantus' in one_plant.species.name
    assert 'Greenus plantus' in one_plant.name