import flask.views

def pop13aux():
    """
    Realiza la funcion pop de 13 variables auxiliares de sesion
    """
    flask.session.pop('aux',None)
    flask.session.pop('aux1',None)
    flask.session.pop('aux2',None)
    flask.session.pop('aux3',None)
    flask.session.pop('aux4',None)
    flask.session.pop('aux5',None)
    flask.session.pop('aux6',None)
    flask.session.pop('aux7',None)
    flask.session.pop('aux8',None)
    flask.session.pop('aux9',None)
    flask.session.pop('aux10',None)
    flask.session.pop('aux11',None)
    flask.session.pop('aux12',None)
    flask.session.pop('aux13',None)
    

def longitud(a=None):
    """
    Retorna la longitud de un objeto, funcion que se llama desde un html
    """
    l=len(a)
    return l