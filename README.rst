*****
FTOML
*****

Extends the python module _toml_ with the python library _fstring_

See the test-files for some examples

you can do things like::

    base_url="https://example.com"

    [module1]
    url="{base_url}/path1.html"

    [module2]
    url="{base_url}/path2.html"


... and many things more
