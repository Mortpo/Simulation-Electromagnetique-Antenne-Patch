import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


print('Chemin du fichier')
chemin = "D:/ESIREM/4A/Python-microonde/Ccode/Projet4AFDTD/Data3D/CEzplane"

data = np.zeros((120,62))
num=0
with open(chemin, newline='') as csvdata:
    datareader = csv.reader(csvdata, delimiter=' ')
    for row in datareader:
        for i in range(62):
            data[num][i]=float(row[i])
        num+=1


print(data.shape)
plt.imshow(data)
plt.show()

#donnees
tailleX, tailleY = data.shape
x = np.arange(tailleX)
y = np.arange(tailleY)
X,Y= np.meshgrid(x,y)
Z = data
#figure
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, np.transpose(Z), rstride=1,cstride=1 ,cmap=cm.magma, antialiased=True)

#axe
#ax.set_zlim(-0.5, 0.5)
#affichage
plt.show()