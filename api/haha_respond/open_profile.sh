#!/bin/bash
set -x
pyprof2calltree -i $@  -o tmp.prof
qcachegrind tmp.prof || kcachegrind tmp.prof
rm tmp.prof
