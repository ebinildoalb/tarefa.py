
INÍCIO
    PEDIR o primeiro número 
    PEDIR o segundo número
    PEDIR a operação
 
    SE a operação for "+"
        resultado = primeiro + segundo
    SENÃO SE a operação for "-"
        resultado = primeiro - segundo
    SENÃO SE a operação for "*"
        resultado = primeiro * segundo
    SENÃO SE a operação for "/"
        SE o segundo número for 0
            MOSTRAR "não se pode dividir por zero"
        SENÃO
            resultado = primeiro / segundo
    SENÃO
        MOSTRAR "operação inválida"
 
    MOSTRAR resultado
FIM