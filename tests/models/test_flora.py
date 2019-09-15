from bbb.models.genus import Genus
from bbb.models.species import Species
from bbb.models.flora import Flora

def test_add_plant():
    g1 = Genus(name='Greenus')
    s1 = Species(name='plantus')
    p1 = Flora(genus=g1,species=s1)
    g1.plants.append(p1)
    assert p1.genus.name == 'Greenus'
    assert p1.species.name == 'plantus'
    assert len(g1.plants) == 1