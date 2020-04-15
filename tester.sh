#! /usr/bin/env bash
#test python implementation of rand48 family of functions
#vs the original C99 lib
gcc rand.c -o rand48_test
./rand48_test 2
echo 'c 2 test over'
python3 rand.py 2
echo 'python 2 test over'
./rand48_test 1
echo 'c 1 test over'
python3 rand.py 1
echo 'python 1 test over'

