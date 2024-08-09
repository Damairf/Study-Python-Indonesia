# Filter
# filter(function, iterasi)

teman = [("Guss", 19),
         ("Zulfi", 18),
         ("Bambang", 21),
         ("Josh", 17),
         ("Steve", 24),
         ("Yudha", 15)]

umur = lambda usia: usia[1] >= 18

teman_dewasa = list(filter(umur, teman))

for i in teman_dewasa:
    print(i)