# jFoil

Easily create and plot airfoils using the Joukowsky transformation.

It also uses the potential flow model to characterize and plot the foil's performance at different angles of attack.

<p align="center">
    <br>
    <img src="https://i.imgur.com/7z7Q8Q0.png" width="400"/>
    <br>
<p>

### Install

Using pip:

```bash
pip install jFoil
```

### Example:

```python
import jFoil as jf

# Creates the foil:
foil = jf.jFoil(1, 0.9, 6)

# Saves each point of the foil in csv format:
foil.saveFoil('test_foil.csv')

# Shows the airfoil alone:
foil.plotFoil()

# Shows the airfoil and the current lines for an angle of attack:
foil.currentLines(5)

# Plots the airfoil coefficient of lift with respect to the angle of attack:
foil.plotcL()
```


