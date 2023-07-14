import numpy as np
import matplotlib.pyplot as plt

melons_width = np.random.normal(35, 4, 250)
melons_height = np.random.normal(8, 2, 250)
melons_weight = np.random.normal(10, 0.5, 250)
dict_melon = {'wid':melons_width, 'hei':melons_height, 'wei':melons_weight}

balloon_width = np.random.normal(40, 4, 250)
balloon_height = np.random.normal(10, 3, 250)
balloon_weight = np.random.normal(1, 0.5, 250)
dict_balloon = {'wid':balloon_width, 'hei':balloon_height, 'wei':balloon_weight}

ax = plt.axes(projection='3d')
ax.scatter(dict_melon['wid'], dict_melon['hei'], dict_melon['wei'],marker='^', c='orange', label='Melons')

ax.scatter(dict_balloon['wid'], dict_balloon['hei'], dict_balloon['wei'], c='Blue', label='Ballons')

ax.legend()

ax.set_xlabel('Width')
ax.set_ylabel('Length')
ax.set_zlabel('Weight')

plt.show()