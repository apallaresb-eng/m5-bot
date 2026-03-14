# cogs/gestion.py — Comunicación y gestión del servidor
# Bloque D: recordatorio, limpiar, anuncio_embed, encuesta, silenciar

import discord
from discord.ext import commands
import asyncio
import re
from datetime import datetime, timezone, timedelta
from typing import Optional

import database as db
from config import (
    COLOR_PRINCIPAL, COLOR_EXITO, COLOR_ALERTA, COLOR_INFO,
    ANNOUNCEMENTS_CHANNEL_ID, RANGO_ALTO_MANDO
)
from utils.embeds import embed_base, embed_error, embed_exito, embed_info
from utils.permisos import requiere_rango_minimo, solo_oficiales, solo_alto_mando
