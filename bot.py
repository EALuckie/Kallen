#bot.py
import responses
import discord

'''
Token: MTE0MDAwOTE4Njc4MTA1MjkzOA.GvNxt0.EHg4fVZZ1lGqlFMUQ9uH4wIV5aIp1QIhaY7XCY
Invite link: https://discord.com/api/oauth2/authorize?client_id=1140009186781052938&permissions=1634235578432&scope=bot
'''

async def send_message(message, user_message):
    try:
        response=responses.handle_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print("Ups an error in send_message()")
        print (e)

def run_discord_bot():
    TOKEN= "MTE0MDAwOTE4Njc4MTA1MjkzOA.GvNxt0.EHg4fVZZ1lGqlFMUQ9uH4wIV5aIp1QIhaY7XCY"
    #Important: Explicitly enable the priviliged intents in the application's page.
    #So you're able to read messages from the users
    intents = discord.Intents.default()  
    intents.message_content = True
    client = discord.Client(intents = intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")

    @client.event
    async def on_message(message):
        if message.author== client.user:
            return
        
        username= str(message.author)
        user_message= str(message.content)
        channel= str(message.channel)

        print(f"{username} said: {message.content} in channel: {channel}")

        await send_message(message, user_message)

    client.run(TOKEN)