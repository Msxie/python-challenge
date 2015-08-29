import pickle

peak = open('banner.p')
data = pickle.load(peak)
for meta in data:
    val = ''
    for tu in meta:
        val = val + tu[0]*tu[1]
    print val
peak.close()
