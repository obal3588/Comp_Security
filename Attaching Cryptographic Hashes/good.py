#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ���� h�F:��N���Yjr��Q'Bz5��?,�� 8>{Z�9t��Zݯ��&γ��zZ���2�Z�z?�1,h�Ƙ'���}��l�_KQ�A%���
����k��:aeh�Ds���֠�}��u;
"""
from hashlib import sha256

if ((sha256(blob).hexdigest()) == "d313b30454ac0d5df660ecd0ffeb0eb559699e1332c14575af24ba7656582926") :
	print "I come in peace!"
else :
        print "Prepare to be destroyed!"
