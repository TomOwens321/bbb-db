from bbb.models.species import Species

def test_add_species():
    name = 'speciesone'
    s1 = Species(name=name)
    assert s1.name == name

def test_description():
    s1 = Species(desc='SCF')
    assert s1.desc == 'SCF'

def test_plants_list():
    s1 = Species()
    assert len(s1.plants) == 0