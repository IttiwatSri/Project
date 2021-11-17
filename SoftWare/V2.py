import numpy as np
import warnings


# Per 1000 kcal
Omega6 = 6.2 # g.
Zinc = 95 # mg.
VitE = 15.5 # IU.
Calcium = 1.9 # g. 
Phosphorus = 1.9 # g.
Magnesium = 220 # mg.

warnings.filterwarnings('ignore')

nutrients = [ Omega6 , Zinc , VitE , Calcium , Phosphorus , Magnesium ]
allNutri = np.array(nutrients)
KcalperDay = 800 
necessity = allNutri * KcalperDay / 1000 
print(necessity)