---
layout: post
title:  "eigensystem in python"
date:   2022-11-28 00:16:27
---


## Eigensystem in python


```python
import numpy as np

# mathematica style function defined
Matrix = np.array     
Eigensystem = np.linalg.eig
Conj = np.conjugate

A = Matrix([[-4, 4, -1, 9],
           [6, -6, 9, 10],
           [-5, 8, 6, 8],
           [ 7, 0, -4, -2]])

Eigenvalues, eigenvectors_tem =  Eigensystem(A)

Eigenvectors = eigenvectors_tem.transpose() 
```
np.matrix 도 가능하지만 
np.matrix 는 numpy 공식문서에서 말하길 곧 없어진다고 함.
It is no longer recommended to use the np.matrix class, 
even for linear algebra. Instead use regular np.array. 
The np.matrix class may be removed in the future.
python 은 transpose 해야 제대로된 eigenvectors를 얻을 수 있음. 

### Eigenvalues

```python
Eigenvalues
```




    array([  7.91990627+3.47031997j,   7.91990627-3.47031997j,
           -13.76135877+0.j        ,  -8.07845377+0.j        ])



### Eigenvectors


```python
Eigenvectors
```




    array([[-0.0091516 +0.29357931j,  0.39202769+0.23164396j,
             0.76189327+0.j        , -0.21490198+0.28234479j],
           [-0.0091516 -0.29357931j,  0.39202769-0.23164396j,
             0.76189327-0.j        , -0.21490198-0.28234479j],
           [-0.46037801+0.j        ,  0.74688832+0.j        ,
            -0.46565954+0.j        ,  0.11563357+0.j        ],
           [-0.50291592+0.j        , -0.68341441+0.j        ,
            -0.08688245+0.j        ,  0.52198828+0.j        ]])



### The eigenvectors are already normalized


```python
np.dot(Conj(Eigenvectors[0]), Eigenvectors[0])
```




    (1+0j)




```python
len(Eigenvalues)
```




    4



### Eigenvalues, Eigenvectors check!
A.$\varphi$[i] - $\lambda$[i] $\varphi$[i] = 0


```python
tem = 0.0
for i in range(len(Eigenvalues)) : 
    tem += np.dot(A, Eigenvectors[i]) - Eigenvalues[i]* Eigenvectors[i]

tem

```




    array([ 6.66133815e-15+0.j,  4.44089210e-15+0.j, -1.46549439e-14+0.j,
            7.32747196e-15+0.j])



### numerically small value
6.66133815e-15 ~ 0