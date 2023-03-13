from pydbpedia import PyDBpedia, namespace

dbpedia_uris = ["http://dbpedia.org/resource/Elon_Musk"]

dbpedia_wrapper = PyDBpedia(endpoint="http://dbpedia.org/sparql")
objects = dbpedia_wrapper.get_objects(subjects=dbpedia_uris, predicates=[namespace.RDF_TYPE])

print(objects)

