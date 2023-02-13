#!/usr/bin/env python

import unittest

from app4triqs import Toto, chain, sum_array, make_array, make_gf, print_gf
from h5 import *
from triqs.utility import mpi
import numpy as np

class test_toto(unittest.TestCase):

    def test_add(self):

        a=Toto(0)
        b=Toto(2)
        
        c=a+b
        self.assertEqual(c, b)


    def test_h5(self):
        a=Toto(0)
        with HDFArchive("f.h5",'w') as A:
            A["a"] = a
        with HDFArchive("f.h5",'r') as A:
            a_read = A["a"]
        self.assertEqual(a, a_read)
        

    def test_mpi(self):

        a=Toto(0)

        if mpi.is_master_node():
            a=Toto(1)
            mpi.bcast(a)

        self.assertEqual(a, Toto(1))

    def test_nda(self):

        a=np.array([(1,2),(2,3)])
        self.assertEqual(sum_array(a), 8)
        np.testing.assert_array_equal(make_array(2),a)

    def test_gf(self):

        g = make_gf()
        print(g.mesh)
        print_gf(2, g)
        # Error to test error message
        # print_gf(8,2)


class test_chain(unittest.TestCase):

    def test_chain(self):

        i = 111
        j = 222
        ij = chain(i,j)
        self.assertEqual(ij, 111222)

if __name__ == '__main__':
    unittest.main()
