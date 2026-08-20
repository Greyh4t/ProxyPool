# ProxyPool

Crawl, validate, and serve HTTP/HTTPS proxies.

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (recommended)

Project dependencies are listed in `requirements.txt`.

## Installation

```powershell
uv venv .venv
uv pip install --python .venv\Scripts\python.exe -r requirements.txt
```

## Usage

Start the proxy pool:

```powershell
uv run proxypool.py
```

The API listens on:

```text
http://localhost:8000
```

Query parameters can be combined to filter the result:

```text
http://localhost:8000/?num=1&port=80&type=3&protocol=http&minscore=0&area=北京
```

The response contains the proxy address and its latest validation latency in
milliseconds:

```json
[["1.2.3.4:8080", 345]]
```

## Configuration

Validation settings are defined in `config.py`. `MAX_LATENCY` is the maximum
accepted proxy latency in milliseconds. A proxy that takes longer than this
limit does not pass validation.

```python
VALIDATE_CONFIG = {
    "TIMEOUT": 20,
    "MAX_LATENCY": 1000,
}
```

The `type` parameter represents the proxy anonymity level:

```text
0: unknown
1: transparent
2: anonymous
3: high anonymous
```
