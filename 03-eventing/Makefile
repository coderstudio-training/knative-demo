FUNC_NAME=my-event-function 

create-function:
	kn func create -l python ${FUNC_NAME}

copy-func-py:
	cp ./func.py ./${FUNC_NAME}

REGISTRY=ghcr.io/sidpalas/knative-${FUNC_NAME}

deploy:
	echo "Generate token from github to authenticate"
	cd ${FUNC_NAME} && func deploy --registry=${REGISTRY}

deploy-broker:
	kubectl apply -f broker.yaml

deploy-trigger:
	kubectl apply -f trigger.yaml

create-curl-pod:
	kubectl run curl --rm --image=radial/busyboxplus:curl -it -- /bin/sh

# Second service to catch event from first service
deploy-event-display:
	kn service create event-display \
		--image gcr.io/knative-releases/knative.dev/eventing/cmd/event_display \
		--port 8080 \

deploy-event-display-trigger:
	kn trigger create event-display \
		--broker=default \
		--filter=type=dev.knative.hifromknative \
		--filter=source=knative/eventing \
		--sink=ksvc:event-display
