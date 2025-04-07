from utils.Release import Release

pr = Release(16426)

print(pr.title_ru)
pr.load()
print(pr.title_ru)