#
# IchiiDev, 2023
# Project Name: snippets-manager
# File Name: Makefile
# License: MIT
#

NO_COMMAND_MESSAGE	=	"Nothing to do here, please type 'make install' or 'make save'"

all:
	echo $(NO_COMMAND_MESSAGE)

install:
	mkdir -p snippets
	python src/installation/main.py

save:
	python src/saving/main.py

.SILENT: all install save
.PHONY: all install save
