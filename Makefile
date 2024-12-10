PHONY: clean build
ALL: clean build 

PROJECT_NAME ?= covid-fusion
IMAGE_NAMESPACE ?= healthfusiongenai/${PROJECT_NAME}
PARENT_IMAGE_NAME=debian:12-slim
LOCAL_IMAGE_NAME_PREFIX=${IMAGE_NAMESPACE}

IMAGE_VERSION ?= $(shell cat VERSION)
APP_NAME_GSOD ?= cv-etl-gsod
APP_NAME_COUNTY_GEO ?= cv-etl-county-geo

# TODO: will needd to clean this up, and make it more robust, currently hardcoded to docker
ifeq ($(shell command -v podman 2> /dev/null),)
    CMD=docker
else
    CMD=podman
endif

CMD=docker

build-setup:
	@echo "__version__ = $(IMAGE_VERSION)"

# build all of the containers
containers: gsod-container county-geo-container

# Build the docker image for gsod
gsod-container:
	$(CMD) build \
	--network=host \
	--build-arg PARENT_IMAGE_NAME=$(PARENT_IMAGE_NAME) \
	--build-arg PROJECT_NAME=$(PROJECT_NAME) \
	-t $(LOCAL_IMAGE_NAME_PREFIX)-$(APP_NAME_GSOD):$(IMAGE_VERSION) \
	-f Dockerfile.cv-etl-gsod \
	.

# Build the docker image for gsod
county-geo-container:
	$(CMD) build \
	--network=host \
	--build-arg PARENT_IMAGE_NAME=$(PARENT_IMAGE_NAME) \
	--build-arg PROJECT_NAME=$(PROJECT_NAME) \
	-t $(LOCAL_IMAGE_NAME_PREFIX)-$(APP_NAME_COUNTY_GEO):$(IMAGE_VERSION) \
	-f Dockerfile.cv-etl-county-geo \
	.

# building nocache containers
gsod-nocache-container:
	$(CMD) build --no-cache \
	--network=host \
	--build-arg PARENT_IMAGE_NAME=$(PARENT_IMAGE_NAME) \
	--build-arg PROJECT_NAME=$(PROJECT_NAME) \
	-t $(LOCAL_IMAGE_NAME_PREFIX)-$(APP_NAME_GSOD):$(IMAGE_VERSION) \
	-f Dockerfile.cv-etl-gsod \
	.

county-geo-nocache-container:
	$(CMD) build --no-cache \
	--network=host \
	--build-arg PARENT_IMAGE_NAME=$(PARENT_IMAGE_NAME) \
	--build-arg PROJECT_NAME=$(PROJECT_NAME) \
	-t $(LOCAL_IMAGE_NAME_PREFIX)-$(APP_NAME_COUNTY_GEO):$(IMAGE_VERSION) \
	-f Dockerfile.cv-etl-county-geo \
	.

# Run the docker container
gsod-run: gsod-container
	$(CMD) run \
	--volume /data/gsod:/data/gsod \
	--entrypoint /bin/bash \
	$(LOCAL_IMAGE_NAME_PREFIX)-$(APP_NAME_GSOD):$(IMAGE_VERSION)

county-geo-run: county-geo-container
	$(CMD) run -rm \
	--volume /data/county-geo:/data/county-geo \
	--entrypoint /bin/bash \
	$(LOCAL_IMAGE_NAME_PREFIX)-$(APP_NAME_COUNTY_GEO):$(IMAGE_VERSION)	

exec-gsod: gsod-container
	$(CMD) exec -it $(LOCAL_IMAGE_NAME_PREFIX)-$(APP_NAME_GSOD):$(IMAGE_VERSION) /bin/bash

exec-county-geo: county-geo-container
	$(CMD) exec -it $(LOCAL_IMAGE_NAME_PREFIX)-$(APP_NAME_COUNTY_GEO):$(IMAGE_VERSION) /bin/bash

# Push the docker image to the registry
push:
	$(CMD) push $(APP_NAME):$(VERSION)

clean-all:
	$(CMD) system prune -a -f label=	

clean:
	$(CMD) system prune -a --filter label=${PROJECT_NAME} -f
