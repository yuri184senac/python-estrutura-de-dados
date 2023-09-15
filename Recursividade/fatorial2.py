def contagem_regressiva_recursiva(comeca_em: int=10, termina_em: int=0) -> int:
    print(comeca_em);

    if comeca_em <= termina_em:
        return comeca_em;

    return contagem_regressiva_recursiva(comeca_em-1);

if __name__ == "__main__":
    contagem_regressiva_recursiva(20)