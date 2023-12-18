curl -v "http://broker-ingress.knative-eventing.svc.cluster.local/default/default" \
	-X POST \
	-H "Ce-Id: 536808d3-88be-4077-9d7a-a3f162705f79" \
	-H "Ce-specversion: 0.3" \
	-H "Ce-Type: dev.knative.samples.helloworld" \
	-H "Ce-Source: dev.knative.samples/helloworldsource" \
	-H "Content-Type: application/json" \
	-d '{"msg":"Hello World from the curl pod."}'