# -*- coding: utf-8 -*-
import sha512_crypt


def test_roundtrip():
    hashed = sha512_crypt.encrypt("abc")
    assert sha512_crypt.verify("abc", hashed)


def test_verify_passlib():
    hashed = "$6$rounds=656000$Ykk6fjI2sU3/uprV$Z6yV/9Z741lfroSSzB9MwxSRnGeI9Z74hBkgNsHuojQJxZ9XjPkHg9jqqGLvWZ586wqnSSx5vrXZdhrMSZZE4/"  # NOQA
    assert sha512_crypt.verify("abc", hashed)


def test_verify_fail():
    hashed = "$6$rounds=656000$Ykk6fjI2sU3/uprV$Z6yV/9Z741lfroSSzB9MwxSRnGeI9Z74hBkgNsHuojQJxZ9XjPkHg9jqqGLvWZ586wqnSSx5vrXZdhrMSZZE4"  # NOQA
    assert not sha512_crypt.verify("abc", hashed)
