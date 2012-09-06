#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  basic.py
#  part of s87lib
#  
#  Copyright 2012 Silvano Wegener
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 


import sys, os


def makeString(*strings, **keyWordArgs):
	try:
		joiner = keyWordArgs['joiner']
	except KeyError:
		joiner = ' '
	return joiner.join(strings)


class Help(object):
	def __init__(self):
		self.parameters = {}
		self.addParameter('--help','this info.')
		self.description = 'no description available'


	def addParameter(self, parameter, description='no description available.'):
		if parameter == '' or self.existsParameter(parameter):
			return False
		self.parameters[parameter] = description


	def addDescription(self, description):
		self.description = description


	def existsParameter(self, parameter):
		try:
			check =  self.parameters[parameter]
			return True
		except KeyError:
			return False


	def printHelp(self):
		topLine = os.path.split(sys.argv[0])[1] + ' - help and description.'
		print topLine
		print '-'*len(topLine)
		print 'Description:\n ' + self.description +'\n'
		print 'Parameters:'
		parametersMaxLength = self.longestParameterLength()
		for parameter in self.parameters.keys():
			infoLine = makeString(' ',parameter.ljust(parametersMaxLength, ' '),'|',self.parameters[parameter])
			print infoLine
		print '-'*len(topLine)


	def longestParameterLength(self):
		parameterLength = 0
		for parameter in self.parameters.keys():
			if len(parameter) > parameterLength:
				parameterLength = len(parameter)
		return parameterLength



