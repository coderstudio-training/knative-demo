from parliament import Context
from flask import make_response
import uuid
import logging
import sys

logging.basicConfig(level=logging.INFO)

def main(context: Context):
    """ 
    Function template
    The context parameter contains the Flask request object and any
    CloudEvent received with the request.
    """

    # Add your business logic here
    logging.info("Received request!")
    logging.info(context.request.data)

    response = make_response({
        "msg": "Hi from knative event driven app!"
    })
    response.headers["Ce-Id"] = str(uuid.uuid4())
    response.headers["Ce-specversion"] = "0.3"
    response.headers["Ce-Source"] = "knative/eventing"
    response.headers["Ce-Type"] = "dev.knative.hifromknative"
    return response