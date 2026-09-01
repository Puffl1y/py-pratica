# Controle de alunos e notas
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"

alunos = input("Digite os nomes dos alunos separados por vírgula: ").split(",")
alunos_objetos = []
for nome in alunos:
    alunos_objetos.append(Aluno(nome, []))

for aluno in alunos_objetos:
    print(f"\nAdicionando notas para o aluno {aluno.nome}:")
    while True:
        nota = input("Digite uma nota (ou 'sair' para encerrar): ")
        if nota.lower() == 'sair':
            break
        try:
            nota = float(nota)
            aluno.adicionar_nota(nota)
        except ValueError:
            print("Por favor, digite um número válido.")

for aluno in alunos_objetos:
    print(f"\nAluno: {aluno.nome}")
    print(f"Notas: {aluno.notas}")
    print(f"Média: {aluno.calcular_media():.2f}")
    print(f"Situação: {aluno.verificar_aprovacao()}")