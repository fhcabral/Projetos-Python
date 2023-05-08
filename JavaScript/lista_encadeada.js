function Node(valor){
    this.valor = valor
    this.proximo = null
}

function fila_dinamica(){
    this.primeiro = null
    this.ultimo = null

    this.estavazia = () => {this.primeiro == null}

    this.inserir = function(valor){
        const Novodado = new Node(valor)
        if(!this.primeiro){
            this.primeiro = Novodado
            this.ultimo = Novodado 
        }
        else
        {
            this.ultimo.proximo = Novodado
            this.ultimo = this.ultimo.proximo
        }
    }
    
    this.print = function(){
        const result = []
        let temp = this.primeiro
        while(temp){
            result.push(temp.valor)
            temp=temp.proximo
        }
        console.log(result)
    }
}

let array = new fila_dinamica()

array.inserir(2)
array.inserir(5)
array.inserir(3)
array.inserir(5)
array.inserir(6)
array.inserir(9)
array.print()