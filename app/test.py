import pytest
import random
import string

from utils import *

# Number of test cases to run
num_tests = 10

def randomString(stringLength):
    """Generate a random string of given length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def testing512():  
    for k in range(num_tests):
        rand_len = random.randint(10, 53)
        inp = randomString(rand_len)
        
        n_hex, e, red1 , p_hex, q_hex, red2, red3, red4, public_key, private_key = generate(512)
        d = private_key.d
        
        encrypted_obj = encrypt(inp, int(n_hex, 16), e)
        decrypted_msg_byteObj = decrypt(encrypted_obj, int(n_hex, 16), e, d, int(p_hex, 16), int(q_hex, 16))
        decrypted_msg = str(decrypted_msg_byteObj, 'utf-8')
        assert inp == decrypted_msg, "Test failed because encrypt, decrypt didn't work as expected, strings don't match"

def testing1024():  
    for k in range(num_tests):
        rand_len = random.randint(10, 53)
        inp = randomString(rand_len)
        
        n_hex, e, red1 , p_hex, q_hex, red2, red3, red4, public_key, private_key = generate(1024)
        d = private_key.d
        
        encrypted_obj = encrypt(inp, int(n_hex, 16), e)
        decrypted_msg_byteObj = decrypt(encrypted_obj, int(n_hex, 16), e, d, int(p_hex, 16), int(q_hex, 16))
        decrypted_msg = str(decrypted_msg_byteObj, 'utf-8')
        assert inp == decrypted_msg, "Test failed because encrypt, decrypt didn't work as expected, strings don't match"

def testing3_512():  
    for k in range(num_tests):
        rand_len = random.randint(10, 53)
        inp = randomString(rand_len)
        
        n_hex, e, red1 , p_hex, q_hex, red2, red3, red4, public_key, private_key = generate(512, 3)
        d = private_key.d
        
        encrypted_obj = encrypt(inp, int(n_hex, 16), e)
        decrypted_msg_byteObj = decrypt(encrypted_obj, int(n_hex, 16), e, d, int(p_hex, 16), int(q_hex, 16))
        decrypted_msg = str(decrypted_msg_byteObj, 'utf-8')
        assert inp == decrypted_msg, "Test failed because encrypt, decrypt didn't work as expected, strings don't match"


def testing3_1024():  
    for k in range(num_tests):
        rand_len = random.randint(10, 53)
        inp = randomString(rand_len)
        
        n_hex, e, red1 , p_hex, q_hex, red2, red3, red4, public_key, private_key = generate(1024, 3)
        d = private_key.d
        
        encrypted_obj = encrypt(inp, int(n_hex, 16), e)
        decrypted_msg_byteObj = decrypt(encrypted_obj, int(n_hex, 16), e, d, int(p_hex, 16), int(q_hex, 16))
        decrypted_msg = str(decrypted_msg_byteObj, 'utf-8')
        assert inp == decrypted_msg, "Test failed because encrypt, decrypt didn't work as expected, strings don't match"