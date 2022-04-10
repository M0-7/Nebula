for filename in os.listdir("./events/server"):
    if filename.endswith(".py"):
      initial_extensions.append("events.server."+ filename[:-3])
  for filename in os.listdir("./events/user"):
    if filename.endswith(".py"):
      initial_extensions.append("events.user."+ filename[:-3])
for filename in os.listdir("./serverstats"):
    if filename.endswith(".py"):
      initial_extensions.append("serverstats."+ filename[:-3])