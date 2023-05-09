# json-add-empty

This python script is designed to compare who json files and add missing keys with with emty strings.

## Samples

Template json

```json
{
  "TEST": {
    "test-1": "test-1",
    "test-2": "test-2",
    "test-3": "test-3",
    "test-nested": {
      "nested-1": "nested-1",
      "nested-2": "nested-2",
      "nested-3": "nested-3"
    }
  }
}
```

Test json

```json
{
  "TEST": {
    "test-1": "test-1"
  }
}
```

Result:

```json
{
  "TEST": {
    "test-1": "test-1",
    "test-2": "",
    "test-3": "",
    "test-nested": {
      "nested-1": "",
      "nested-2": "",
      "nested-3": ""
    }
  }
}
```

## Authors

- [@myek-9](https://github.com/myek-9)
