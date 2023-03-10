# JurosPython
Um projeto pessoal que visa melhorar e tornar um pouco mais justa o calculo de juros.

# Objetivo
Nesse projeto eu viso propor uma forma mais justa para o calculo de juros em empréstimos, pois acredito que o cálculo de juros compostos é muito injusto com o pagante.
## Breve histórico e justificativa

Desde, pelo menos o século XVI, quando foi institucionalizado os empréstimos a juros; contrariando a Igreja Católica que definia a prática como o pecado da usura, todos os empréstimos funcionam sobre dois regimes distintos: os juros simples e os chamados juros compostos.

Basicamente, os juros são uma fração do valor emprestado que o tomador do emprétimo se compromete a pagar de volta 
a fim de garantir o empréstimo e para fazer jus ao período em que o emprestador do dinheiro (Seu legítimo dono) não pôde acessar sua 
riqueza.

Para tal cálculo é considerado justo cobrar um valor proporcional ao valor emprestado, assim, na escola você provavelmente estudou os 
juros calculados da seguinte forma:  
$$J=C*i$$  
- onde,  J é o juro a ser pago;  
C é o capital (valor) emprestado;  
i é a taxa de juros (um valor que para ser justo varia entre 0 e 1).

Assim, vemos que o valor pago depende do valor emprestado, tal qual o valor de um aluguel de carros depende do valor do veículo alugado, 
mas o valor a ser pago, chamado __montante__ é definido como a soma do valor emprestado com o juros, ou seja:  
$$M=C+J$$  

Os juros porém tem um terceiro fator importante a ser levado em consideração, o tempo, pois quanto do ponto de vista do emprestador quanto
mais tempo o tomador levar para pagar de volta do empréstimo, mais arriscado é para este dar um calote (por si só essa é uma forma tosca de avaliar esse risco, mas é intuitiva e todos costumam aceitá-la), de forma que quanto mais tempo levar para este pagar a dívida, 
mais o emprestador deseja cobrar empréstimo.

Assim, tomando *t* como sendo o tempo para quitação do empréstimo:  
$M=C+J*t$  
e simplificando essa fórmula para melhor legibilidade:  

$M=C*(1+i*t),$  
 *onde i é a taxa de juros*  

é importante olhar para essa fórmula, pois é a partir dela que será calculado os juros compostos.  
Veja que pela fórmula acima, podemos descrever variadas formas de dar dinheiro a alguém, como um "empréstimo". Quando selecionamos *i=0*, 
vemos que pela fórmula isso equivale a maioria dos empréstimos informais, onde o tomador paga apenas o valor emprestado de volta em algum momento.  
Já quando selecionamos *i=-1* pela fórmula isso equivale a uma doação, onde o "tomador" do emprétimo não se vê obirgado a pagar nada depois. Essa pode ser uma forma bastante viajada de se pensar, mas é notável que no passado muitos economistas liberais *matematizávam* a questão de doações dessa forma, e por isso essa visão sobre os empréstimos orientou diversas políticas monetárias ao longo do tempo.

### Juros Compostos
O caso dos juros compostos começam quando surge a idéia de crédito, nela o tomador de empréstimo, tem uma quantida pré-Aprovada que ele pode utilizar e o banco *acredita* (daí o termo) que ele dará conta de arcar com esse pagamento num prazo muito curto (algo como 1 mês),
essa modalidade de empréstimo então é semelhante ao caso de um amigo seu que te empresta uma grana acreditando que vc pagará amanhã.  

Note que nesse caso específico valor de *t=1* e assim a fórmula do juros acaba sendo:  
$$M=C*(1+i)$$ 
