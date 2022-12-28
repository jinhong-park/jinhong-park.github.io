pip3 install sympy_plot_backends[all]

jupyter nbconvert --to markdown JUPYTER_NOTEBOOK.ipynb


```python
from sympy import *
from spb import *


x = Symbol('x')
plot(1/x,(x,-1,1))
```


    
![png](https://jinhong-park.github.io/memos/2_sympy_plot_files/2_sympy_plot_1_0.png)
    








```python
plot(gamma(x), (x, -5, 5), ylim=(-5,5))
```




    
![png](https://jinhong-park.github.io/memos/2_sympy_plot_files/2_sympy_plot_2_1.png)
    









```python
plot(gamma(x), (x,-5,5), ylim=(-5,5), detect_poles=True, adaptive=False, n=2e4, eps = 1E-4)
```


    
![png](https://jinhong-park.github.io/memos/2_sympy_plot_files/2_sympy_plot_3_0.png)
    







```python
plot(floor(x), (x,0,8))
```


    
![png](https://jinhong-park.github.io/memos/2_sympy_plot_files/2_sympy_plot_4_0.png)
    








```python
plot(floor(x), (x,0,8), detect_poles=True)
```


    
![png](https://jinhong-park.github.io/memos/2_sympy_plot_files/2_sympy_plot_5_0.png)
    






```python
# Two plots in one with different line styles
# and line widths :

p1 = plot(sin(x), (x, -2*pi, 2*pi), {'linestyle': '--'}, show=False)
p2 = plot(cos(x), (x, -2*pi, 2*pi), {'linewidth': 4}, show=False)
(p1 + p2).show()
```


    
![png](https://jinhong-park.github.io/memos/2_sympy_plot_files/2_sympy_plot_6_0.png)
    



```python
from sympy import *
from spb import *

x = Symbol('x')
plot(sin(x), cos(x), (x,-2*pi, 2*pi), backend = MB)
```


    
![png](https://jinhong-park.github.io/memos/2_sympy_plot_files/2_sympy_plot_7_0.png)
    






```python
from sympy import *
from spb import *

x = Symbol('x')
plot(sin(x), cos(x), (x,-2*pi, 2*pi), backend = MB) ## BB means Bokeh
```


    
![png](https://jinhong-park.github.io/memos/2_sympy_plot_files/2_sympy_plot_8_0.png)
    





```python
from sympy import *
from spb import plot_polar


phi = symbols('phi')

expr = sin(phi) * cos(3 * phi) + pi/2

plot_polar(expr, (phi, 0, 2 * pi), polar_axis = True, ylim = (0,3), title = "$%s$" %latex(expr) )


```


    
![png](https://jinhong-park.github.io/memos/2_sympy_plot_files/2_sympy_plot_9_0.png)
    








```python
from sympy import *
from spb import *

z = Symbol('z')
expr = log(z)
plot_complex( expr, (z, -2-2j, 2+2j), coloring = 'b', title = '$' + latex(expr)+'$', backend=MB)   ## MB -> BB bokeh backend
```


    
![png](https://jinhong-park.github.io/memos/2_sympy_plot_files/2_sympy_plot_11_0.png)
    




```python
from sympy import *
from spb import *
import numpy as np


u, v = symbols("u, v")

plot3d_parametric_surface(1.2**v * sin(u)**2 * sin(v), 
1.2**v * sin(u)**2 * cos(v), 
1.2**v * sin(u)* cos(u), (u, 0, pi) , (v, -pi/4, 3*pi),
wireframe = True,  use_cm = True, wf_n1 = 50, backend = MB)   ## MB -> PB plotly backend

```


    
![png](https://jinhong-park.github.io/memos/2_sympy_plot_files/2_sympy_plot_12_0.png)
    
