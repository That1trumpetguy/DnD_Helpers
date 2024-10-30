"""
Origin Date 10/30/24 
Author: Deven Nieves-Noel
This is meant to the the summarizer aspect of the DnD WA interface, it is meant to take in the transcribed text from the the Model I have
on my local home system, and translate it into a shorter form summary for posting via the API to the World Anvil, both for the party and myself

This version quries chat gpt, although I am looking into finding models that I can runan d train locally on my machine at a later date.
GPT API Key: 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
"""

from openai import OpenAI

client = OpenAI()

# Read content from the file
with open("transcript.txt", "r") as file:
    transcript_text = file.read()

completion = client.chat.completions.create(
    model= "gpt-4o-mini", 
    messages = [
        {
            "role": "system", "content": "You are a helper for summarizing the transcripts of recorded DnD sesions, highlight any items that are picked up, characters they meet, or events where a party memerb goes down or dies. The party members are: Michi (female), Ord (Male), Insang Hang (Male), Jizzard (Male), and Junoon (Male). Give me as much detail as can fit in a 3 paragraph (1 standard page) summary"
        },
        {
            "role": "user", 
            "content": transcript_text
        }
    ]
)

print(completion.choices[0].message)