from ArvoreBinariaSemImplementacao import ArvoreBinaria

arv = ArvoreBinaria(40)
arv.addEsq(32)
arv.addDir(27)
arv.descerEsquerda()
print('Cursor: ', arv.getCursor())
arv.addDir(16)
arv.descerDireita()
print('Cursor: ', arv.getCursor())
arv.addEsq(10)
arv.addDir(20)
arv.resetCursor()
arv.descerDireita()
print('Cursor: ', arv.getCursor())
arv.addDir(55)
arv.descerDireita()
print('Cursor: ', arv.getCursor())
arv.addEsq(8)

print('Busca:', arv.busca(578))

arv.preordem()
print()
arv.emordem()
print()
arv.posordem()
#print(arv.__dict__)
print()
print(arv.go(116))
arv.preordem()
print('Cursor: ', arv.getCursor())
print(arv.removeEsq())
arv.preordem()
