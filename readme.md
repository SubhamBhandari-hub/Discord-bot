🤖 Simple Discord Bot

A lightweight Discord bot built with Python using discord.py.
It handles basic commands and logs incoming messages for debugging.

⚙️ Features
Responds to simple commands
Logs all received messages in console
Basic error handling
Easy to extend for new commands
📜 Commands

Use these in your Discord server:

!hello → Bot replies: Yo. I’m alive.
!ping → Bot replies: pong
!bye → Bot replies: See you later 👋
!lol → Bot replies: haha.
!okay → Bot replies: Okay 👍
!gg → Bot replies: good game👍
🧠 How It Works
Uses discord.ext.commands for command handling
Listens for messages with on_message
Processes commands manually using bot.process_commands(message)
Prints all received messages to terminal for debugging