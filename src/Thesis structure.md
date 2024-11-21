Thesis structure:

# 1 - Introduction

Até ao 3 a estrutura é semelhante à preparação.

Tirei a secção sobre resource management, tinha o Mesos, OMEGA, etc, deveria ter tirado?

## 1.1 Context

## 1.2 Problem Statement

## 1.3 Contributions

## 1.4 Document Organization

# 2 Related work

## 2.1 Cloud and edge computing

### 2.1.1 Other computing paradigms

## 2.2 Overlay networks

### 2.2.1 Unstructured and structured overlays

### 2.2.2 Properties of overlay networks

### 2.2.3 Tools to build overlay networks

### 2.2.4 Related overlay networks

### 2.2.4 Conclusions

## 2.3 Monitoring solutions

### 2.3.1 Properties of monitoring solutions

### 2.3.1 Related monitoring solutions

### 2.3.3 Conclusions

### 2.4 Summary

# 3 GO-Babel framework

Explicação do que é, para que serve e porque é que construimos o node watcher (medir latencia é dificil no Babel)

# 3.1 Overview

Resumo muito high-level, citar papers originais e dizer que explicação mais aprofundada esta lá

# 3.2 Node Watcher

Explicacao high-level das operações e para que servem, e porque é que abstraímos a implementação num só modulo

# 3.3 Conclusion

# 4 The DeMMon framework

Explicação do que é, para que serve e porque é que construimos

# 4.1 Overview

Imagem com:

clientes (como aplicações de gestão de recursos) , aplicações (para enviarem métricas), API, overlay network e monitoring protocol

Explicar sucintamente como os componentes interagem entre si

## 4.2 Overlay network

Explicar a fundo, com imagens etc

## 4.3 Monitoring protocol

Explicar a fundo, com imagens etc

## 4.4 DeMMon API

Fazer uma breve explicacao das operacoes possiveis, falar da query language, extensibilidade, etc, com imagens etc

## 4.3 Summary

# 5 Benchmark

falar do NovaPokemon, motivacao para construir
explicar porque microservicos, etc

## 5.1 Overview

Diagrama com os servicos, brevemente explicar interacao entre eles

## 5.2 Design choices

Falar de S2 cells, location server, notifications, alguns mecanismos de relevancia e de que maneira que podem ser uteis para testar sistemas de deployment / resource management

## 5.3 Summary

# 6 Evaluation

## 6.1 Evaluation environment

## 6.1 Overlay network

Lista de experiências e resultados de membership

## 6.3 Broadcast

Lista de experiências e resultados de broadcast

## 6.2 Monitoring

Lista de experiências e resultados de monitorizaçao

## 6.3 Use cases ???

Falar do NovaPokemon com a tese do bruno aqui???

## 7 Conclusion and future work
