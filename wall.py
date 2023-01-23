import ifcopenshell
import ifcopenshell.util.element

m = ifcopenshell.open("231110AC-11-Smiley-West-04-07-2007.ifc")
walls = m.by_type("IfcWall")
print(len(walls))

print(f'Liczba ścian w modelu: {len(walls)}')

#property set

walls = m.by_type("IfcWall")
wall = walls[1]
pset_for_wall = ifcopenshell.util.element.get_psets(wall)
print(pset_for_wall)

#l. scian zewnetrznych

walls = m.by_type("IfcWall")
ext_walls = []
for w in walls:
    psets = ifcopenshell.util.element.get_psets(w)
    if psets.get("Pset_WallCommon"):
        if bool(psets.get("Pset_WallCommon").get("IsExternal")):
            ext_walls.append(w)
            
print(f'Liczba ścian zewnętrznych: {len(ext_walls)}')

#objetosc

totalvolume = 0

for w in ext_walls:
    psets = ifcopenshell.util.element.get_psets(w)
    for psetname, pset_dict in psets.items():
        for name, value in pset_dict.items():
            # print (f"{name}: {value}")
            if name == "NetVolume":
                totalvolume += float(value)
print(f'Objętość: {totalvolume:.2f}')
