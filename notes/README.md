# Notes
Here is your wiki where you can document all stages of the project and save intermediate results and analyses.

## cSMTiser
The cSMTiser tool requires:<br>
* moses decoder + KenLM
* mgiza

### Installing Moses on Windows 10 using the Linux submodule
1. Set up a virtual environment (`csmt_env`).<br>
2. `sudo apt-get install`:<br>
   `g++` ✓  <br>
   `git` ✓ <br>
   `subversion` ✓ <br>
   `automake` ✓ <br>
   `libtool` ✓ <br>
   `zlib1g-dev` ✓ <br>
   `libicu-dev` ✓ <br>
   `libboost-all-dev` ✓ (Boost library)<br>
   `libbz2-dev` ✓ <br>
   `liblzma-dev` ✓ <br>
   `python-dev` ✓ <br>
   `graphviz` ✓     <br>
   `imagemagick` ✓ <br>
   `make` ✓ <br>
   `cmake` ✓ <br>
   `libgoogle-perftools-dev` (for tcmalloc) ✓  <br>
   `autoconf` ✓ <br>
   `doxygen` ✓ <br>

To compile with bare minimum of features:<br>
`./bjam -j4` ✓
   
### MGIZA
GIZA was developed by Qin Gao. It is an implementation of the popular GIZA++ word alignment toolkit to run multi-threaded on multi-core machines.<br>
`git clone https://github.com/moses-smt/mgiza.git` ✓ <br>
`cd mgiza/mgizapp`✓ <br>
`cmake .`✓ <br>
`make` ✓ <br>
`make install` ✓ <br>

TODO:<br>
Compiling MGIZA requires the Boost library. If your Boost library are in non-system directory, use the script to compile MGIZA:<br>
`manual-compile/compile.sh` ??? <br>
   
The MGIZA binary and the script merge_alignment.py need to be copied in you binary directory that Moses will look up for word alignment tools. This is the exact command I use to copy MGIZA to it final destination:<br>

`export BINDIR=~/workspace/bin/training-tools` workspace? bin/trainig-tools? <br> 
`cp bin/* $BINDIR/mgizapp`<br> 
`cp scripts/merge_alignment.py $BINDIR` <br>

MGIZA works with the training script `train-model.perl`. You indicate its use (opposed to regular GIZA++) with the switch `-mgiza`. The switch `-mgiza-cpus` NUMBER allows you to specify the number of CPUs. 
