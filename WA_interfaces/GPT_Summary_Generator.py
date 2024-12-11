"""
Origin Date 10/30/24 
Author: Deven Nieves-Noel
This is meant to the the summarizer aspect of the DnD WA interface, it is meant to take in the transcribed text from the the Model I have
on my local home system, and translate it into a shorter form summary for posting via the API to the World Anvil, both for the party and myself

This version quries chat gpt, although I am looking into finding models that I can runan d train locally on my machine at a later date.
"""
#import block
import os
from openai import OpenAI
from pywaclient.api import BoromirApiClient
#This is my own custom code, which takes the output from GTP and pushes it into a summary article
from DnD_Session_Report_API_Tool import Push_Article

client = OpenAI()

input_path = r"E:\Code Items\Code_Items\Transcriber"

output_path = r"E:\Code Items\Code_Items\DnD_Summaries"

for file_name in os.listdir(input_path):
    if file_name.startswith("DnD") and file_name[-3:] == 'txt':  #I need to check that the file name is actually a DnD transcript which I handle with checking the first characters of the name and the last three which give file type

        #next I need to add a check to make sure the summary has not already been generated
        if not os.path.isfile(f"{output_path}\{file_name}"):

        # Read content from the file
            with open(f"{input_path}\{file_name}", "r", encoding='utf-8') as file:
                #now we open and read from the file to get a vairable to work with
                transcript_text = file.read()

            completion = client.chat.completions.create(
                model= "gpt-4o-mini", 
                messages = [
                    {
                        "role": "system", "content": """You are a helper for summarizing the transcripts of recorded DnD sesions, highlight any loot items 
                        that are picked up, characters they meet, or events where a party member goes down or dies. The party members may contain the following players:
                        Michi (female), Ord (Male), Insang Hang (Male), Jizzard (Male), and Junoon (Male). Give me as much detail as can fit in a 1-3 page
                        summary, then in a seperate section detail any NPC characters that the players may have encountered. Do not retain memeory of any other transcription projects or inputs you 
                        have previousley recieved, treat each input as unique and new."""
                    },
                    {
                        "role": "user", 
                        "content": transcript_text
                    }
                ]
            )

            #This gives us the first option that the GPT engine spits out as an output, there may be multiple outputs that I will need to look into
            output_file = completion.choices[0].message.content

            #this calls the WorldAnvil API code that I have to push the summary into an article on WA proper, this will need to be disabled for the moment becuase the API is not working for me
            #Push_Article(output)

            with open(f"{output_path}\{file_name}", 'w', encoding='utf-8') as summary:
                summary.write(output_file)

        else:
            pass


