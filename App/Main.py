class Main:
    pass

print("Testando projeto")

from Cliente import  Cliente

c1= Cliente("Cacau", "11 40028922")
conta=Conta(c1.get_nome(), 1222)

conta.deposita(100)
conta.saque(50)
conta.extrato()
