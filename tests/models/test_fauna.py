from bbb.models.genus import Genus
from bbb.models.species import Species
from bbb.models.fauna import Fauna

def test_add_bug():
    g1 = Genus(name='Buzzie')
    s1 = Species(name='beezii')
    b1 = Fauna(genus=g1,species=s1)
    g1.bugs.append(b1)
    assert b1.genus.name == 'Buzzie'
    assert b1.species.name == 'beezii'
    assert len(g1.bugs) == 1