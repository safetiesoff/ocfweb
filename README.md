ocfweb
==========
[![Build Status](https://jenkins.ocf.berkeley.edu/buildStatus/icon?job=ocfweb-test)](https://jenkins.ocf.berkeley.edu/job/ocfweb-test/)

The main ocf website.


## Working on `ocfweb`

Clone the repo, and be sure to check out submodules:

    $ git clone git@github.com:ocf/ocfweb.git
    $ git submodule update --init


### Running in development mode

Either on supernova, or on your own staff VM, run `make dev`. The first time
will take a while, but future runs will be almost instant thanks to
[pip-faster](https://github.com/Yelp/pip-faster).

It will start listening on a deterministically random port (really, 8000 plus
the last 3 digits of your user id) which is printed to you. You can then view
the site in development.


### Building SCSS

Run `make scss` to build SCSS. You can also use `make watch-scss` to rebuild it
automatically when SCSS files change.


### Running tests

To run tests locally, run `make check`. Please don't push to master with
failing tests—Jenkins will refuse to deploy your code, and nobody will be able
to deploy until fixing it.
