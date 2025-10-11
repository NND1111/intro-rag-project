# Intro RAG Project
Our definitly more than 3-day collab to build a simple RAG system.
## Setup
- Run `pip install -r requirements.txt` 
- Run hf login auth in cmd and enter your User Access Token (created on hugging face website)
- Add your data of choice to /data as .txt file. Try to keep the number of pages low (less than 20 pages) for reasonably embeding time. Or else use data in /pre_chosen_data if you want to test RAG right away (or you are a fan of Trinh Cong Son)
- Run cells in the main.ipynb (embeding takes long time!)
- Test with your own query (export to csv file if you want)
- If you use free plan for api call, you may have to wait for cooldown (one month)
