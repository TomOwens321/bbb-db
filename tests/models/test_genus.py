from bbb.models.genus import Genus
from .test_db_fixtures import one_genus

def test_add_genus():
    name = 'GenusOne'
    g1 = Genus(name=name)
    assert g1.name == name

def test_description():
    g1 = Genus(desc='SCF')
    assert g1.desc == 'SCF'

def test_plants_list():
    g1 = Genus()
    assert len(g1.plants) == 0

def test_genus_fixture(one_genus):
    assert 'Greenus' in one_genus.name
