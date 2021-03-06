# Notes
Here is your wiki where you can document all stages of the project and save intermediate results and analyses.

## Norma
Please note that Norma is only available as **a command-line utility** – there is no graphical interface. There are also **no pre-compiled binaries** at this point; you need to compile the source code yourself. Norma is written in **C++11**, though bindings for **Python 2** are provided as well.

At the moment, normalizers are restricted to work with **one word at a time**. That means they cannot take context into account or contract several words into one. 

### Dependencies

Needed for compilation:
* GCC >= 4.9 (GNU Compiler Collection) --> installed on both PC and mltgpu
* CMake >= 2.8.10  --> `cmake version 3.10.2` on PC, `cmake version 3.14.5` on mltgpu 
* Boost >= 1.54 --> `installed boost version: 1.65.1` on PC, not installed on mltgpu (!!!) <br>
 ...in particular these libraries: Filesystem, Program Options, Regex, System, Test
* pkg-config --> `0.29.1` on PC, `1.6.1`on mltgpu
* gfsm >= 0.0.16-1 and gfsmxl >= 0.0.15, available from http://kaskade.dwds.de/~moocow/mirror/projects/gfsm/<br>
...download the latest version of both and do the following in each folder:<br>
`cd gfsm-X.Y.Z`  (or wherever you extracted the distribution) <br>
`sh ./configure` <br>
`make` <br>
`make install` <-- I had to use `sudo make install` because of permission issues.<br> 
 
* GLib >= 2.0 ([instructions](https://programmer.help/blogs/ubuntu-18.04-install-glib-library-and-configure-codeblocks.html)) <br>

Optionally:<br>
* ICU >= 1.49
* Doxygen (for generating the documentation)
* Python 2 >= 2.7 and Boost::Python (for Python bindings/embeddings)

### Norma installation
`mkdir build` <br>
`cd build` <br>
`cmake <pathtosource>` --> NB: I used the path for the norma directory, not src, since the CMakeList file in src was [missing an important line](https://stackoverflow.com/questions/52255075/cmake-warning-dev-in-cmakelists-txt-no-cmake-minimum-required-command-is-pres) which was there in the CMakeList file in the norma directory.<br>
`make` <br>

## Norma running

**Interactive** mode is unavailable in the latest release of Norma, due to technical issues. You can currently only use **batch mode**:

In order to **normalize all words from a text file** that contains one wordform per line, just call:<br>

    normalize -c example/example.cfg -f example/fnhd_sample.txt <br>

...where:<br>
* `example.cfg` contains:<br>

`normalizers=RuleBased` #Specifies the normalizer to use <br>
`saveonexit=False` #Controls whether parameter files are saved when Norma exits. It defaults to False. <br>
`perfilemode=False` #Allows you to use Norma with many different parametrizations without changing the configuration file each time.<br>

`[Lexicon]`<br>
#Most normalizer components require a *target lexicon*. This is basically a list of valid word forms that the normalizers can generate, and is used to restrict the normalizer's output. A target lexicon requires two files to be given in the configuration file:<br> 
`fsmfile=bible_lexicon.fsm` # is the name of the lexicon file as a finite-state machine (see below).<br>
`symfile=bible_lexicon.sym` <br>
NB: A target lexicon doesn't seem to be required for the mapping-based normalizer, which makes sense!

`[RuleBased]`<br>
`rulesfile=example.RuleBased.rulesfile`<br>

...and:<br>
* `fnhd_sample.txt` contains a one token per line of words to normalize:<br>
\[...\]<br>
*dese*<br>
*wort*<br>
*spricht*<br>
*vnser*<br>
*liber*<br>
*here*<br>
\[...\]

For **training Norma on manually normalized data**, use:

    normalize -c example/example.cfg -f example/fnhd_train.txt -t --saveonexit

...where `fnhd_train.txt`is a word mapping file of this format:<br>
\[...\]<br>
*vnser	unser <br>
frawn	frauen <br>
lang	lang <br>
wainend	weinend <br>
vnd	und <br>
vastund	fastend* <br>
\[...\]

Flags:<br>
`-t` - causes Norma to perform training only, without generating any normalizations <br>
`--saveonexit` - is required (if not given in the config file) to save the trained parametrizations back to the parameter files <br>
`-h` - gives a list of all possible command-line options <br>

## cSMTiser
The cSMTiser tool requires:<br>
* moses decoder + KenLM
* mgiza

Running the cSMTiser tool consists of the following steps:
* configuring the normaliser
* training data preprocessing
* building the models and tuning the system
* running the final normaliser

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
   
In addition, you have to install some perl packages:

`cpan XML::Twig` ✓ <br>
`cpan Sort::Naturally` ✓ <br>

To compile Moses with bare minimum of features:<br>
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

NB: I ended up following [this person's](https://danieltakeshi.github.io/2014/11/19/brain-dump-successfully-installing-and-running-the-moses-statistical-machine-translation-system/) instructions for this instead. Let's see...

MGIZA works with the training script `train-model.perl`. You indicate its use (opposed to regular GIZA++) with the switch `-mgiza`. The switch `-mgiza-cpus` NUMBER allows you to specify the number of CPUs. 
