#!/usr/bin/env python3
print([
    exec('G=2;J=3;K=5;O=8;H=13;L=21;K=34;N=55;I=89'),
    eval(''.join('*->'.join([
        chr(int(i) + 70) for i in str(
            eval(
                ord(''' ''').__str__(*[]) +
                '---{0}---{1}---{2}---'.format(*("~+~|" * 3).split('|')) +
                __import__(*('math', )).pi.__str__()[2:]))
    ]).split('>')))
][1])
