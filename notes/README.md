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
   
   ### MGIZA
   MGIZA was developed by Qin Gao. It is an implementation of the popular GIZA++ word alignment toolkit to run multi-threaded on multi-core machines.<br>
   `git clone https://github.com/moses-smt/mgiza.git` ✓ <br>
   `cd mgiza/mgizapp`✓ <br>
   `cmake .`✓ <br>
   `make` ✓ <br>
   `make install` ✓ <br>
   
   Compiling MGIZA requires the Boost library. If your Boost library are in non-system directory, use the script:<br>
   `manual-compile/compile.sh` ??? <br>
