deploy-podinfo-service-blue:
	kn service create podinfo \
		--image ghcr.io/stefanprodan/podinfo:6.5.4 \
		--port 9898 \
		--env PODINFO_UI_COLOR="#34577c"

deploy-podinfo-service-green:
	kn service update podinfo \
		--image ghcr.io/stefanprodan/podinfo:6.5.4 \
		--port 9898 \
		--env PODINFO_UI_COLOR="#AFE1AF"

list-revisions:
	kn revisions list

apply-traffic-split:
	kn service update podinfo \
		--traffic podinfo-00001=50 \
		--traffic @latest=50