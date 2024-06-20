FUNC_NAME=my-first-function 

create-function:
	kn func create -l python ${FUNC_NAME}

setup-python-env:
	eval "$(pyenv init -)"
	pyenv local 3.11.4
	python -m venv ./${FUNC_NAME}/venv && \
		source ./${FUNC_NAME}/venv/bin/activate

install-deps:
	cd ${FUNC_NAME} && pip install -r requirements.txt

run-func-local:
	cd ${FUNC_NAME} && ./app.sh

run-tests-local:
	cd ${FUNC_NAME} && python test_func.py

curl-app:
	curl http://localhost:8080/?message=hello

auth-knative-ghcr:
	docker login https://ghcr.io/v2/knative/

REGISTRY=ghcr.io/sidpalas/knative-my-first-func

build-image-local:
	cd ${FUNC_NAME} && func build --registry=${REGISTRY}

run-image-local:
	cd ${FUNC_NAME} && func run --registry=${REGISTRY}

deploy:
	echo "Generate token from github to authenticate"
	cd ${FUNC_NAME} && func deploy --registry=${REGISTRY}

invoke: 
	cd ${FUNC_NAME} && func invoke

describe-service:
	kn service describe my-first-function

list-revosions:
	kn revision list

describe-route:
	kn routes describe my-first-function

