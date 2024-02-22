def _is_valid_url(url: str) -> bool:
    """Check if the url is valid."""
    from urllib.parse import urlparse
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)
