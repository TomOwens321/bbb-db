import pytest
from bbb.models.genus import Genus
from bbb.models.species import Species
from bbb.models.flora import Flora
from bbb.models.fauna import Fauna
from bbb.models.location import Location
from bbb.models.seed import Seed

"""
Create a set of models that other tests may use.
"""
@pytest.fixture
def one_genus():
    """
    Create a Genus object
    """
    return Genus(name='Greenus')

@pytest.fixture
def one_species():
    """
    Create a species object
    """
    return Species(name='plantus')

@pytest.fixture
def one_plant():
    """
    Create a standard Greenus plantus
    """
    g = Genus(name='Greenus')
    s = Species(name='plantus')
    p = Flora(genus=g,species=s)
    return p

@pytest.fixture
def one_bug():
    """
    Create a standard Buzzie beezii
    """
    g = Genus(name='Buzzie')
    s = Species(name='beezii')
    b = Fauna(genus=g,species=s)
    return b

@pytest.fixture
def one_location():
    l = Location(name='Here',lattitude=40.000,longitude=-105.000,altitude=5000)
    return l

@pytest.fixture
def one_seed():
    s = Seed(collection_lot='SCF-1234')
    return s