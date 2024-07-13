'''
Library for interacting with the PasteBin API
https://pastebin.com/doc_api
'''
import requests

PASTEBIN_API_POST_URL = 'https://pastebin.com/api/api_post.php'
API_DEV_KEY = '4GLskhG47Uk55brq1r3NDKDsCX0M1UZV'

def post_new_paste(title, body_text, expiration='N', listed=True):
    """Posts a new paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
        listed (bool): Whether paste is publicly listed (True) or not (False) 
    
    Returns:
        str: URL of new paste, if successful. Otherwise None.
    """    
    # TODO: Function body
    # Note: This function will be written as a group 
    print("Posting new paste to Pastebin...", end='')
    # Message body parameters
    
    postparameters = {
                    'API_NISH_KEY' : API_DEV_KEY,
                    'API_OPTION': 'PASTE',
                    'API_PASTE_CODE': body_text,
                    'API_PASTE_NAME': title,
                    'API_PASTE_PRIVATE': 0 if listed else 1,
                    'API_PASTE_EXPIREDDATE': expiration
                     }
    
    # Request a new PasteBin paste
    
    respmeassge= requests.post(PASTEBIN_API_POST_URL, data=postparameters)
    
    #check if paste was created successfully
    
    if respmeassge.status_code == requests.codes.ok:
    
            print("Congratulation on Success")
    
    else:
    
        print("sorry, failure in creating paste")
    
        print(f'Response code: {respmeassge.status.code}' ({respmeassge.reason}))
    
    return respmeassge.text