#!/usr/bin/env python3
# encoding: utf-8

I = lambda x: x
"""lazy convenience wrapper for normal-order grossness"""
IF = lambda p: lambda a: lambda b: p(a)(b)()
K = T = lambda x: lambda y: x
KI = F = K(I)
M = lambda f: f(f)  # dynamic typing FTW
# M(M)

not_ = lambda p: p(F)(T)
and_ = lambda p: lambda q: p(q)(p)
or_  = lambda p: lambda q: p(p)(q)
beq  = lambda p: lambda q: p(q)(not_(q))
xor  = lambda p: lambda q: p(not_(q))(q)

n0 = lambda f: lambda x: x  # eta-equivalent to K(I)
n1 = lambda f: lambda x: f(x)

succ = lambda n: (lambda f: lambda x: f(n(f)(x)))
is0 = lambda n: n(K(F))(T)
eq = lambda a: lambda b: and_(is0(sub(a)(b)))(is0(sub(b)(a)))
n2 = succ(n1)
n3 = succ(n2)

add  = lambda a: lambda b: (lambda f: lambda x: b(f)(a(f)(x)))
add = lambda a: a(succ)

n5 = add(n3)(n2)

mul = lambda a: lambda b: lambda f: lambda x: a(b(f))(x)
# mul = lambda a: lambda b: a(add)(b)

n4 = mul(n2)(n2)
n6 = mul(n3)(n2)

decode = lambda n: n(lambda x: x+1)(0)
encode = lambda n: n0 if n<=0 else succ(encode(n-1))
encode = M(lambda f: lambda n: n0 if n<=0 else succ(f(f)(n-1)))

is0 = lambda n: n(K(F))(T)

# JS: f => M(g => f(x => g(g)(x)))
Z = lambda f: M(lambda g: f(lambda x: M(g)(x)))
# sample usage:
Z(lambda f: lambda n: 1 if n == 0 else n*f(n-1))
encode = Z(lambda f: lambda n: n0 if n<=0 else succ(f(n-1)))

V = lambda a: lambda b: lambda f: f(a)(b)
fst = lambda p: p(K)
snd = lambda p: p(KI)

pred = lambda n: fst(
	n(
	lambda p: V(snd(p))(succ(snd(p))))
	(V(n0)(n0)))

# so elegant 😻
sub = lambda a: lambda b: b(pred)(a)

fib = Z(lambda f: lambda n:
	IF(or_(is0(n)(is0(pred(n)))))
		(lambda: n1)
		(lambda: add(f(pred(n)))(f(sub(n)(n2)))))

fact = Z(lambda f: lambda n:
	IF(is0(n))
		(lambda: n1)
		(lambda: mul(n)(f(pred(n)))))
