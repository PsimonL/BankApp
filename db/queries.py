select_client_query = "Select * from clients where clients.pesel="

insert_clients_query_part1 = """INSERT INTO `clients` ( `pesel`, `password`, `name`, `surname`, `wallet`, `accountNumber`,
                                    `confirmed`,`creditCards`,`loans`,`deposits`) VALUES 
"""
select_unconfirmed_clients_query = "select * from clients where confirmed=0"

select_user_by_pesel_query_part1="select password from clients where pesel= "