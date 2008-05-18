'''
PyFBUploader is a Python script for uploading Photos using the Facebook Platform
PyFBUploader is copyright 2008 Eric Stein

PyFBUploader is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2, or (at your option)
any later version.

PyFBUploader is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
License for more details.  The GPL version 2 is included as LICENSE.
'''

import os
import re
import md5
import sys
import math
import time

class Interact:
	#---------------------------
	#        INTERACTION
	#---------------------------

	def edit_file(self, filename) :
		self.runtty('vim', [filename])

	def edit_loop(self, filename, what) :
		m = what + ' unchanged\na)bort, c)ontinue, e)dit'

		contents = self.read_file(filename)

		while True :
			self.edit_file(filename)
			new = self.read_file(filename)

			if (new == contents) :
				print m
				response = sys.stdin.readline()
				if (len(response) > 1) :
					fc = response[0]
					if fc == 'a' :
						return False
					if fc == 'c' :
						return True
			else :
				return True

	# requires integer dict keys
	def choices_menu(self, t, d) :
		dg = 1;
		for k in d.keys() :
			if not type(k) == int :
				return None
			dg = max(dg, 1 + int(math.log(k)/math.log(10)))

		print t + ':'
		
		for k in d.keys() :
			kv = str(k)
			print kv.zfill(dg) + ': ' + d[k]

		sys.stdout.write('> ')
		
		n = int(sys.stdin.readline())
		if not d.has_key(n) :
			return None
		return n

	#--------------------------
	#           FILES
	#--------------------------

	def tree_replicate(self, file, destination) :
		a = ['-rp', file, destination]
		self.runtty('cp', a)

	def tree_destroy(self, file) :
		a = ['-rf', file]
		self.runtty('rm', a)

	# Note on locks: this works like a shared semaphore in C/C++; it is cooperative.
	# remove_lock can be run when acquire_lock failed - the pairing does not have
	# to be in the same process.

	# Create a lock file
	# Any other attempt to create this lock file will return False
	# until remove_lock is called
	def acquire_lock(self, filename) :
		try:
			fd = os.open(filename, os.O_EXCL | os.O_RDWR | os.O_CREAT)
			os.close(fd)
			return True
		except OSError:
			return False

	# Remove a lock file
	# Fails if there is no lock file to remove
	def remove_lock(self, filename) :
		try:
			os.unlink(filename)
			return True
		except OSError:
			return False

	def read_file(self, filename) :
		try:
			h = open(filename, 'r')
			s = h.read()
			h.close()
			return s
		except IOError:
			return False

	def write_file(self, filename, text) :
		try:
			h = open(filename, 'w')
			h.write(text)
			h.close()
			return True
		except IOError:
			return False

	def temp_file_name(self, basefilename) :
		if not os.path.exists(basefilename) :
			return basefilename
		i = 0
		while (os.path.exists(basefilename + str(i))) :
			i = i + 1
		return basefilename + str(i)

	#---------------------------
	#         EXECUTION
	#---------------------------

	def runtty(self, command, arguments=[]) :
		pid = os.fork()
		if pid == 0 :
			os.execvp(command, [command] + arguments)
		else :
			(pid, status) = os.wait()
			return status

	def run(self, command) :
		(i, o) = os.popen2(command)
		i.close()
		r = o.read()
		o.close()
		return r
