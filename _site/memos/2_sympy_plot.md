pip3 install sympy_plot_backends[all]

jupyter nbconvert --to markdown JUPYTER_NOTEBOOK.ipynb


```python
from sympy import *
from spb import *


x = Symbol('x')
plot(1/x,(x,-1,1))
```


    
![png](https://jinhong-park.github.io/memos/2_sympy_plot_files/2_sympy_plot_1_0.png)
    





    <spb.backends.matplotlib.MatplotlibBackend at 0x114c5a1a0>




```python
plot(gamma(x), (x, -5, 5), ylim=(-5,5))
```

    /Users/parkjinhong/.pyenv/versions/3.10.3/lib/python3.10/site-packages/adaptive/learner/learner1D.py:573: RuntimeWarning: invalid value encountered in subtract
      self._scale[1] = np.max(y_max - y_min)
    /Users/parkjinhong/.pyenv/versions/3.10.3/lib/python3.10/site-packages/adaptive/learner/learner1D.py:448: RuntimeWarning: invalid value encountered in true_divide
      return y / y_scale



    
![png](https://jinhong-park.github.io/memos/2_sympy_plot_files/2_sympy_plot_2_1.png)
    





    <spb.backends.matplotlib.MatplotlibBackend at 0x13a262350>




```python
plot(gamma(x), (x,-5,5), ylim=(-5,5), detect_poles=True, adaptive=False, n=2e4, eps = 1E-4)
```


    
![png](https://jinhong-park.github.io/memos/2_sympy_plot_files/2_sympy_plot_3_0.png)
    





    <spb.backends.matplotlib.MatplotlibBackend at 0x13a371030>




```python
plot(floor(x), (x,0,8))
```


    
![png](https://jinhong-park.github.io/memos/2_sympy_plot_files/2_sympy_plot_4_0.png)
    





    <spb.backends.matplotlib.MatplotlibBackend at 0x13a5d08b0>




```python
plot(floor(x), (x,0,8), detect_poles=True)
```


    
![png](https://jinhong-park.github.io/memos/2_sympy_plot_files/2_sympy_plot_5_0.png)
    





    <spb.backends.matplotlib.MatplotlibBackend at 0x13a5d1450>




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
    





    <spb.backends.matplotlib.MatplotlibBackend at 0x13a9e9420>




```python
from sympy import *
from spb import *

x = Symbol('x')
plot(sin(x), cos(x), (x,-2*pi, 2*pi), backend = BB) ## BB means Bokeh
```





<div class="bk-root" id="d220fa84-d163-4145-8ad4-c5c80ef2f592" data-root-id="1145"></div>








    <spb.backends.bokeh.BokehBackend at 0x14a64d390>




```python
from sympy import *
from spb import plot_polar


phi = symbols('phi')

expr = sin(phi) * cos(3 * phi) + pi/2

plot_polar(expr, (phi, 0, 2 * pi), polar_axis = True, ylim = (0,3), title = "$%s$" %latex(expr) )


```


    
![png](https://jinhong-park.github.io/memos/2_sympy_plot_files/2_sympy_plot_9_0.png)
    





    <spb.backends.matplotlib.MatplotlibBackend at 0x14b8123b0>




