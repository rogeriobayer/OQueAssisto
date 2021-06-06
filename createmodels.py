from detecto import core

dataset = core.Dataset('img/')
model = core.Model(['SporTV', 'sportv2', 'SporTV3'])

model.fit(dataset)
model.save('canais.pth')
