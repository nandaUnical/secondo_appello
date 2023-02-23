import pytest
import sys
#sys.path.insert(1,'C:/Users/hp/Documents/!Master/Agile/!!Second Apello/secondo_appello/pasword')
from  pasword import code_pasword as cp


@pytest.fixture
def pasword_object():
    texto = cp.obtener_datos()
    object = cp.pasword(texto)
    return object

@pytest.mark.parametrize('pwd',[('1234','qwert','1q2w3e')])

def test_validate_pwd_size(pwd):
    for elem in pasword_object.response :
        #print(paswo)
        assert elem['issues'] != 'Pasword should have at least 8 characters and no more than 16.'

'''
def test_validate_pwd_size (pasword_object):
    pasword_object.validate_pwd_size() 
    
    print (pasword_object.response)

def test_have_upper_case ():
    assert cp.have_upper_case('12W12') == True, 'It should have at least une uppercase latter'

def test_differents_char ():
    assert cp.have_4diff_char ('asdasdasd') == False , 'Have 4 differents characters'

def test_have_adyacent_char() :
    assert cp.have_adyacent_char ('12234') == True, 'Havent adyacent characters'
    '''

#test_validate_pwd_size(pasword_object)