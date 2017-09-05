from pprint import pprint

import grequests
import requests


def http_get(url, headers=None):
    return requests.get(url, headers=headers)


def http_multiget(urls, headers=None):
    return zip(urls, grequests.map([grequests.get(url, headers=headers) for url in urls]))


def list_docker_hub_image_tags(repository):
    url = "https://hub.docker.com/v2/repositories/" + repository + "/tags"
    request_headers = {'Accept': 'application/json'}

    tags = []

    while url is not None:
        response = http_get(url, headers=request_headers)
        pprint(response.text)
        response_data = response.json()
        tags += response_data["results"]
        url = response_data["next"]

    return tags


def get_docker_hub_image_manifest(repository, reference):
    url = "https://index.docker.io/v2/" + repository + "/manifests/" + reference


    request_headers = {'Accept': 'application/vnd.docker.distribution.manifest.v2+json'}

    response = http_get(url, headers=request_headers)
    pprint(response.text)
    return response.json()


repository = 'samloh84/oracle-java-jdk'
tags = list_docker_hub_image_tags(repository)
pprint(tags)

for tag_info in tags:
    pprint(get_docker_hub_image_manifest(repository,tag_info['name']))
