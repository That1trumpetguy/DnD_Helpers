#Deven Nieves-Noel 
#9/21/2024

'''
This is meant to be a general file to test the ability to use the WorldAnvil API
I intend to make multiples of these files, for thhings like item creation, npc creation, and better map integration
This is the first forray and will most likely be the least successful

There are some helpful rescources from the WA discord linked below:

Current Documentation: https://www.worldanvil.com/api/external/boromir/documentation

Current API Python wrapper: https://gitlab.com/SoulLink/world-anvil-api-client

Current (personal) API token "9TaQa6Z37R2ApLy4F9bZbNo0UyYRtPtBejkZGkwykSPHQpAdFFwmmTMZOGmvERWHJcdkqA7YNLM2RMOGWyBpfEhBx68g2B9vKwPDsPeZmmg2HGor2bC0kbQtJFzpDmSF5Jc0JWssvAA4pzMtKeHnhQLq9ffIdtfPEaz5pZowNOw6hC2It6K2UocykUXuyqAQkRXtJFc1U8nuVqNbb5FD1hSOmOcniUukLAmNjDJPG0KPCSn62BlnhmWI1"

'''
#import block
import os
from pywaclient import BoromirApiClient

"""
This is the general forray into item and stat block creation
TO-DO: 
-figure out linking to the API and get my keys
-Get a draft item written, that I will attempt to push to the world
-Get a life
"""

client = BoromirApiClient(
    'Test_script_1', 
    
)