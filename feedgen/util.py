#!/bin/env python
# -*- coding: utf-8 -*-
'''
	feedgen.util
	~~~~~~~~~~~~

	This file contains helper functions for the feed generator module.

	:copyright: 2013, Lars Kiesow <lkiesow@uos.de>
	:license: FreeBSD and LGPL, see license.* for more details.
'''



def ensure_format(val, allowed, required, allowed_values={}):
	'''Takes a dictionary or a list of dictionaries and check if all keys are in
	the set of allowed keys, if all required keys are present and if the values
	of a specific key are ok.

	:param val: Dictionaries to check.
	:param allowed: Set of allowed keys.
	:param required: Set of required keys.
	:param allowed_values: Dictionary with keys and sets of their allowed values.
	:returns: List of checked dictionaries.
	'''
	if not val:
		return None
	# Make shure that we have a list of dicts. Even if there is only one.
	if not isinstance(val, list):
		val = [val]
	for elem in val:
		if not isinstance(elem, dict):
			raise ValueError('Invalid data (value is no dictionary)')
		if not set(elem.keys()) <= allowed:
			raise ValueError('Data contains invalid keys')
		if not set(elem.keys()) >= required:
			raise ValueError('Data contains not all required keys')
		for k,v in allowed_values.iteritems():
			if elem.get(k) and not elem[k] in v:
				raise ValueError('Invalid value for %s' % k )
	return val