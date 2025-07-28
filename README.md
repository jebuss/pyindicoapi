# pyindicoapi

A Python API wrapper for the CERN Indico API.

---

## Installation

```bash
cd pyindicoapi
pip install .
```

---

## Usage

in order to use the Indico API you need an excess token and the `url` of your Indico instance

```python
from pyindicoapi import IndicoAPI

API_TOKEN= "my Token"
BASE_URL = "https://my.indico.server"

api = IndicoAPI( BASE_URL, API_TOKEN)
```

### Categories

```python
categories = api.list_categories()
print(categories)

# get subcategories of category with id 1
subcategories = api.list_categories(1)

# get a category (category id = 1)
category = api.get_category(1)
```

### Events

#### List events

```python
api.list_events()
```

#### Get an event

```python

# get event with id = 1
event = get_event(1)
```

#### Custom resource

You may also call a custom resource from the Indico API according to the [API resources](https://docs.getindico.io/en/latest/http-api/exporters/)

```python
resource = api.get_custom_resource(resource_name, resource_id, location=None, output_type='json')
```

where:

* `resource_name` is the specific resource you try to call (e.g. `categ `, `event `, `room`)
* `resource_id` is the id of the resource
* `location` location of the resource, e.g. the location of a room.
* `output_type` desired output format (e.g. *json* ,  *jsonp* ,  *xml* ,  *html* ,  *ics* ,  *atom* , *bin*) [default is `json`]
