################################################################################
# 
#	Syringenator : Software for the Syringenator robot
#
#	Copyright (c) 2019 by the authors. All rights reserved.
#
################################################################################

SHELL:=/bin/bash

srcdir:=src

ARDDIR:=$(srcdir)/controller
ARDLIBDIR:= $(srcdir)/sketchbook/libraries
PIDIR :=$(srcdir)/pi


CPPFLAGS:= --std=c++11 -g -I/usr/local/include/opencv4/

.PHONEY: all all_docs clean super_clean constants

all: constants all_docs


################################################################################
#                                CONSTANTS HEADERS
################################################################################


ARDCONST:= $(ARDLIBDIR)/constants/constants.h
PYCONST := $(PIDIR)/constants.py
CONSTIN := $(srcdir)/constants.in

constants: $(PYCONST)

boilerplate:="This file has been autogenerated, CHANGES MADE HERE WILL NOT PERSIST"

$(PYCONST): $(CONSTIN) Makefile
	install -d $(ARDLIBDIR)/constants
	echo -en "/**\t@file $(ARDCONST)\n " > $(ARDCONST)
	echo -e "##\t@file $(PYCONST)"  > $(PYCONST)
	HEADER=true                                        ;\
	cat $(CONSTIN) | while read -r line; do           \
		if $$HEADER; then                               \
			if test "$$line" == "%%"; then              \
				echo -e "*\t$(boilerplate)\n */\n\n" >> $(ARDCONST) ;\
				echo -e "#ifndef CONSTANTS_H\n#define CONSTANTS_H\n\n" >> $(ARDCONST) ;\
				echo -e "#\t$(boilerplate)\n"        >> $(PYCONST)  ;\
				HEADER=false                           ;\
			else                                        \
				echo -ne "*\t$$line\n " >> $(ARDCONST) ;\
				echo -e "#\t$$line"  >> $(PYCONST)     ;\
			fi                                          \
		elif test "$$line" != ""; then                  \
			words=($$line)                             ;\
			echo "#define $${words[0]} $${words[1]} ///< $${words[@]:2:100}" >> $(ARDCONST) ;\
			echo -e "## $${words[@]:2:100}\n$${words[0]} = $${words[1]}" >> $(PYCONST)  ;\
		fi   \
	done ;\
	echo -e "\n#endif // CONSTANTS_H\n\n" >> $(ARDCONST)


################################################################################
#                                DOCUMENTATION
################################################################################


docsource:=$(wildcard *.md)
docsource+=$(wildcard $(ARDDIR)/*)
docsource+=$(wildcard $(PIDIR)/*)
pdfman   :=refman.pdf

all_docs: $(pdfman)

$(pdfman): docs
	$(MAKE) -C latex all
	mv latex/refman.pdf ./$(pdfman)

# also produces latex file
docs: doxygen.cfg $(docsource) $(PYCONST)
	rm -fr docs latex $(pdfman)
	doxygen doxygen.cfg


################################################################################
#                                   DEMOS
################################################################################


demoImgCapCpp: $(PIDIR)/demoImgCap.cpp
	g++ $(CPPFLAGS) -o $@ $^ -lrealsense2 -lopencv_core -lopencv_highgui


################################################################################
#                                    CLEAN
################################################################################

cleanfiles:=imgCapCpp

clean:
	rm -fr *.pyc $(cleanfiles)

super_clean:
	rm -fr docs latex $(pdfman) $(ARDCONST) $(PYCONST)


