# hca-bundle-jsonld-lambda
Generate RDF from HCA bundles using a AWS microservice.

This simple microservice accepts HCA bundles identifiers and
returns JSON-LD created using the [hca-bundle-jsonld](https://github.com/simonjupp/hca-bundle-jsonld)
module. It will then return the resulting turtle file to the consumer. These
results can be added to a triple store so they can be queried via SPARQL,
or loaded to disk to perform local queries.

This is conceived to work as part of an infrastructure that could
create a graph store of data in the Human Cell Atlas.

For more information see [hca-bundle-jsonld](https://github.com/simonjupp/hca-bundle-jsonld)
or the Example Usage notebook.

## Development

Head over to the issues! Some of the open issues are:

* Better dependency management
  * hca_bundle_jsonld is not in amazon's pypi so we manually update
* Content negotiation
  * Add the ability to return JSON-LD in addition to turtle.
* Dynamic queries
  * Add the ability to do queries dynamically against the resulting RDF.
* Add yours in the issues!