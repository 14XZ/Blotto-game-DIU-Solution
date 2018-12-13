For confidentiality, this repository is released on Dec. 13th 2018 (more specifically, after Dec. 12th 2018).


# Blotto-game
Blotto Game simulation

Two algorithms are analysed and implemented:
1. Python verion of [^n2] rather than [authors' R implementation](https://github.com/dongquan11/Approx_discrete_Blotto) (just because I do not like R).
Just run 

```python3 test.py 100 100``` or 

```python3 test.py 100 110``` or

```python3 test.py 100 90```

and will write one more row in ```document.csv```.

2. Julia implementation forks (but modified of course) from [authors' implementation](github.com/Soben713/ColonelBlotto)[^n1] which reduces number of linear constraints in [^n3].
First run ```julia Colonel/blotto.jl``` and obtain files like ```distri_90_100a.csv```, ```distri_110_100b.csv```. Then run ```python3 test_julia_output.py``` to write one more row in ```document.csv```.

For results of baby tournament, just run ```python3 draw_table.py``` and will obtain files like ```output_table_90.csv```, ```output_table_110.csv```.


[^n1] [Vu, Dong Quan, Patrick Loiseau, and Alonso Silva. "Efficient computation of approximate equilibria in discrete Colonel Blotto games." (2018).](https://hal.archives-ouvertes.fr/hal-01787505/)

[^n2] [Faster and Simpler Algorithm for Optimal Strategies of Blotto Game](http://www.aaai.org/ocs/index.php/AAAI/AAAI17/paper/download/14980/13777)

[^n3] [Ahmadinejad, AmirMahdi, et al. "From Duels to Battlefields: Computing Equilibria of Blotto and Other Games." AAAI. 2016.
APA](http://www.aaai.org/ocs/index.php/AAAI/AAAI16/paper/download/12163/11607).
