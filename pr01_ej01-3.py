Python 3.8.10 (default, Jun  2 2021, 10:49:15) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 4**3/2
32.0
>>> 4/2**3
0.5
>>> (4/2)
2.0
>>> (4/2)**3
8.0
>>> (6-4)/(6+4)
0.2
>>> 5*(6-4)/(6+4)
1.0
>>> (5*(6-4))/(6+4)
1.0
>>> abs(6-4)/sqrt(6**2-4**2)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#7>", line 1, in <module>
NameError: name 'sqrt' is not defined
>>> import from math sqrt
SyntaxError: invalid syntax
>>> import math
>>> abs(6-4)/sqrt(6**2-4**2)

Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#10>", line 1, in <module>
NameError: name 'sqrt' is not defined
>>> from math import sqrt
>>> abs(6-4)/sqrt(6**2-4**2)
0.4472135954999579
>>> fido
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#13>", line 1, in <module>
NameError: name 'fido' is not defined
>>> fido=0
>>> dido=" "
>>> dido
' '
>>> guido=False
>>> guido==dido
False
>>> False==guido
True
>>> 0==fido
True
>>> 0=fido
SyntaxError: cannot assign to literal
>>> fido+=1
>>> dido=fido+1
>>> fido=fido+1
>>> fido==dido
True
>>> mi_nombre = 'Sergio'
>>> mi_grado = 'Diseño y desarrollo de videojuegos'
>>> mi_curso = 1
>>> print("Mi nombre es", mi_nombre, "y estudio", mi_curso, "de", mi_grado, ".")
Mi nombre es Sergio y estudio 1 de Diseño y desarrollo de videojuegos .
>>> nombre_compañero = 'Pablo'
>>> grado_compañero = 'Ingenieria electronica'
>>> grado_compañero
'Ingenieria electronica'
>>> curso_compañero = mi_curso
>>> curso_compañero
1
>>> curso_compañero = 3
>>> curso_compañero
3
>>> mi_curso
1
>>> 'El nombre de mi compañero es "{0}" y cursa {1}º de {2}.'.format(nombre_compañero, curso_compañero, grado_compañero)
'El nombre de mi compañero es "Pablo" y cursa 3º de Ingenieria electronica.'
>>> 