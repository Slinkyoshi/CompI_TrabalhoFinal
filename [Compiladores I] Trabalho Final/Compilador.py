
from AbrirArquivo import carregarArquivo
from AnalisadorLexico import AnalisadorLexico
from AnalisadorSintatico import AnalisadorSintatico
from AnalisadorSemantico import AnalisadorSemantico
from TabelaDeSimbolos import TabelaDeSimbolos
from GrafoSintatico import grafoSintatico

def main():

    lista = carregarArquivo()
    token, string = AnalisadorLexico().analisar(lista)
    tabelaDeSimbolos = TabelaDeSimbolos()
    
    AnalisadorSintatico(token, string, tabelaDeSimbolos).analisar()
    AnalisadorSemantico(token, string, tabelaDeSimbolos.getTabela()).analisar()
    tabelaDeSimbolos.mostrarTabela()
    print ("\nCODIGO COMPILADO SEM ERROS")
    grafoSintatico()
    


main()



