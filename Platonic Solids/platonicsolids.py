import pyvista as pv

kinds = [
    "tetrahedron",
    "cube",
    "octahedron",
    "dodecahedron",
    "icosahedron",
]
centers = [
    (0, -2, 0),
    (0, -1, 0),
    (0, 0, 0),
    (0, 1, 0),
    (0, 2, 0),
]

colors = ["red", "yellow", "green", "blue", "purple"]

solids = [
    pv.PlatonicSolid(kind, radius=0.4, center=center)
    for kind, center in zip(kinds, centers)
]

p = pv.Plotter(window_size=[2000, 1000])
for ind, solid in enumerate(solids):
    smooth_shading = ind == len(solids) - 1
    p.add_mesh(
        solid,
        color=colors[ind],
        smooth_shading=smooth_shading,
        specular=1.0,
        specular_power=10,
        show_edges=True,
    )

p.view_vector((5.0, 2, 3))
p.add_floor("-z", lighting=True, color="tan", pad=1.0)
p.enable_shadows()
p.show()
