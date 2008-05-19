'''
PyFBUploader is a Python script for uploading Photos using the Facebook Platform
PyFBUploader is copyright 2008 Eric Stein

PyFBUploader is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2, or (at your option)
any later version.

Bash is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
License for more details.  The GPL version 2 is included as LICENSE.

$Id$
'''

import pickle
import os.path

def getfile() :
	return os.path.join(os.path.expanduser('~'), '.pyfbuploader')

def getsession() :
	try:
		f = open(getfile(), 'r')
		s = pickle.load(f)
		f.close()
		return s
	except:
		return None

def setsession(s) :
	f = open(getfile(), 'w')
	pickle.dump(s, f)
	f.close()
