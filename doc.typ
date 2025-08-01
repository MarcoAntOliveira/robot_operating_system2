// === Macros reutilizáveis ===
#let header(title, author, date) = [
  #set align(center)
  = #title
  Autor: #author
  Data: #date
]

// === Configurações globais ===
#set page(
  margin: (top: 2cm, bottom: 2cm, x: 2.5cm),
)


// === Cabeçalho do documento ===
#header("Documentação ROS2", "Marcos", "20/07/2025")

= 1.  Talker and Listener

Este documento descreve uma demonstração simples do ROS utilizando os nós `talker` e `listener`. A comunicação entre esses nós ocorre por meio do tópico `/chatter`.

==  1.1 Execução dos nós

Primeiramente, acionamos o `talker`:

```bash
ros2 run demo_nodes_cpp talker
```
Depois, iniciamos o listener:

ros2 run demo_nodes_cpp listener

= 1.2 Visualização gráfica

Podemos visualizar a comunicação entre os nós com o rqt_graph.

#image("talker_listener.png", width: 80%)

Como pode ser observado, tanto o nó talker quanto o nó listener se comunicam com o tópico /chatter. Eles não trocam informações diretamente entre si.

= 1.3 Inspeção do tópico /chatter

Para inspecionar as mensagens publicadas no tópico /chatter, utilizamos:

= 1.4 imprimindo dados da porta serial com python
Uma das funcionalidades que podem ser aproveitadas do codigo em python é a vizualição da portaserial

