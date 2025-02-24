 ---
 Tags: #fleeting 
 Description: Live do PycodeBr sobre padrão de projeto
 Theme:[[Mestrado ITA 👨🏽‍🏫]], [[Ambiente virtual -  venv]], 
## ID: 20250223200951
---

# Descrição breve: 

## Entendendo as categorias de padrões de projeto, segundo GoF

#### GoF (Gang of Four)

Para esse estudo, vamos explorar um pouco dos padrões de projeto descritos no livro `Padrões de projeto: Solucões reutilizáveis de software orientado em objeto - 1994`.

O livro lista o total de 23 padrões de projeto, onde os autores classificam todos os padrões em 3 categorias.

![[Pasted image 20250223202358.png]]

### Padrões Criacionais

1. **Singleton** Garante uma única instância de uma classe.
2. **Factory Method**: Define uma interface para criar objetos, mas permite que subclasses decidam qual classe instanciar.
3. **Abstract Factory**: Fornece uma interface para criar famílias de objetos relacionados.
4. **Builder**: Separa a construção de um objeto complexo de sua representação.
5. **Prototype**: Permite a criação de novos objetos copiando um protótipo.

O termo Criacionais se refere ao fato desses padrões **fornecerem técnicas para possibilitar a criação objetos e instâncias de objetos**, desta forma construir construtores de objetos.

### Padrões Estruturais

1. **Adapter:** Converte a interface de uma classe em outra interface esperada pelo cliente.
2. **Bridge:** Separa uma abstração de sua implementação.
3. **Composse:** Compões objetos em estruturas de árvores para representar hierarquias parte-todo.
4. **Decorador:** Adiciona responsabilidade a objetos dinamicamente.
5. **Facade:** Fornece uma interface simplificada para um subsistema complexo.
6. **Flyweight**: Reduz o custo de criação de muitos objetos semelhantes.
7. **Proxy:** Fornece um substituto ou espaço reservado para outro objeto.
   
Padrões que se propõe a explicar **como estruturar o código por inteiro., fazendo uma camada se comunicar com a outra.**

### Padrões comportamentais 

Estes são padrões mais complexos e se propões a explicar como suas classes irão se comportar ao longo da vida útil do projeto.

1. **Chain of Responsibility**: Passa uma solicitação ao longo de uma cadeia de manipuladores.
2. **Command**: Encapsula uma solicitação como um objeto.
3. **Interpreter**: Define uma representação gramatical para uma linguagem e um interpretador para interpretá-la.
4. **Iterator**: Fornece uma maneira de acessar sequencialmente os elementos de uma coleção.
5. **Mediator**: Define um objeto que encapsula como um conjunto de objetos interage.
6. **Memento**: Captura e externaliza o estado interno de um objeto.
7. **Observer**: Define uma dependência um-para-muitos entre objetos.
8. **State**: Permite que um objeto altere seu comportamento quando seu estado interno muda.
9. **Strategy**: Define uma família de algoritmos, encapsula cada um e os torna intercambiáveis.
10. **Template Method**: Define o esqueleto de um algoritmo em uma operação.
11. **Visitor**: Permite adicionar novas operações a uma estrutura de objetos sem alterar suas classes.
### Esses são todos os padrões de projeto existentes?

Absolutamente, não. Os 23 padrões de projeto citados no livro em questão, são apenas alguns dos muitos outros padrões de projeto existentes.

Quando nos referimos à padrões de projeto, estamos falando de um conceito muito amplo, que inclusive, transcende a área da programação e criação de software.

Outros livros famosos que podemos citar, inclusive alguns mais modernos:

1. **"Clean Code: A Handbook of Agile Software Craftsmanship"** (Robert C. Martin):
    - Focado em boas práticas de escrita de código limpo e legível.
    - Aborda princípios como SOLID e TDD (Test-Driven Development).
2. **"Refactoring: Improving the Design of Existing Code"** (Martin Fowler):
    - Ensina técnicas para melhorar o design de código existente.
    - Inclui exemplos práticos de refatoração.
3. **"Domain-Driven Design: Tackling Complexity in the Heart of Software"** (Eric Evans):
    - Introduz o conceito de Domain-Driven Design (DDD).
    - Focado em alinhar o design de software com o domínio do negócio.
4. **"Patterns of Enterprise Application Architecture"** (Martin Fowler):
    - Aborda padrões para aplicações empresariais, como MVC, Active Record e Data Mapper.
5. **"Design Patterns Explained: A New Perspective on Object-Oriented Design"** (Alan Shalloway e James R. Trott):
    - Explica os padrões do GoF de forma mais acessível, com exemplos práticos.
6. **"Head First Design Patterns"** (Eric Freeman e Elisabeth Robson):
    - Um livro didático e visual que explica os padrões de projeto de forma descontraída.
7. **"The Pragmatic Programmer"** (Andrew Hunt e David Thomas):
    - Um guia prático para se tornar um programador mais eficiente e eficaz.
    - Aborda princípios como DRY (Don't Repeat Yourself) e KISS (Keep It Simple, Stupid).
8. **"Building Microservices"** (Sam Newman):
    - Um guia completo para projetar e implementar microsserviços.
9. **"Implementing Domain-Driven Design"** (Vaughn Vernon):
    - Complementa o livro de Eric Evans com exemplos práticos e detalhados.
10. **"Continuous Delivery"** (Jez Humble e David Farley):
    - Focado em práticas para entregar software de forma rápida e confiável.
11. **"Site Reliability Engineering"** (Google):
    - Introduz conceitos de engenharia de confiabilidade (SRE) usados no Google.
12. **"Release It!"** (Michael T. Nygard):
    - Aborda padrões e anti-padrões para sistemas em produção.
13. "Machine Learning Design Patterns: Solutions to Common Challenges in Data Preparation, Model Building, and MLOps"

## Primeiro temos um problema e então buscamos qual padrão ira nos ajudar a resolver

### **Padrões Arquiteturais**

- Separa a lógica de negócios (Model), a interface do usuário (View) e o controle (Controller).
- Amplamente usado em frameworks como Django, Ruby on Rails e Spring.

1. **MVVM (Model-View-ViewModel)**:
    - Similar ao MVC, mas focado em aplicações com interfaces ricas (como aplicativos móveis e desktop).
    - Usado em frameworks como Angular e Xamarin.
2. **Microservices**:
    - Divide uma aplicação em serviços independentes e escaláveis.
    - Popular em arquiteturas modernas de sistemas distribuídos.
3. **CQRS (Command Query Responsibility Segregation)**:
    - Separa operações de leitura (Query) e escrita (Command) em modelos diferentes.
    - Útil para sistemas com alta complexidade de leitura/escrita.
4. **Event Sourcing**:
    - Armazena o estado de uma aplicação como uma sequência de eventos.
    - Permite reconstruir o estado atual a qualquer momento.
5. **Service Locator**:
    - Centraliza o acesso a serviços em uma aplicação.
    - Alternativa ao Dependency Injection em alguns cenários.
6. **Repository**:
    - Abstrai o acesso a dados, fornecendo uma interface simples para operações de persistência.
    - Comum em aplicações que usam ORMs (Object-Relational Mappers).
7. **Unit of Work**:
    - Gerencia transações e rastreia alterações em objetos durante uma operação.
    - Frequentemente usado com o padrão Repository.

### **Padrões de Integração**

.....

# <font color="#92cddc">Singleton</font>

<font color="#92cddc">Soluciona de maneira simples a conexão com o banco de dados, evitando múltiplas conexões. </font>

Problema: 

Em sistemas grandes, pode ser necessário ter **uma única instância de um recurso compartilhado** ao longo de toda a aplicação, como uma conexão com o banco de dados, um gerenciador de configuração ou uma sessão global. Sem o Singleton, você poderia acabar criando múltiplas instâncias desse recurso, o que pode levar a problemas de **desempenho** e **inconsistência de dados.**

Solução:

O Singleton resolve isso garantindo que uma classe tenha apenas **uma instância global** acessível durante a execução do programa. O uso de uma instância única evita a criação desnecessária de objetos e assegura que o recurso compartilhado seja acessado de maneira consistente.

Imagine um sistema onde você precisa garantir que **somente uma conexão de banco de dados** seja usada durante a execução. Se a classe `BancoDeDados` não seguir o padrão Singleton, seria possível criar várias instâncias da classe, e cada uma teria sua própria conexão com o banco de dados, o que resultaria em **desempenho ruim** e **conflitos de conexão**.

## <font color="#92cddc">Prática </font>

```
class BancoDeDadosSingleton: 
	_instancia = None 
	def __new__(cls): 
		if cls._instancia is None: 
			cls._instancia = super().__new__(cls) 
			cls._instancia.conexao = cls._criar_conexao() 
		return cls._instancia 
		
	@staticmethod 
	def _criar_conexao(): 
		print("Conectando ao banco de dados...") 
		return "Conexão ao banco" 


# Ambas as instâncias vão usar a mesma conexão 
db1 = BancoDeDadosSingleton() 
db2 = BancoDeDadosSingleton() 
print(db1 is db2) # True
```

- Foi criada uma classe que conecta com o banco de dados e o que esta dentro desta classe é o método que cria a conexão. 
- `__new__`  : método de criação do python.
	- quando instancia a conexão com o banco de dados ele chama a classe 

## <font color="#92cddc">Por que usar ?</font>

- Evita múltiplas conexões desnecessárias com o banco de dados.
- Garante que o sistema compartilhe uma instância de recurso, evitando sobrecarga e inconsistência.

# <font color="#c3d69b">Factory Method</font>

Problema:

Em sistemas orientados a objetos, muitas vezes você precisa criar instâncias de **Diferentes classes** de acordo com condições específicas. Se você tiver uma lógica de criação dispersa ao longo do código, **isso violaria o principio da coesão** e tornaria o código mais difícil de manter. Além disso, se novas classes de carros forem adicionadas, o código de criação também precisaria ser alterado em vários lugares.

Solução: 

O <font color="#c3d69b">Factory Method delega a criação do objetos para subclasses</font>, permitindo que o<font color="#c3d69b"> processo de instaciamento seja encapsulado em uma única função</font>, sem que o código do cliente precise se preocupar com o tipo exato de objeto sendo instanciado.

Vamos supor que em um sistema você tenha diferentes tipos de carro, como `carro esportivo, carro popular e carro de luxo`, e deseja instancia-los de maneira centralizada. Se o código de criação fosse espalhado por varias partes do código, isso **poderia violar o princípio de aberto/fechado**, dificultando a adição de novos tipos de carros sem modificar várias partes do sistema.


```
class Carro: 
	def dirigir(self): 
		pass 

class CarroEsportivo(Carro): 
	def dirigir(self): 
		return "Dirigindo um carro esportivo!" 
		
class CarroPopular(Carro): 
	def dirigir(self): 
		return "Dirigindo um carro popular!" 
		
class CarroFactory: 
	def criar_carro(self, tipo): 
		if tipo == 'esportivo': 
			return CarroEsportivo() 
		elif tipo == 'popular': 
			return CarroPopular() 
		else: 
			raise ValueError("Tipo de carro não reconhecido.") 
			
# Teste 
factory = CarroFactory() 

carro = factory.criar_carro('esportivo') 
print(carro.dirigir()) 

carro = factory.criar_carro('popular') 
print(carro.dirigir())
```

1. Dentro da primeira classe carro `class Carro` tem a primeira função chamada `dirigir` com um comando `pass`:
	1. `pass` é um método para declarar uma função vazia em python
	2. É possível usar `...` que tem a mesma função.
2. As classes `CarroEsportivo` e `CarroPopular` herdam a classe ``Carro`` que por sua vez terão sua função`` dirigir``
	1. quando foi declarada a classe `Carro` ainda não se sabia como ela seria lidada(esportivo, popular,...) e por isso é necessária a alteração desta função em cada classe nova.
3. <font color="#c3d69b">O Padrão Factory centraliza a logica desse processo:</font>
	1. Para cada caso a classe `CarroFactory` respondera para o usuário.
4. Se for necessário criar um novo tipo de carro `suv`, por exemplo, bastaria criar uma nova classe  nova classe `CarroSuv`, e dentro de `CarroFactory` incluir um novo tipo.


> Em suma, é criar uma classe que cria outras classes.


# <font color="#d99694">Abstract Factory</font>

**Problema:** 

Em sistemas mais complexos, você pode precisar de famílias de objetos que precisam ser criados de forma consistente, mas que podem ter diferentes variantes. Por exemplo, ao criar carros, você pode querer diferentes variantes de carros esportivos ou populares, mas cada tipo de carro precisa de interiores e rodas diferentes. Criar esses objetos de forma dispersa pode ser difícil de manter.

**Solução:**

O **Abstract Factory** cria uma interface para **produzir diferentes famílias de objetos**, permitindo que você troque facilmente a **família de objetos** que está sendo criada sem modificar o código cliente.

Neste cenário, a `CarroFactory` precisa criar **carros com interiores e rodas** diferentes dependendo do tipo do carro, e isso deve ser feito de maneira consistente.


```
from abc import ABC, abstractmethod


class Interior:
    def tipo_interior(self):
        pass


class InteriorEsportivo(Interior):
    def tipo_interior(self):
        return "Estofado de couro esportivo"


class InteriorPopular(Interior):
    def tipo_interior(self):
        return "Estofado de tecido"


class CarroFactory(ABC):
    @abstractmethod
    def criar_interior(self):
        pass

    @abstractmethod
    def criar_rodas(self):
        pass


class CarroEsportivoFactory(CarroFactory):
    def criar_interior(self):
        return InteriorEsportivo()

    def criar_rodas(self):
        return "Rodas esportivas"


class CarroPopularFactory(CarroFactory):
    def criar_interior(self):
        return InteriorPopular()

    def criar_rodas(self):
        return "Rodas comuns"


# Teste
def cliente(factory: CarroFactory):
    interior = factory.criar_interior()
    rodas = factory.criar_rodas()
    print(f"Interior: {interior.tipo_interior()} | Rodas: {rodas}")

esportivo_factory = CarroEsportivoFactory()
popular_factory = CarroPopularFactory()

cliente(esportivo_factory)
cliente(popular_factory)


```


**Por que usar?**

- Permite criar diferentes **famílias de objetos** (ex: tipos de interiores e rodas).
- **Isola** a lógica de criação de objetos, mantendo o código do cliente simples e desacoplado.
- Facilita a **substituição** de famílias de objetos sem alterar o código de criação.




# Builder

Problema:

Quando você precisa criar objetos complexos com muitos parâmetros ou configurações, um único construtor pode tornar-se difícil de entender e usar, especialmente se você precisar de diferentes combinações de parâmetros.

Solução:

O **Builder** permite construir o objeto **passo a passo**, configurando cada parte de maneira explícita. Ele abstrai a complexidade do processo de criação e permite construir objetos de forma flexível.

Para construir um carro, você pode precisar configurar várias partes, como o **motor**, **cor**, **rodas** e **interior**. Criar um carro com todos esses parâmetros no **construtor** seria um problema, pois as combinações possíveis seriam grandes.


```
class Carro:
    def __init__(self, tipo_motor, cor, tipo_rodas):
        self.tipo_motor = tipo_motor
        self.cor = cor
        self.tipo_rodas = tipo_rodas

    def __str__(self):
        return f"Carro com motor {self.tipo_motor}, cor {self.cor}, e rodas {self.tipo_rodas}"


class CarroBuilder:
    def __init__(self):
        self.tipo_motor = None
        self.cor = None
        self.tipo_rodas = None

    def com_motor(self, tipo_motor):
        self.tipo_motor = tipo_motor
        return self

    def com_cor(self, cor):
        self.cor = cor
        return self

    def com_rodas(self, tipo_rodas):
        self.tipo_rodas = tipo_rodas
        return self

    def construir(self):
        return Carro(self.tipo_motor, self.cor, self.tipo_rodas)


# Teste
builder = CarroBuilder()
carro = builder.com_motor('V8').com_cor('vermelho').com_rodas('esportivas').construir()
print(carro)

```


**Por que usar?**

- Facilita a **construção de objetos complexos**, tornando o código mais legível e flexível.
- Permite **alterar a construção** do objeto sem mudar a interface, mantendo o código **flexível e extensível**.




# Prototype

Problema:

Quando você precisa duplicar objetos com muitas configurações e não quer reconstruí-los do zero, a cópia manual do objeto pode ser trabalhosa e sujeita a erros.

Solução:

O **Prototype** resolve isso clonando um objeto existente, o que economiza tempo e esforço na criação de novos objetos.

Imagina que você tenha um **modelo de carro** e precise criar versões **idênticas** com pequenas variações (como cor, modelo, etc.). Clonar o carro evita a repetição do processo de construção de objetos complexos.


```
import copy


class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    def __str__(self):
        return f"Carro modelo {self.modelo}, cor {self.cor}"

    def clonar(self):
        return copy.deepcopy(self)


# Teste
carro_original = Carro("Fusca", "azul")
carro_clonado = carro_original.clonar()
carro_clonado.cor = "preto"
print(carro_original)
print(carro_clonado)

```

**Por que usar?**

- **Clona objetos complexos** sem a necessidade de recriar atributos manualmente.
- Evita redundância na criação de objetos similares, **facilitando a reutilização** de instâncias.




---
## Contexto
- **Situação**: Estou no inicio de mestrado, um dia antes da aula inaugural e tentado aprender mais como manter meus futuros projetos organizados. 
- **Fonte**: 

## Próximos Passos
- **Ação 1**: 
- **Ação 2**: 

## Referências
- [video aula](https://www.youtube.com/live/gtqNm-kPrN4) - PycoderBR
- [Fonte 2](link) - Nota breve sobre a fonte



