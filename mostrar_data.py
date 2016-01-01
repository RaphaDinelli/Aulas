import time

def mostrar_data_completa():
    localtime = time.localtime(time.time())
    
    semana ={0:'Domingo', 1:'Segunda-feira',2:'Terça-feira',3:'Quarta-feira',
    4:'Quinta-feira',5:'Sexta-feira',6:'Sabado'}
    
    return '%s/%s/%s %s:%s %s' %(localtime[2], 
    localtime[1], localtime[0], localtime[3], localtime[4], semana[localtime[6]])
    
def relogio():
    while True:
        print('\n'*100, mostrar_data_completa())
        time.sleep(60)
        
relogio()
