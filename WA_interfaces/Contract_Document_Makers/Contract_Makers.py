<<<<<<< HEAD

#This now prints Hello World 
print("Hello World")
=======
"""
Origin Date: 1/20/24

Author: That1trumpetguy (Deven Nieves-Noel)

Project: Long-Form document Ai Generator
    - This is supposed to be a general generation tool for creating longform documents that I do not have the time to write,
    things like contracts, book introductions, and other multi-page form content that realistically the players are not meant to fully interface 
    with. The first thing configured should be a guild contract for Nullble
"""
#import block, also grabs pywa client in case I want to push directly to WA for any reason
import os
import re
from openai import OpenAI
from pywaclient.api import BoromirApiClient

client = OpenAI()

completion = client.chat.completions.create(
    model= "gpt-4o-mini", 
    messages = [
        {
            "role": "system", "content": """This is a generator for Contracts and other long form documents to be used in a fictional Dungeons and Dragons
            setting, write all documents as if internal to this fictional setting (no phrases in the finished product similar to: In this setting, in this world, 
            in the setting of X, ect.). These documents, while legally binding are not currenlty considered magic, therefore do not reference them as such.
            The current setting is the city of Selkath, in the counry of Karamistan. I want these documents as convoluted as possible, increasing the difficulty
            of comprehension. Additionally, I want any documents generated to be a minimum of 3 pages, maximumm of the remaining number of tokens you have available"""
        },
        {
            "role": "user", 
            "content": """Please generate an adventuring guild contract for the guild Twilight Pheonix; in it contents please include a whole host of conflicting 
            stipulations and requirements, quote legal precidents that do not exist or make sense, Include a clause that automaticaly 
            constripts the signer to the armed forces of the guilds host nation should a state of war be declared. Include clauses for
            enforcement the void the persons right to any form of privacy"""
        }
    ]
)

#This gives us the first option that the GPT engine spits out as an output, there may be multiple outputs that I will need to look into
output_file = completion.choices[0].message.content

print(output_file)
>>>>>>> 753605a602cd1e01c6e66abdc1a99b6ab91c3ceb
