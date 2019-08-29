# breachre_bot
A simple Python bot for Discord that checks whether your security has been compromised by scanning multiple databases with an e-mail provided.

**Usage**
1. Set *TOKEN* and *BREACH_TOKEN* env variables :
`export TOKEN="your_discord_token_here" ; export BREACH_TOKEN="your_BR_API_token_here"`
2. Activate virtual environment OR install requiremnets from *requiremnets.txt* :
`python3 -m venv env`
`source env/bin/activate`
`pip install -r requirements.txt`
3. Launch to fire up:
`python3 bot.py`

**Troubleshooting**
Well, logging is on by default, so it should be no sweat.
