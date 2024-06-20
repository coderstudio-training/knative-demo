# The Plan

## Intro

- [ ] What is serverless?
- [ ] What is event driven architecture?
- [ ] What is knative?
  - https://knative.dev/docs/about/testimonials/
  - https://knative.dev/docs/concepts/

## Setup

Install system:

- [ ] Install knative serving - https://knative.dev/docs/install/yaml-install/serving/install-serving-with-yaml/
- [ ] Install knative eventing - https://knative.dev/docs/install/yaml-install/serving/install-serving-with-yaml/
- [ ] or Install via Knative Operator - kubectl apply -f https://github.com/knative/operator/releases/download/knative-v1.14.3/operator.yaml
- Install CLIs:
  - [ ] Install `kn` cli https://knative.dev/docs/client/install-kn/
  - [ ] Intall `func` cli https://knative.dev/docs/getting-started/install-func/

## Deploy a knative Function

- [ ] create function - https://knative.dev/docs/functions/creating-functions/
- [ ] explore generated files https://github.com/boson-project/parliament

## Deploy a knative Service

- [ ] deploy podinfo
- [ ] show traffic splitting

## Deploy an event driven application

- [ ] What are cloudevents?
  ```
  {
      "specversion" : "1.0",
      "type" : "com.github.pull.create",
      "source" : "https://github.com/cloudevents/spec/pull",
      "subject" : "123",
      "id" : "A234-1234-1234",
      "time" : "2018-04-05T17:31:00Z",
      "comexampleextension1" : "value",
      "comexampleothervalue" : 5,
      "datacontenttype" : "text/xml",
      "data" : "<much wow=\"xml\"/>"
  }
  ```
- [ ]
