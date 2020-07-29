*****
FTOML
*****

Extends the python module *toml* with the python library *fstring*

See the test-files for some examples

you can do things like::

    base_url="https://example.com"

    [module1]
    url="{base_url}/path1.html"

    [module2]
    url="{base_url}/path2.html"


... and many things more

Tox
===

Prerequisites for pyenv according to https://github.com/pyenv/pyenv/wiki/Common-build-problems ::

    sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

To prepare tox for the tests, install pyenv and install all needed python versions. e.g.::

    echo pypy-5.7.1 2.7.18 3.5.9 3.6.11 3.7.8 3.8.5|xargs -n1 pyenv install
    pyenv global pypy-5.7.1 2.7.18 3.5.9 3.6.11 3.7.8 3.8.5

then run tox::

    tox



