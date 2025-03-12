"""
Origin Date 10/30/24 
Author: Deven Nieves-Noel
This is meant to the the summarizer aspect of the DnD WA interface, it is meant to take in the transcribed text from the the Model I have
on my local home system, and translate it into a shorter form summary for posting via the API to the World Anvil, both for the party and myself

This version quries chat gpt, although I am looking into finding models that I can runan d train locally on my machine at a later date.

TO DO: 

- I need a way to give the summarizer some setting context and information, but only once
- I need a way to fix misspellings of character names
- I need a way to remove soem of the janky character analysis that the model tries to include, its not welcome in a summary for players
"""
#import block
import os
import re
from openai import OpenAI
from pywaclient.api import BoromirApiClient
#This is my own custom code, which takes the output from GTP and pushes it into a summary article
from DnD_Session_Report_API_Tool import Push_Session_Report

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
                        "role": "system", "content": """You are a helper function, who’s purpose is to summarize transcriptions of Dungeons and Dragons games. I will be giving you a variety of transcripts over time, each one with this prompt attached, 
                        you are to summarize the events of the session, as well as meaningful actions taken by the characters in each session, however you are not to include any “story” or “character” analysis, as these summaries exist for the players themselves. 
                        Do not include anything like “This shows character x’s commitment to y” as that type of analysis is not needed. You will include a section detailing any NPC (Non-Plyer Character) characters that they players or party interacts with, their 
                        descriptions, and what the result of the encounter was. In addition to this you will also include a detailed breakdown of any loot or items the party picked up during the session, and any money they spent in the acquisition of items. 
                        The party members include: Michi (female, played by Nullble/Kalan), Ord (Male, played by Jake/Render), Insan Hang (Male, played by Coy/PanMelon), Jizzard (Male, Played by Hunter), Fors (Female, played by Natale), 
                        and Junoon (Male, played by Allyanna), because of scheduling, certain characters may not be present for all of the sessions and so may be absent in the transcript or only mentioned by reference. I want all transcriptions to be in the 
                        same structure and format, and to fit a maximum length of 4 pages, minimum 2.5 page. """
                    },
                    {
                        "role": "user", 
                        "content": transcript_text
                    }
                ]
            )

            #This gives us the first option that the GPT engine spits out as an output, there may be multiple outputs that I will need to look into
            output_file = completion.choices[0].message.content

            #This extracts the date from the file name and allows it to be passed to the article pusher
            match = re.search(r"DnD_(\d{2}-\d{2}-\d{2})\.txt", file_name)

            if match:
                date = match.group(1)
                print(f"Extracted transcript from date: {date}")
            else:
                date = "Unknown"
                print("Date is unknown")
            #this calls the WorldAnvil API code that I have to push the summary into an article on WA proper, this will need to be disabled for the moment becuase the API is not working for me
            Push_Session_Report(output_file, date)

            with open(f"{output_path}\{file_name}", 'w', encoding='utf-8') as summary:
                summary.write(output_file)

        else:
            pass


