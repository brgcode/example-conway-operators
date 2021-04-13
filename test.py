from compas.datastructures import Mesh
from compas.datastructures import (
    mesh_conway_ambo,
    mesh_conway_bevel,
    mesh_conway_dual,
    mesh_conway_expand,
    mesh_conway_gyro,
    mesh_conway_join,
    mesh_conway_kis,
    mesh_conway_meta,
    mesh_conway_needle,
    mesh_conway_ortho,
    mesh_conway_snub,
    mesh_conway_truncate
)

mesh = Mesh.from_polyhedron(6)

ambo = mesh_conway_ambo(mesh)
bevel = mesh_conway_bevel(mesh)
dual = mesh_conway_dual(mesh)
expand = mesh_conway_expand(mesh)
gyro = mesh_conway_gyro(mesh)
join = mesh_conway_join(mesh)
kis = mesh_conway_kis(mesh)
meta = mesh_conway_meta(mesh)
needle = mesh_conway_needle(mesh)
ortho = mesh_conway_ortho(mesh)
snub = mesh_conway_snub(mesh)
truncate = mesh_conway_truncate(mesh)
