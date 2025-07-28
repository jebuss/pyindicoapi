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
