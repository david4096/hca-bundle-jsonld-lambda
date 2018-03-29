import os
import logging

import requests

from hca_bundle_jsonld.bundle_to_rdf import bundle_to_rdf
from chalice import Chalice, Response

app = Chalice(app_name='hca-bundle-jsonld-lambda', debug=True)
app.log.setLevel(logging.DEBUG)


DSS_URL = "https://dss.dev.data.humancellatlas.org/v1"


def bundle_json_to_turtle_string(bundle):
    os.chdir('/tmp')
    file_name = bundle_to_rdf(bundle)
    turtle = ""
    with open("/tmp/{}".format(file_name), "r") as f:
        turtle = f.read()
    return turtle

@app.route('/{bundle_uuid}')
def index(bundle_uuid):
    r = requests.get("{}/bundles/{}?replica=aws".format(DSS_URL, bundle_uuid))
    if r.status_code == 200:
        turtle = bundle_json_to_turtle_string(r.json())
        return Response(body=turtle,
                        status_code=200,
                        headers={'Content-Type': 'text/turtle'})
    else:
        return Response(body=r.json(), status_code=r.status_code)

