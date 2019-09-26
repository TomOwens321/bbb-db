from .test_db_fixtures import one_seed

def test_seed_fixture(one_seed):
    assert 'SCF' in one_seed.collection_lot