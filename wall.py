import ifcopenshell
import ifcopenshell.util.element

m = ifcopenshell.open("231110AC-11-Smiley-West-04-07-2007.ifc")
walls = m.by_type("IfcWall")
print(len(walls))

print(f'Liczba ścian w modelu: {len(walls)}')

#dodawanie