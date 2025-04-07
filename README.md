## anixart-api

Api client for [anixart](https://anixart.tv).

In this repository, requests are only for public information, without authorization, registration, etc.

### Usage:

```py
from utils.Release import Release

pr = Release(16426)

print(pr.title_ru) # None
pr.load()
print(pr.title_ru) # Восхождение героя щита 2
```
