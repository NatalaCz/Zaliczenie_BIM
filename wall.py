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

