import discord
from discord.ext import commands

client = commands.Bot(command_prefix="?")

TOKEN = ""


@client.event
async def on_ready():
  print("yay")

@client.command()
async def info(ctx):
  info_embed = discord.Embed(description="The COVID-19 pandemic is a ubiquitous issue that affects billions of people every day. It is important to be informed about COVID-19 to be prepared for the dangers it poses to the community. Despite favorable numbers, COVID-19 remains a hugely influential crisis and thus, precautions must be taken so as to prevent further repercussions of lax habits.", color=discord.Color.blue())
  await ctx.send(embed=info_embed)

@client.command()
async def healthscreening(ctx):
  lst = []
  message = await ctx.send("Welcome to the Health Helper Health Screening! To start off, have you recently been in close contact with an individual affected by COVID-19? (Answer with 'yes' or 'no')")
  response1 = await client.wait_for("message")
  lst.append(response1.content.lower())
  await ctx.send("Are you vaccinated against COVID-19? (Answer with 'fully', 'partially', or 'no')")
  response2 = await client.wait_for("message")
  lst.append(response2.content.lower())
  await ctx.send("Have you recently experienced any symptoms of COVID-19 (i.e. sore throat, fever, cough, etc.)? (Answer with 'many', 'some', or 'none')")
  response3 = await client.wait_for("message")
  lst.append(response3.content.lower())
  if lst == ["yes", "fully", "many"]:
    await ctx.send("You most likely have COVID-19. Take a COVID test (rapid or PCR) and use the '!assist' command to find other commands with resources and advice that may be relevant to your situation.")
  elif lst == ["yes", "fully", "some"]:
    await ctx.send("You most likely have COVID-19. Take a COVID test (rapid or PCR) and use the '!assist' command to find other commands with resources and advice that may be relevant to your situation.")
  elif lst == ["yes", "fully", "none"]:
    await ctx.send("You most likely do not have COVID-19. However, you should still take a COVID test (rapid or PCR) and use the '!assist' command to find other commands with resources and advice that may be relevant to your situation.")
  elif lst == ["yes", "partially", "many"]:
    await ctx.send("You most likely have COVID-19. Take a COVID test (rapid or PCR) and use the '!assist' command to find other commands with resources and advice that may be relevant to your situation.")
  elif lst == ["yes", "partially", "some"]:
    await ctx.send("You most likely have COVID-19. Take a COVID test (rapid or PCR) and use the '!assist' command to find other commands with resources and advice that may be relevant to your situation.")
  elif lst == ["yes", "partially", "none"]:
    await ctx.send("You most likely do not have COVID-19. However, you should still take a COVID test (rapid or PCR) and use the '!assist' command to find other commands with resources and advice that may be relevant to your situation.")
  elif lst == ["yes", "no", "many"]:
    await ctx.send("You most likely have COVID-19. Take a COVID test (rapid or PCR) and use the '!assist' command to find other commands with resources and advice that may be relevant to your situation.")
  elif lst == ["yes", "no", "some"]:
    await ctx.send("You most likely have COVID-19. Take a COVID test (rapid or PCR) and use the '!assist' command to find other commands with resources and advice that may be relevant to your situation.")
  elif lst == ["yes", "no", "none"]:
    await ctx.send("You most likely do not have COVID-19. However, you should still take a COVID test (rapid or PCR) and use the '!assist' command to find other commands with resources and advice that may be relevant to your situation.")
  elif lst == ["no", "fully", "many"]:
    await ctx.send("You most likely do not have COVID-19. However, you should still take a COVID test (rapid or PCR) and use the '!assist' command to find other commands with resources and advice that may be relevant to your situation.")
  elif lst == ["no", "fully", "some"]:
    await ctx.send("You most likely do not have COVID-19. However, you should still take a COVID test (rapid or PCR) and use the '!assist' command to find other commands with resources and advice that may be relevant to your situation.")
  elif lst == ["no", "fully", "none"]:
    await ctx.send("You most likely do not have COVID-19. You may use the '!assist' command to find other commands with resources and advice.")
  elif lst == ["no", "partially", "many"]:
    await ctx.send("You most likely do not have COVID-19. However, you should still take a COVID test (rapid or PCR) and use the '!assist' command to find other commands with resources and advice that may be relevant to your situation.")
  elif lst == ["no", "partially", "some"]:
    await ctx.send("You most likely do not have COVID-19. However, you should still take a COVID test (rapid or PCR) and use the '!assist' command to find other commands with resources and advice that may be relevant to your situation.")
  elif lst == ["no", "partially", "none"]:
    await ctx.send("You most likely do not have COVID-19. You may use the '!assist' command to find other commands with resources and advice.")
  elif lst == ["no", "no", "many"]:
    await ctx.send("You most likely have COVID-19. Take a COVID test (rapid or PCR) and use the '!assist' command to find other commands with resources and advice that may be relevant to your situation.")
  elif lst == ["no", "no", "some"]:
    await ctx.send("You most likely do not have COVID-19. However, you should still take a COVID test (rapid or PCR) and use the '!assist' command to find other commands with resources and advice that may be relevant to your situation.")
  elif lst == ["no", "no", "none"]:
    await ctx.send("You most likely do not have COVID-19. You may use the '!assist' command to find other commands with resources and advice.")
  else:
    await ctx.send("Error processing requests. Retake health screening.")

@client.command()
async def closecontact(ctx):
  cc_embed = discord.Embed(description="A close contact is when you have spent time close to someone who has contracted COVID-19. Close contacts may result in exposure to COVID-19. If you are a close contact, we recommend to take a COVID-19 pathogen test. There are two types of COVID-19 tests, rapid tests and PCR tests. It is recommended that you take one of these tests.", color=discord.Color.blue())
  await ctx.send(embed=cc_embed)

@client.command()
async def positive_symptoms(ctx):
  pos_symp_embed = discord.Embed(description="In the event that you test positive for COVID-19 and exhibit serious symptoms, contact your primary healthcare provider about course of action. Quarantine and social distance from those around you until further notice from your doctor or after a minimum of 10 days in isolation.", color=discord.Color.blue())
  await ctx.send(embed=pos_symp_embed)

@client.command()
async def positive_asymptomatic(ctx):
  pos_asymp_embed = discord.Embed(description="In the event that you test positive for COVID-19 but do not exhibit symptoms or exhibit minor symptoms, quarantine and distance yourself from those around around you for a minimum of 5 days in isolation.", color=discord.Color.blue())
  await ctx.send(embed=pos_asymp_embed)

@client.command()
async def resources(ctx):
  res_embed = discord.Embed(title="COVID-19 Resources", color=discord.Color.blue())
  res_embed.add_field(name="CDC: Centers for Disease Control and Prevention", value="https://www.cdc.gov", inline=False)
  res_embed.add_field(name="WHO: World Health Organization", value="https://www.who.int", inline=False)
  res_embed.add_field(name="Get Vaccinated", value="https://www.vaccines.gov", inline=False)
  res_embed.add_field(name="COVID-19 NYC Health", value="https://www1.nyc.gov/site/doh/covid/covid-19-main.page", inline=False)
  res_embed.add_field(name="COVID-19 Resources for Schools", value="https://www.ed.gov/coronavirus", inline=False)
  await ctx.send(embed=res_embed)

@client.command()
async def assist(ctx):
  embed = discord.Embed(title="Health Helper Commands", color=discord.Color.blue())
  embed.add_field(name="!assist (this command)", value="List of all commands and their descriptions.", inline=False)
  embed.add_field(name="!info", value="Description of the COVID-19 Pandemic.", inline=False)
  embed.add_field(name="!healthscreening", value="Take a survey to evaluate potential COVID-19 symptoms.", inline=False)
  embed.add_field(name="!resources", value="List of informative resources.", inline=False)
  embed.add_field(name="!closecontact", value="Close Contacts Information.", inline=False)
  embed.add_field(name="!positive_symptoms", value="Covid-19 Positive with Symptoms.", inline=False)
  embed.add_field(name="!positive_asymptomatic", value="Covid-19 Positive with No Symptoms.", inline=False)
  await ctx.send(embed=embed)

client.run(TOKEN)
