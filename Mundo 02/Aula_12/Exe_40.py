n1 = float(input('Digite a primeira nota?'))
n2 = float(input('Digite a segunda nota?'))
nf = (n1 + n2) / 2
if nf >= 7.0:
    print('A média final foi ({}). O(A) aluno(a) está aprovado.'.format(nf))
elif nf >= 5.0 and nf <= 6.9:
    print('A nota final foi ({}). O(A) aluno(a) está de recuperação.'.format(nf))
elif nf < 5.0:
    print('A nota final foi ({}). O(A) aluno(a) está reprovado(a).')