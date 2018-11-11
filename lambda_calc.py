#!/usr/bin/env python3
# encoding: utf-8

I = lambda x: x
K = lambda x: lambda y: x
KI = K(I)

V = lambda a: lambda b: lambda f: f(a)(b)
fst = lambda p: p(K)
snd = lambda p: p(KI)

n0 = KI
n1 = lambda f: lambda x: f(x)
succ = lambda n: lambda f: lambda x: f(n(f)(x))
encode = lambda n: n0 if n <= 0 else succ(encode(n-1))
decode = lambda n: n(lambda x: x+1)(0)
pred = lambda n: fst(n( lambda p: V(snd(p))(succ(snd(p))) )(V(n0)(n0)))
# pred = lambda n: n(
# lambda p: (lambda a: lambda b: lambda f: f(a)(b))(p(lambda x: lambda y: y))((lambda n: lambda f: lambda x: f(n(f)(x)))(p(lambda x: lambda y: y)))
# )(lambda f: f(lambda f: lambda x: x)(lambda f: lambda x: x))(lambda x: lambda y: x)
pred = lambda n: n(
lambda p: (lambda f: f(p(lambda x: lambda y: y))((lambda n: lambda f: lambda x: f(n(f)(x)))(p(lambda x: lambda y: y))))
)(lambda f: f(lambda f: lambda x: x)(lambda f: lambda x: x))(lambda x: lambda y: x)

add = lambda a: lambda b: a(succ)(b)
sub = lambda a: lambda b: b(pred)(a)
mul = ...
div = ...
pow = lambda a: lambda b: b(a)
