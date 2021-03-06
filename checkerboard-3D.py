#!/usr/bin/env python

# two dimensional tight-binding checkerboard model

# Copyright under GNU General Public License 2010, 2012, 2016
# by Sinisa Coh and David Vanderbilt (see gpl-pythtb.txt)

from pythtb import * # import TB model class
import numpy as np
import pylab as plt

# define lattice vectors
lat=[[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]
# define coordinates of orbitals
# Pb at [0,0,0]; 3 I at [0.5,0,0] and permutations
orb=[[0.0,0.0,0.0],
     [0.0,0.0,0.5],
     [0.0,0.5,0.0],
     [0.5,0.0,0.0]
     ]

# make 3D dimensional tight-binding model (real and recip)
my_model=tb_model(3,3,lat,orb)

# set model parameters
delta=1.1
t=0.6

# set on-site energies
my_model.set_onsite([-delta,delta,delta,delta])
# set hoppings (one for each connected pair of orbitals)
# (amplitude, i, j, [lattice vector to cell containing j])
#my_model.set_hop(t, 1, 0, [0, 0, 0])
#my_model.set_hop(t, 1, 0, [1, 0, 0])
#my_model.set_hop(t, 1, 0, [0, 1, 0])
#my_model.set_hop(t, 1, 0, [1, 1, 0])
#my_model.set_hop(t, 1, 0, [0, 0, 1])
#my_model.set_hop(t, 1, 0, [1, 0, 1])
#my_model.set_hop(t, 1, 0, [0, 1, 1])
#my_model.set_hop(t, 1, 0, [1, 1, 1])

# Within 1st unit cell
my_model.set_hop(t, 0, 1, [0,0,0])
my_model.set_hop(t, 0, 2, [0,0,0])
my_model.set_hop(t, 0, 3, [0,0,0])

my_model.set_hop(t, 0, 1, [0,0,1])
my_model.set_hop(t, 0, 2, [0,1,0])
my_model.set_hop(t, 0, 3, [1,0,0])

#my_model.set_hop(t,0,0,[1,0,0])


# print tight-binding model
my_model.display()

#Visualise that which we have
(fig, ax) = my_model.visualize(0, 1)
plt.show()

# generate k-point path and labels
#path=[[0.0,0.0,0.0],[0.0,0.5,0.0],[0.5,0.5,0.0],[0.5,0.5,0.5],[0.0,0.0,0.0]]
#label=(r'$\Gamma $',r'$X$', r'$M$', r'$R$', r'$\Gamma $')
# Adopt full BZ route for Simple Cubic from: https://dx.doi.org/10.1016%2Fj.commatsci.2010.05.010
path=[  [0.0,0.0,0.0],
        [0.0,0.5,0.0],
        [0.5,0.5,0.0],
        [0.0,0.0,0.0],
        [0.5,0.5,0.5],
        [0.0,0.5,0.0],
        [0.5,0.5,0.0],
        [0.0,0.0,0.0]]
label=(r'$\Gamma $',r'$X$', r'$M$', r'$\Gamma $', r'$R$', r'$X$', r'$M$', r'$\Gamma $')


(k_vec,k_dist,k_node)=my_model.k_path(path,301)

print '---------------------------------------'
print 'starting calculation'
print '---------------------------------------'
print 'Calculating bands...'

# solve for eigenenergies of hamiltonian on
# the set of k-points from above
evals=my_model.solve_all(k_vec)

# plotting of band structure
print 'Plotting bandstructure...'

# First make a figure object
fig, ax = plt.subplots()

# specify horizontal axis details
ax.set_xlim([0,k_node[-1]])
ax.set_xticks(k_node)
ax.set_xticklabels(label)
for n in range(len(k_node)):
  ax.axvline(x=k_node[n], linewidth=0.5, color='k')

# plot bands
for n in range(2):
  ax.plot(k_dist,evals[n])
# put title
ax.set_title("Towards a 3D band structure")
ax.set_xlabel("Path in k-space")
ax.set_ylabel("Band energy")
# make an PDF figure of a plot
fig.tight_layout()

plt.show() # Show figure + wait to be dismissed

fig.savefig("checkerboard-3D_band.pdf")

print 'Done.\n'
