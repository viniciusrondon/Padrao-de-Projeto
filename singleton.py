class BancoDeDadosSingleton: # uma classe que conecta ao banco de dados da aplicacao
    _instancia = None
    def __new__(cls): # metodo de criacao 
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.conexao = cls._criar_conexao()
        return cls._instancia
    
    @staticmethod
    def _criar_conexao():
        print("Conectando ao banco de dados...")
        return "Conexão ao banco"
    

# Ambas as  instâncias vão usar a mesma conexão
db1 = BancoDeDadosSingleton()
db2 = BancoDeDadosSingleton()
print(db1 is db2) # True
    


