# Imhotep JSHint

Imhotep JSHint is a plugin for [Glow's Imhotep fork](https://github.com/glowdigitalmedia/imhotep), which provides bindings to the JSHint linter.


## Installation
Install the plugin with:

```
pip install -e git+git://github.com/glowdigitalmedia/imhotep_jshintdiff.git@0.1.1#egg=imhotep_jshintdiff
```

It also requires the JSHint linter:

```
npm install jshint

```

Optionally put ```.jshintrc``` with JSHint config in the repo root if you want to change the linting defaults.