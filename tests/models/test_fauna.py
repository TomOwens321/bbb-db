from bbb.models.genus import Genus
from bbb.models.species import Species
from bbb.models.fauna import Fauna
from .test_db_fixtures import one_bug

def test_add_bug():
    g1 = Genus(name='Buzzie')
    s1 = Species(name='beezii')
    b1 = Fauna(genus=g1,species=s1)
    g1.bugs.append(b1)
    s1.bugs.append(b1)
    assert b1.genus.name == 'Buzzie'
    assert b1.species.name == 'beezii'
    assert len(g1.bugs) == 1
    assert len(s1.bugs) == 1

def test_fauna_fixture(one_bug):
    assert 'Buzzie' in one_bug.name
    assert 'beezii' in one_bug.name