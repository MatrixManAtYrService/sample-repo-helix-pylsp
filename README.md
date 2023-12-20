This repo exists to facilitate communication about project structure.  It has no useful functionality.


### Setup and Test

```
poetry config  virtualenvs.in-project true
poetry install
poetry run pytest
```

### pylsp stuff


When I am editing files in 'src', imports autocomplete without trouble

```
hx  src/sample/say_foo.py
# 'import samp...' autocompletes
```

But when I edit files in 'test', imports 
  
```
hx test/test_say_foo.py
# 'import samp...' does not autocomplete
```
Is there something I can do to give pylsp the bigger picture so that it autocompletes imports when editing test files?
 
