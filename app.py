import os
import logging

import requests

from hca_bundle_jsonld.bundle_to_rdf import bundle_to_rdf
from chalice import Chalice, Response

app = Chalice(app_name='hca-bundle-jsonld-lambda', debug=True)
app.log.setLevel(logging.DEBUG)


DSS_URL = "https://dss.dev.data.humancellatlas.org/v1"


@app.route('/{bundle_uuid}')
def index(bundle_uuid):
    r = requests.get("{}/bundles/{}?replica=aws".format(DSS_URL, bundle_uuid))
    bundle = r.json()
    os.chdir('/tmp')
    file_name = bundle_to_rdf(bundle)
    turtle = ""
    with open("/tmp/{}".format(file_name), "r") as f:
        turtle = f.read()
    return Response(body=turtle,
                    status_code=200,
                    headers={'Content-Type': 'text/turtle'})

