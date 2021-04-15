#
#
# main() será executado quando você chamar essa ação
#
# @param As ações do Cloud Functions aceitam um único parâmetro, que deve ser um objeto JSON.
#
# @return A saída dessa ação, que deve ser um objeto JSON.
#
#
import numpy as np
import sys

def main(dict):
    score = int(np.random.normal(500, 200))
    while 1 > score > 999:
        score = int(np.random.normal(500, 200))
    return { 
        'body': {
            'score': score 
        }
    }
