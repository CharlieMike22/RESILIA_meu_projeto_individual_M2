
def buscar_candidatos(resultados, nota_entrevista, nota_teorico, nota_pratica, nota_soft):
    candidatos = []
    for candidato, notas in resultados.items():
        nota_e, nota_t, nota_p, nota_s = [int(n[1]) for n in notas.split("_")]
        if nota_e >= nota_entrevista and nota_t >= nota_teorico and nota_p >= nota_pratica and nota_s >= nota_soft:
            candidatos.append(candidato)

        return candidatos

nota_entrevista = int(input("Digite a nota mínima (de 0 a 9) desejada na entrevista: "))
nota_teorico = int(input("Digite a nota mínima (de 0 a 9) desejada no teste teórico: "))
nota_pratica = int(input("Digite a nota mínima (de 0 a 9) desejada no teste prático: "))
nota_soft = int(input("Digite a nota mínima (de 0 a 9) desejada na avaliação de soft skills: "))

resultados = {'Freddie Mercury': 'e8_t9_p8_s8',
         'Roger Waters': 'e8_t8_p7_s7',
         'Kurt Cobain': 'e5_t7_p6_s3',
         'Paul McCartney': 'e8_t7_p7_s8',
         'Klaus Meine': 'e9_t8_p9_s8'
}

