#!/usr/bin/env python3

import os
import logging
from logging import handlers


#BOILERPLATE
#TODO: USAR FUNÇÃO DE LOG NO FUTURO (loguru)
#pegando variável de ambiente (verifica o nível que o usuário está passando na variável de ambiente)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()


#nossa instância de logging (usuário e nível atual de debug)
log = logging.Logger("Vanessa", log_level)
'''
#level (níveis de erro)
ch = logging.StreamHandler()
ch.setLevel(log_level)
'''

#direcionando as informações do logging para um arquivo
fh = handlers.RotatingFileHandler("meulog.log", maxBytes=10**6, backupCount=10,)
fh.setLevel(log_level)

#formatação (colocar nome do usuário, horário na mensagem de erro)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
fh.setFormatter(fmt)

#destino
log.addHandler(fh)

'''
log.critical("Erro geral. O banco de dados sumiu!")
log.info("Mensagem geral para usuários")
log.debug("Mensagem pro desenvolvedor, administrador")
log.warning("Aviso que não causa erro.")
log.error("Erro que afeta uma única execução.")
'''
print("-----")

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s, str(e)")
    # stdout
    # stderr