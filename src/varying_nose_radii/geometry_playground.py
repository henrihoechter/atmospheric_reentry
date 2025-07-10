import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the points
points = {
    0: (0.0000000000, 0.0000000000, 0.0000000000), # heatshield apex
    1: (0.0678458016, 0.38440644288, 0.01678354775), # nose circle and straight line tangency point max Y
    2: (0.1391766360, 0.58019977018, 0.02533206904), # straight line and shoulder circle tangency point max Y
    3: (0.2566382136, 0.6623689709, 0.02891965382), # shoulder circle apex max Y
    4: (-0.4, 0.0000000000, 0.0000000000), # computational domain apex
    5: (-0.2914467174, 0.6150503087, 0.02685367641), # comp domain nose circle and straight line tangency max Y
    6: (-0.1588457268, 0.8991433994, 0.03925744863), # boundary point max Y
    7: (0.2566382136, 1.38846172541, 0.06062154812), # comp domain max X max Y point
    8: (0.0678458016, 0.38440644288, -0.01678354775), # nose circle and straight line tangency point max Z
    9: (0.1391766360, 0.58019977018, -0.02533206904), # straight line and shoulder circle tangency point max Z
    10: (0.2566382136, 0.6623689709, -0.02891965382), # shoulder circle apex max Z
    11: (-0.2914467174, 0.6150503087, -0.02685367641), # comp domain nose circle and straight line tangency max Z
    12: (-0.1588457268, 0.8991433994, -0.03925744863), # boundary point max Z
    13: (0.2566382136, 1.38846172541, -0.06062154812) # comp domain max X max Z point
}

# points = {
    # ------------------------------------------------------------------------------------------------------------------
#     # Body points (Inner boundary of the computational domain, on the cone surface)
#     # ------------------------------------------------------------------------------------------------------------------
#     0: (0.0000000000, 0.0000000000, 0.0000000000), # 0: Heatshield Apex (same as original 0)

#     # Front wedge plane points (positive Y, positive Z)
#     1: (0.0678458016, 0.38440644288, 0.01678354775), # 1: Nose-cone tangency (same as original 1)
#     2: (0.2566382136, 0.6623689709, 0.02891965382),  # 2: End of straight cone body (was original 3 - shoulder apex)

#     # Back wedge plane points (positive Y, negative Z)
#     7: (0.0678458016, 0.38440644288, -0.01678354775),# 7: Nose-cone tangency (same as original 8)
#     8: (0.2566382136, 0.6623689709, -0.02891965382),  # 8: End of straight cone body (was original 10 - shoulder apex)

#     # ------------------------------------------------------------------------------------------------------------------
#     # Computational Domain points (Outer boundary of the computational domain)
#     # ------------------------------------------------------------------------------------------------------------------
#     3: (-0.4000000000, 0.0000000000, 0.0000000000), # 3: Computational domain apex on X-axis (was original 4)

#     # Front wedge plane points (positive Y, positive Z)
#     4: (-0.2914467174, 0.6150503087, 0.02685367641), # 4: Upstream domain boundary (was original 5)
#     5: (0.2566382136, 1.38846172541, 0.06062154812), # 5: Downstream domain boundary (was original 7)

#     # Back wedge plane points (positive Y, negative Z)
#     9: (-0.2914467174, 0.6150503087, -0.02685367641), # 9: Upstream domain boundary (was original 11)
#     10: (0.2566382136, 1.38846172541, -0.06062154812) # 10: Downstream domain boundary (was original 13)
# }

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Extract coordinates for plotting
X = np.array([p[0] for p in points.values()])
Y = np.array([p[1] for p in points.values()])
Z = np.array([p[2] for p in points.values()])

# Plot points
ax.scatter(X, Y, Z, c='r', marker='o', s=50)

# Label points
for i, (x, y, z) in points.items():
    ax.text(x, y, z, f'{i}', color='blue')

# --- Draw connections to infer shape ---
# Body profile (X-Y plane, assuming Z is near 0 for these points)
# Points 0, 1, 2, 3 likely define a curve or segments
# Let's connect them as if they form a line segment for now.
# # Points 0, 1 (nose), 2 (shoulder), 3 (end of body)
# ax.plot([points[0][0], points[1][0]], [points[0][1], points[1][1]], [points[0][2], points[1][2]], 'k--')
# ax.plot([points[1][0], points[2][0]], [points[1][1], points[2][1]], [points[1][2], points[2][2]], 'k--')
# ax.plot([points[2][0], points[3][0]], [points[2][1], points[3][1]], [points[2][2], points[3][2]], 'k--')

# # Corresponding Z-plane points (8, 9, 10)
# ax.plot([points[0][0], points[8][0]], [points[0][1], points[8][1]], [points[0][2], points[8][2]], 'g--')
# ax.plot([points[8][0], points[9][0]], [points[8][1], points[9][1]], [points[8][2], points[9][2]], 'g--')
# ax.plot([points[9][0], points[10][0]], [points[9][1], points[10][1]], [points[9][2], points[10][2]], 'g--')

# # Connecting Y-plane to Z-plane for the body
# ax.plot([points[1][0], points[8][0]], [points[1][1], points[8][1]], [points[1][2], points[8][2]], 'm:')
# ax.plot([points[2][0], points[9][0]], [points[2][1], points[9][1]], [points[2][2], points[9][2]], 'm:')
# ax.plot([points[3][0], points[10][0]], [points[3][1], points[10][1]], [points[3][2], points[10][2]], 'm:')

# # Computational domain boundary in X-Y plane (4, 5, 6, 7)
# ax.plot([points[4][0], points[5][0]], [points[4][1], points[5][1]], [points[4][2], points[5][2]], 'b-')
# ax.plot([points[5][0], points[6][0]], [points[5][1], points[6][1]], [points[5][2], points[6][2]], 'b-')
# ax.plot([points[6][0], points[7][0]], [points[6][1], points[7][1]], [points[6][2], points[7][2]], 'b-')

# Corresponding Z-plane domain boundary (4, 11, 12, 13)
# ax.plot([points[4][0], points[11][0]], [points[4][1], points[11][1]], [points[4][2], points[11][2]], 'c-')
# ax.plot([points[11][0], points[12][0]], [points[11][1], points[12][1]], [points[11][2], points[12][2]], 'c-')
# ax.plot([points[12][0], points[13][0]], [points[12][1], points[13][1]], [points[12][2], points[13][2]], 'c-')

# Connecting Y-plane to Z-plane for domain
# ax.plot([points[5][0], points[11][0]], [points[5][1], points[11][1]], [points[5][2], points[11][2]], 'y:')
# ax.plot([points[6][0], points[12][0]], [points[6][1], points[12][1]], [points[6][2], points[12][2]], 'y:')
# ax.plot([points[7][0], points[13][0]], [points[7][1], points[13][1]], [points[7][2], points[13][2]], 'y:')

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Visualization of blockMeshDict Vertices')
ax.grid(True)
plt.show()

# --- Interpretation ---
print("\nInterpretation of Points:")
print("Points 0-3 (0, 1, 2, 3) define one profile of the body.")
print("Points 8-10 (8, 9, 10) define another profile of the body, seemingly mirrored in Z (or Y, depending on axis interpretation).")
print("Points 4-7 (4, 5, 6, 7) define one profile of the outer computational domain.")
print("Points 11-13 (11, 12, 13) define another profile of the outer computational domain, again mirrored.")
print("\nThis pattern is typical for a 'wedge' or 'azimuthal slice' geometry in OpenFOAM's blockMesh.")
print("The domain likely spans from the X-axis (where Y=0 and Z=0 for points 0 and 4) outwards.")
print("The positive Y points (1,2,3,5,6,7) define one 'side' of the wedge.")
print("The negative Z points (8,9,10,11,12,13) define the other 'side' of the wedge (note Z is negative Y of previous points).")
print("The 'max Y' and 'max Z' descriptions indicate these are the outer boundaries of your wedge slice.")
print("Points 0 and 4 are on the X-axis, serving as apexes for the body and computational domain, respectively.")