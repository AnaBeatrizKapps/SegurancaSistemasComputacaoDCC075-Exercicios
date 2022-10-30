# Algoritmo RBAC
# Para esse algoritmo foi utilizado a biblioteca: https://pypi.org/project/py-rbac/

from rbac import RBAC

class Article():
    """docstring for Article."""

def __init__(self, id, author):
    self.id = id
    self.author = author

rbac = RBAC()

# Criando a ROLE e permitindo somente 1 pessoa para essa função
jr_editor = rbac.create_role('jr_editor', max_subjects=1)
# Designando 10 editores para essa função e jr_editor é uma função abaixo da função editor
editor = rbac.create_role('editor', children=jr_editor, max_subjects=10)
# a função principal foi designada para somente 1 pessoa e não herda as permissões de seus filhos
chief = rbac.create_role('chief', children=(jr_editor, editor), inherit=False, max_subjects=1)

# objeto artigo é definido como entrada para o RBACDomain
article = rbac.create_domain(Article)

# criando as permissões
create = rbac.create_permission('c')
read = rbac.create_permission('r')
update = rbac.create_permission('u')
delete = rbac.create_permission('d')

# Atribuindo as permissões de criar e ler para o jr-editor
jr_editor.add_permission((create, read), article)
# Só poderá remover o que escreveu
# match_domain_prop indica a propriedade de instância do artigo
jr_editor.add_permission(delete, article, match_domain_prop='author')
editor.add_permission(create, article)

# definindo john como jr
john = rbac.create_subject(1)
john.authorize(jr_editor)

# trava a configuração do rbac
# isso valida toda a estrutura da nossa configuração
assert rbac.lock() is None

# ou desbloqueia para adicionar mais 2 sujeitos
rbac.unlock()
jack = rbac.create_subject(3)
jack.authorize(editor)
brad = rbac.create_subject(4)
brad.authorize(chief)

rbac.lock()

some_article = Article(28372, 1)
# júnior tentando deletar um artigo
# a biblioteca corresponderá ao id do john que é 1 com o autor do artigo e
# permite a operação se eles corresponderem.
assert rbac.go(1, some_article, delete) is None