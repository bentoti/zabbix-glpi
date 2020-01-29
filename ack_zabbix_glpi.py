## Modificado por: Vitor Mazuco / vitor.mazuco@gmail.com>
## Ultima atualizacao: 27/09/2017
## Observacoes: Este script é executado automaticamente apos a abertura do ticket no GLPI

from zabbix_api import ZabbixAPI
import sys
 
server = "http://127.0.0.1/zabbix"
username = "Admin"             
password = "zabbix"     
 
conexao = ZabbixAPI(server = server)
conexao.login(username, password)

reconhecer_evento = conexao.event.acknowledge({"eventids": sys.argv[1], "message": "Ticket " + str(sys.argv[2]) + " criado no GLPI."})

# Esse código foi publicado originalmete pelo @Janssen dos Reis Lima
