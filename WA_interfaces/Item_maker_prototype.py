#Deven Nieves-Noel 
#9/21/2024

'''
This is meant to be a general file to test the ability to use the WorldAnvil API
I intend to make multiples of these files, for thhings like item creation, npc creation, and better map integration
This is the first forray and will most likely be the least successful

There are some helpful rescources from the WA discord linked below:

Current Documentation: https://www.worldanvil.com/api/external/boromir/documentation

Current API Python wrapper: https://gitlab.com/SoulLink/world-anvil-api-client

Current (personal) API token "

'''
#import block
import os
from pywaclient.api import BoromirApiClient

"""
This is the general forray into item and stat block creation
TO-DO: 
-figure out linking to the API and get my keys
-Get a draft item written, that I will attempt to push to the world
-Get a life
"""

client = BoromirApiClient(
    #Project Name
    'Test_script_1', 
    #Github Project URL
    "nourl_yet", 
    #Project Version
    'V0',
    #API Key supplied by WA saff
    '073a7c2deeffd2c94244f78fce44036aae2f34d54dd27e5719eff88b9c9b85ff8bd1442ce8986d81dc082cfa397a7b7879b4a6e7c7a60bfe3b0c6b0a8e2024c0',
    #Api User authentication token generated by the user in the world
    '9TaQa6Z37R2ApLy4F9bZbNo0UyYRtPtBejkZGkwykSPHQpAdFFwmmTMZOGmvERWHJcdkqA7YNLM2RMOGWyBpfEhBx68g2B9vKwPDsPeZmmg2HGor2bC0kbQtJFzpDmSF5Jc0JWssvAA4pzMtKeHnhQLq9ffIdtfPEaz5pZowNOw6hC2It6K2UocykUXuyqAQkRXtJFc1U8nuVqNbb5FD1hSOmOcniUukLAmNjDJPG0KPCSn62BlnhmWI1'
)

authenticated_user = client.user.identity()

#print(f"{authenticated_user}")

# get the references to all the worlds on your account.
worlds = [world for world in client.user.worlds(authenticated_user['id'])]

#print(f"these are all of the worlds {worlds}")

#print(worlds[0]['id'])


new_test_article = client.article.put({
    #Title for the article
    'title': "A test of the Code Article Builder III",
    #The display state of the article
    'state': "Private",
    'content': "This is example content, the example date is 3/28/200",
    #The world for it to go in, it references line 47-48, id is a lookup for a param in the dictionary that line 48 provides, it gives world id 
    'world': {
        'id': worlds[0]['id']
    },
    #template type for the article to be generated
    'templateType': 'report'
}) 

# new_test_block = client.block.put({
#     #Title for the article
#     'title': "Block Builder ID 28",
#     #The display state of the article
#     'state': "Private",
#     #A test of the user Icon setting for the block builder  on the WorldAnvil interface
#     'icon' : "ra-ammo-bag",

#     'template': {
#         "id": 28
#     },
#     #The world for it to go in, it references line 47-48, id is a lookup for a param in the dictionary that line 48 provides, it gives world id 
#     'world': {
#         'id': worlds[0]['id']
#     },
# })