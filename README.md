# Veri Python Client
Python client for veri

```shell script
pip install veriservice
```


```python
import veriservice
```


```python
service = "localhost:5000"

veriservice.init_service(service)

vsc = veriservice.VeriClient(service)
```

```python
data_conf = {
    'dataName': 'example',
}

client.create_data_if_not_exists(data_conf)
data = [
            {
                'label': 'a',
                'feature': [0.5, 0.1, 0.2]
            },
            {
                'label': 'b',
                'feature': [0.5, 0.1, 0.3]
            },
            {
                'label': 'c',
                'feature': [0.5, 0.1, 1.4]
            },
        ]

insertion_conf = {
    'dataName': 'example',
    'ttl': 1000,
}
for d in data:
    client.insert(d['feature'], d['label'], d['label'], 0, insertion_conf)
```

```python
search_conf = {
    'dataName': 'example',
    'ttl': 1000,
}
result = client.search([0.1, 0.1, 0.1], search_conf)
for i in result:
    print(result)
```