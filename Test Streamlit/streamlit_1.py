import streamlit as slt
import matplotlib.pyplot as plt
import numpy as np
slt.write(
    """
    # Welcome

    #### Hello, friends!
    """
)


 
x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
slt.pyplot(fig)