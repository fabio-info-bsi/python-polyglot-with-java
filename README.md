# python-polyglot-with-java
Este projeto tem o objetivo de implementar código Java incorporado no Python através de programação polyglota na GraalPy.

---

## Pré-requisitos

- [GraalPy (Python)](https://www.graalvm.org/jdk21/reference-manual/python/)
- Java >= 17
- Maven >= 3

---

## GraalPy (Python)

GraalPy fornece um ambiente de execução compatível com Python 3.10.

Referências:

- https://www.graalvm.org/jdk21/reference-manual/python/

- https://github.com/oracle/graalpython

### Instalação do GraalPy

#### Pyenv
`pyenv install graalpy-23.1.0`

#### Conda-Forge
`conda create -c conda-forge -n graalpy graalpy`

#### Para Windows
Há uma versão prévia do GraalPy para Windows que você pode [baixar](https://github.com/oracle/graalpython/releases/). Ele suporta a instalação de pacotes Python puros via pip. As extensões nativas são um trabalho em andamento.

A compilação do Windows tem vários problemas conhecidos:

- JLine trata o Windows como um terminal burro, sem preenchimento automático e recursos de edição limitados no REPL
- help() interativo no REPL não funciona
- Dentro dos ambientes:
  - graalpy.cmd e graalpy.exe estão quebrados
  - pip.exe não pode ser usado diretamente
  - pip tem problemas com o carregamento do arquivo de cache, use `--no-cache-dir`
  - Apenas binárias Python puros podem ser instaladas, sem extensões nativas ou compilações de código-fonte
  - Para instalar um pacote, use `myvenv/Scripts/python.cmd -m pip --no-cache-dir install <pkg>
- Executar a partir do PowerShell funciona melhor do que executar a partir do CMD; vários scripts vão falhar via CMD.


### Instalação de ambiente e pacotes Python

`graalpy -m venv .env `

`source .env/bin/activate`

`graalpy -m pip install -r requirements.txt` or `graalpy -m ginstall install <package>==<version>`

---
