furniture = ["chair", "table", "wardrobe", "sofa", "bed"]

for item in furniture:
	print(item)

for item in furniture:
	if (item != "sofa"):
		print(item)

furniture.append("box")
furniture.append("shit")

for item in furniture:
	print(item)

for item in furniture:
	if (item == "chair"):
		print("на нем можно сидеть")
	if (item == "table"):
		print("на нем можно писать")