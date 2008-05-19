# PyFBUploader is a Python script for uploading Photos using the Facebook Platform
# PyFBUploader is copyright 2008 Eric Stein
# 
# PyFBUploader is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
# 
# Bash is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.  The GPL version 2 is included as LICENSE.
# 
# $Id$

prefix := /usr
bindir := $(prefix)/bin
libdir := $(prefix)/lib
sharedir := $(prefix)/share
libdir_ := $(libdir)/pyfbuploader

install: fbupload.install interact.py session.py
	mkdir -m 755 -p \
		$(bindir) \
		$(libdir_)
	install -m 755 fbupload $(bindir)
	install -m 644 *.py $(libdir_)

uninstall:
	-rm -rf \
		$(libdir_) \
		$(bindir)/fbuploader

clean:
	rm -f fbupload.install
