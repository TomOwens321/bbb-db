from bbb.models import Flora, Genus, Species, Family
from bbb import db

def flat_list(l):
    return ["%s" % v for v in l]

def _exists(table, value):
    s = db.session()
    r = s.query(table).filter(table.name==value).first()
    if not r:
        print("New record!")
        r = table(name=value)
        s.add(r)
        s.commit()
    return r

def smart_delete(table, record):
    print("Deleting {} from {}".format(record.name, table))
    session = db.session()
    if hasattr(record, 'plants'):
        for p in record.plants:
            record.plants.remove(p)
    if hasattr(record, 'bugs'):
        for b in record.bugs:
            record.bugs.remove(b)
    if hasattr(record, 'locations'):
        for l in record.locations:
            record.locations.remove(l)
    if not (record.genus.plants or record.genus.bugs):
        session.delete(record.genus)
    if not (record.species.plants or record.species.bugs):
        session.delete(record.species)
    session.delete(record)
    session.commit()
