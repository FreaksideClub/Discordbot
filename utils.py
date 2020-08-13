import discord
from discord.ext import commands
from settings import *


async def create_voice_channel(guild, channel_name, category_name="🎤 VOICE ZONE 🎤", user_limit=None):
    """
    Creates a new channel in the category "Game"
    """
    category = get_category_by_name(guild, category_name)
    await guild.create_voice_channel(channel_name, category=category, user_limit=user_limit)
    channel = get_channel_by_name(guild, channel_name)
    return channel


def get_channel_by_name(guild, channel_name):
    """
    Get channel object by channel_name
    """
    channel = None
    for c in guild.channels:
        if c.name == channel_name:
            channel = c
            break
    return channel


def get_category_by_name(guild, category_name):
    """
    Get category object by category name
    """
    category = None
    for c in guild.categories:
        if c.name == category_name:
            category = c
            break
    return category