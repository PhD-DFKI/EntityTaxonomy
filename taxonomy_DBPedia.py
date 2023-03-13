from SPARQLWrapper import SPARQLWrapper, JSON

def get_superclasses_DBPedia(word):
    # Set up the DBpedia endpoint and query
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    query = """
        SELECT DISTINCT ?superclassLabel WHERE {{
            <http://dbpedia.org/resource/%s> rdf:type/rdfs:subClassOf* ?superclass .
            ?superclass rdfs:label ?superclassLabel .
            FILTER(langMatches(lang(?superclassLabel), "en")) .
        }}
        
    """ % (word.replace(" ", "_"))
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    # Execute the query and extract the results
    results = sparql.query().convert()
    superclasses = [result["superclassLabel"]["value"] for result in results["results"]["bindings"]]

    return superclasses

superclasses = get_superclasses_DBPedia("Berlin")
print(superclasses)