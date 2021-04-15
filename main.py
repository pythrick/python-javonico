"""
Criar os seguintes TADs:
• Palestra:
1.Atributos: tema, descrição
2.Método: imprimir
• Palestrante:
1. Atributos:código, nome, palestras (do tipoPalestra)
2. Método: imprimir
• Evento:
1. Atributos:
§ palestras(vetor de Palestras)
§ palestrantes(vetor de Palestrante)
2.Métodos:
§ addPalestra: adiciona uma palestra na última posição do vetor de palestras
§ obterPalestra: que verifica se uma dada palestra está presente no vetor de palestras
§ addPalestrante: adiciona uma palestrante na última posição do vetor de palestrante
§ obterPalestrante: que verifica se um dado palestrante está presente no vetor de palestrante
§ Imprimir todos os dados
• Crie os métodos gets e sets
"""

from python_javonico.models.palestra import Palestra
from python_javonico.models.palestrante import Palestrante
from python_javonico.models.evento import Evento


if __name__ == '__main__':
    palestra_1 = Palestra(codigo="1", tema="Palestra massa!", descricao="Palestra de exemplo")
    palestrante_1 = Palestrante(codigo="1", nome="João", palestras=[palestra_1])

    palestra_2 = Palestra(codigo="2", tema="Nova palestra", descricao="Palestra arroz com feijão")
    palestrante_2 = Palestrante(codigo="2", nome="João", palestras=[palestra_2])

    evento = Evento()
    evento.add_palestra(palestra_1)
    evento.add_palestra(palestra_2)
    evento.add_palestrante(palestrante_1)
    evento.add_palestrante(palestrante_2)

    evento.imprimir()
