# $Id: 155_err_sdp_bad_syntax.py 369517 2012-07-01 17:28:57Z file $
import inc_sip as sip
import inc_sdp as sdp

sdp = \
"""
v=
o=
s=
c=
t=
a=
"""

pjsua_args = "--null-audio --auto-answer 200"
extra_headers = ""
include = [ "Warning: " ]	# better have Warning header
exclude = []

sendto_cfg = sip.SendtoCfg("Bad SDP syntax", pjsua_args, sdp, 400,
			   extra_headers=extra_headers,
			   resp_inc=include, resp_exc=exclude) 
