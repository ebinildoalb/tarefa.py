NÍCIO
    PEDIR um número
    resultado = esse número
    PEDIR a operação
    ENQUANTO a operação não for "=" e não for "OFF"
        PEDIR um número
        SE a operação for "+"
            resultado = resultado + número
        SENÃO SE a operação for "-"
            resultado = resultado - número
        SENÃO SE a operação for "*"
            resultado = resultado * número
        SENÃO SE a operação for "/"
            SE o número for 0
                MOSTRAR "não se pode dividir por zero"
            SENÃO
                resultado = resultado / número
        SENÃO
            MOSTRAR "operação inválida"
        PEDIR a operação
    FIM ENQUANTO
    SE a operação for "="
        MOSTRAR resultado
    MOSTRAR "calculadora desligada"
FIM 