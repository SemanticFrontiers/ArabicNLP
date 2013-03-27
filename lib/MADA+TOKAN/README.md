MADA+TOKAN Installation Instructions
=

Prerequisites
-

You should 
function install_svmtool() {
    echo "Installing SVMTool"
    cd SVMTool-1.3.1
    perl Makefile.PL
    make
    export SVMTOOLSHOME=`pwd`
    export PERL5LIB=$PERL5LIB:$SVMTOOLSHOME/lib
    cd ..
}

function install_srilm () {
    echo "Installing SRILM"
    cd srilm
    export SRILM=`pwd`
    export SRIHOME=`pwd`
    
    make World
    export MANPATH=$SRILM/man:$MANPATH

    # TODO: make this line more general
    export PATH=$SRILM/bin/macosx:$SRILM/bin:$PATH
    ln -s bin/macosx/disambig bin/disambig

    cd ..
}

function install_sama() {
    export XAMADIR=`pwd`/sama_3_1/SAMA-3.1/lib/SAMA_DB/v3_1
    export XAMAVERSION="SAMA3.1"
}
function install_mada() {
    echo "Installing MADA"
    cd MADA-3.2
    export MADAHOME=`pwd`
    export PERL5LIB=$PERL5LIB:$MADAHOME
    perl INSTALL.pl madahome=$MADAHOME srihome=$SRIHOME svmhome=$SVMTOOLSHOME xamadir=$XAMADIR xamaversion=$XAMAVERSION
    cd ..
}

function append_zshrc() {
    echo "export SVMTOOLSHOME=$SVMTOOLSHOME" >> ~/.zshrc
    echo "export PERL5LIB=$PERL5LIB" >> ~/.zshrc
    echo "export PATH=$PATH" >> ~/.zshrc
    echo "export MANPATH=$MANPATH" >> ~/.zshrc
    echo "export XAMADIR=$XAMADIR" >> ~/.zshrc
    echo "export XAMAVERSION=$XAMAVERSION" >> ~/.zshrc
    echo "export MADAHOME=$MADAHOME" >> ~/.zshrc
    echo "export PERL5LIB=$PERL5LIB" >> ~/.zshrc
}
    
install_svmtool
install_srilm
install_sama
install_mada
