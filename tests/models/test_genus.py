from bbb.models.genus import Genus

def test_add_genus():
    name = 'GenusOne'
    g1 = Genus(name=name)
    assert g1.name == name

def test_plants_list():
    g1 = Genus()
    assert len(g1.plants) == 0
