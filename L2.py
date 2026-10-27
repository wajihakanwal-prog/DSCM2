pasta={"pasta Arrabita","italian pasta",20,"Medium"}
print(pasta)
biryani=("chicken biryani","indian biryani",45,"Hard")
print(biryani)
print("Name :",pasta[0])
print("Price :",pasta[2])
print("Type :",pasta[3])

all_recipes=(pasta,biryani)
print("first recipe name",all_recipes[0][0])
print("second recipe name",all_recipes[1][0])
print("pasta details :",pasta[1:3])
print("biryani details :",biryani[1:3])

for details in pasta:
    print(details)


pasta_ingredients={"tomato","onion","garlic","olive oil","spices","cheese"}
print(pasta_ingredients)
biryani_ingredients=("chicken","rice","spices","oil","onion","garlic")
print(biryani_ingredients)
print("Total pasta ingredients :",len(pasta_ingredients))

pasta_ingredients.add("olive oil")
print(pasta_ingredients)

pasta_ingredients.remove("olive oil")
print(pasta_ingredients)

pasta_ingredients.update(["olive oil","spices"])
print(pasta_ingredients)

pasta_ingredients.discard("olive oil")
print(pasta_ingredients)

all_ingredients=pasta_ingredients.union(biryani_ingredients)
common=pasta_ingredients.intersection(biryani_ingredients)
print("All ingredients :",all_ingredients)
only_pasta=pasta_ingredients.difference(biryani_ingredients)
unique_to_pasta=pasta_ingredients.symmetric_difference(biryani_ingredients)
print("Common ingredients :",common)
print("Only pasta ingredients :",only_pasta)
print("Unique to pasta :",unique_to_pasta)
