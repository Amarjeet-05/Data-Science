# # we are converting the mp3/speech into text using whisper
# import whisper
# import os
# import json

# model = whisper.load_model("large-v2") #large-v2 is the model which are we using

# audios = os.listdir("audio")
# # i dumped only two files because it was taking too much time
# for audi in audios:
#     print(f"Processing {audi}...............")
#     result = model.transcribe(audio=f"audio/{audi}", 
#                               language="en",
#                               task="translate")
#     fname = audi.split(".")[0]
#     # print(fname)

#     chunks = []
#     for segment in result["segments"]:      #here we are using result['segment] from the output of that program we looked the structure and then accessing the details from the output
#         chunks.append({"start" : segment["start"],
#                 "end" : segment["end"], 
#                 "text" : segment["text"]})
    
#     json_chunk = {"text" : result["text"],
#                   "chunks" : chunks}
    
    
#     with open(f"json/{fname}.json", "w") as f:
#         json.dump(json_chunk,f)
    
#     print()
#     print(f"{fname} dumped successfully! ")
#     print("*" *40)

def fun(x=[]):
x.append(1)
    return x 
print(fun())
print(fun())