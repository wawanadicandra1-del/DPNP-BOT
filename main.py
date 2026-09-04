import discord
import random
import json
import os
import asyncio
import datetime
import shutil
import traceback

from collections import deque
from config import TOKEN
from discord import app_commands
from discord.ui import View, Button

WELCOME_CHANNEL_ID = 1417152242817044550
JOIN_GREET_CHANNEL_ID = 1402253424296198175
GOODBYE_CHANNEL_ID = 1417152314476859422
BOOST_CHANNEL_ID = 1417152381291860118
BOOSTER_ROLE_ID = 1437740399786459247    
AUTO_ROLE_ID = 1438899323336130802
RULES_CHANNEL_ID = 1459140957932093652
TAKE_ROLE_CHANNEL_ID = 1417152449650626693
PRINCESS_ROLE_ID = 1417156113232826450
PRINCE_ROLE_ID = 1417156158518464594
MOBILE_LEGENDS_ROLE_ID = 1449602863687794789
AMONG_US_ROLE_ID = 1449603295046930443
ROBLOX_ROLE_ID = 1449603377150562354
FREE_FIRE_ROLE_ID = 1502158964857638924
VALORANT_ROLE_ID = 1521865058102149131
PUBG_ROLE_ID = 1533083879563595826
CLASH_OF_CLANS_ROLE_ID = 1533078042711167108
DEAD_BY_DAYLIGHT_ROLE_ID = 1519218694591348786
MINECRAFT_ROLE_ID = 1533083362431074354
E_FOOTBALL_ROLE_ID = 1533083282072146062
CATUR_ROLE_ID = 1475915903945277450
CODENAME_ROLE_ID = 1538166999853834240
LUDOKING_ROLE_ID = 1544505242928947240

REGIONAL_ROLES = [
    ("BALI", 1532525127995228291, "🏖️"),
    ("JAWA", 1532525196924289024, "🗺️"),
    ("KALIMANTAN", 1532525310531211454, "🏕️"),
    ("PAPUA", 1532525895821037649, "🌋"),
    ("SULAWESI", 1532525394429743345, "🛣️"),
    ("SUMATRA", 1532525469671358646, "🏜️"),
    ("NUSA TENGGARA", 1533099143403405382, "🌊"),
    ("MALAYSIA", 1533099187888066670, "🇲🇾"),
]
REGIONAL_ROLE_IDS = [role_id for _, role_id, _ in REGIONAL_ROLES]

ZODIAC_PANEL_IMAGE_URL = os.getenv("ZODIAC_PANEL_IMAGE_URL", "").strip()
REGIONAL_PANEL_IMAGE_URL = os.getenv("REGIONAL_PANEL_IMAGE_URL", "").strip()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GAMES_PANEL_IMAGE_PATH = os.path.join(BASE_DIR, "dpnpgameserverrole.png")
WELCOME_GOODBYE_IMAGE_PATH = os.path.join(BASE_DIR, "dpnp.png")
ZODIAC_PANEL_IMAGE_PATH = os.path.join(BASE_DIR, "dpnpzodiak.png")
REGIONAL_PANEL_IMAGE_PATH = os.path.join(BASE_DIR, "reginoal 3.png")
GENDER_PANEL_IMAGE_PATH = os.path.join(BASE_DIR, "gender.png")
GAME_ROLE_PANEL_IMAGE_PATH = os.path.join(BASE_DIR, "dpnpgameserverrole.png")
EXTRA_ROLE_PANEL_IMAGE_PATH = os.path.join(BASE_DIR, "dpnproleextra.png")

GAME_ROLE_EMOJI_SOURCES = [
    ("Mobile Legends", 1449602863687794789, "role_ml", os.path.join(BASE_DIR, "emojirolepanel1", "Mobile Legends.jpg"), "game_ml", "🎮"),
    ("Among Us", 1449603295046930443, "role_among", os.path.join(BASE_DIR, "emojirolepanel1", "among.png"), "game_among", "👽"),
    ("Roblox", 1449603377150562354, "role_roblox", os.path.join(BASE_DIR, "emojirolepanel1", "roblox.png"), "game_roblox", "🧱"),
    ("Free Fire", 1502158964857638924, "role_ff", os.path.join(BASE_DIR, "emojirolepanel1", "FreeFire.png"), "game_freefire", "🔥"),
    ("Steam Gaming", 1521860590526664844, "role_steam_igaming", os.path.join(BASE_DIR, "emojirolepanel1", "steamgaming.png"), "game_steam", "🖥️"),
    ("Valorant", 1521865058102149131, "role_valorant", os.path.join(BASE_DIR, "emojirolepanel1", "Valorant.jpg"), "game_valorant", "🔫"),
    ("Meccha Chameleon", 1533083014966284368, "role_meccha_chameleon", os.path.join(BASE_DIR, "emojirolepanel1", "mecccha chameleon.png"), "game_meccha_chameleon", "🦎"),
    ("PUBG", PUBG_ROLE_ID, "role_pubg", os.path.join(BASE_DIR, "emojirolepanel1", "pubg MObile.jpg"), "game_pubg", "🔫"),
    ("Clash of Clans", CLASH_OF_CLANS_ROLE_ID, "role_clashofclans", os.path.join(BASE_DIR, "emojirolepanel1", "Clash of Clans.png"), "game_clashofclans", "⚔️"),
    ("Dead by Daylight", DEAD_BY_DAYLIGHT_ROLE_ID, "role_deadbydaylight", os.path.join(BASE_DIR, "emojirolepanel1", "DeadbyDaylight.png"), "game_deadbydaylight", "🪓"),
    ("Minecraft", MINECRAFT_ROLE_ID, "role_minecraft", os.path.join(BASE_DIR, "emojirolepanel1", "minecraft.jpg"), "game_minecraft", "🧱"),
    ("E-football", E_FOOTBALL_ROLE_ID, "role_efootball", os.path.join(BASE_DIR, "emojirolepanel1", "efootball.jpg"), "game_efootball", "⚽"),
    ("Catur", CATUR_ROLE_ID, "role_catur", os.path.join(BASE_DIR, "emojirolepanel1", "catur.png"), "game_catur", "♟️"),
    ("Codename", CODENAME_ROLE_ID, "role_codename", os.path.join(BASE_DIR, "emojirolepanel1", "Codname.jpg"), "game_codename", "🎯"),
    ("LudoKing", LUDOKING_ROLE_ID, "role_ludoking", os.path.join(BASE_DIR, "emojirolepanel1", "Ludoking.png"), "game_ludoking", "🎲"),
]

EXTRA_ROLE_EMOJI_SOURCES = [
    ("Nobar", 1521857351651561595, "role_nobar", os.path.join(BASE_DIR, "emojirolepanel5", "nobar.png"), "extra_nobar", "🎥"),
    ("Announcements", 1533084663403511979, "role_announcements", os.path.join(BASE_DIR, "emojirolepanel5", "Announcements.png"), "extra_announcements", "📢"),
    ("Discord Ping", 1533105173793214726, "role_discord_ping", os.path.join(BASE_DIR, "emojirolepanel5", "Discord Ping.jpg"), "extra_discord_ping", "🔔"),
    ("Yapping", 1533084494687371264, "role_yapping", os.path.join(BASE_DIR, "emojirolepanel5", "Yapping.png"), "extra_yapping", "💬"),
]

GAME_ROLE_EMOJI_CACHE: dict[str, discord.Emoji | discord.PartialEmoji | str] = {}
REGIONAL_ROLE_EMOJI_CACHE: dict[str, discord.Emoji | discord.PartialEmoji | str] = {}
EXTRA_ROLE_EMOJI_CACHE: dict[str, discord.Emoji | discord.PartialEmoji | str] = {}
ZODIAC_ROLES = [
    ("Aquarius", 1532514717623648366, "♒"),
    ("Aries", 1532514788750655679, "♈"),
    ("Cancer", 1532514841334382752, "♋"),
    ("Capricorn", 1532514902378549328, "♑"),
    ("Gemini", 1532515009416925264, "♊"),
    ("Leo", 1532515040652165340, "♌"),
    ("Libra", 1532515100424929382, "♎"),
    ("Pisces", 1532515143819333843, "♓"),
    ("Sagitarius", 1532515243127738488, "♐"),
    ("Scorpio", 1532515310010236948, "♏"),
    ("Taurus", 1532515369569222676, "♉"),
    ("Virgo", 1532515408223928473, "♍"),
]
ZODIAC_ROLE_IDS = [role_id for _, role_id, _ in ZODIAC_ROLES]


def role_mention(guild: discord.Guild | None, role_id: int, fallback_name: str) -> str:
    if guild is None:
        return fallback_name
    role = guild.get_role(role_id)
    return role.mention if role else fallback_name


def remove_other_roles(guild: discord.Guild | None, member: discord.Member, role_ids: list[int], selected_role_id: int):
    if guild is None:
        return []
    roles = [guild.get_role(role_id) for role_id in role_ids]
    roles = [role for role in roles if role is not None]
    return [role for role in roles if role.id != selected_role_id and role in member.roles]

XP_FILE = "xp_data.json"
DAILY_XP = 50
genius = None

voice_join_time = {}
daily_claims = {}
last_message_time = {}
XP_COOLDOWN = 60

spam_records = {}
SPAM_WINDOW = 10
SPAM_THRESHOLD = 5

if os.path.exists(XP_FILE):
    with open(XP_FILE, "r") as f:
        xp_data = json.load(f)
else:
    xp_data = {}

def save_xp():
    with open(XP_FILE, "w") as f:
        json.dump(xp_data, f)

# ===== HELPER: PATH COOKIES =====
def get_ffmpeg_path():
    """Cari ffmpeg di system PATH atau lokasi umum."""
    # Cek PATH dulu
    ffmpeg = shutil.which('ffmpeg')
    if ffmpeg:
        print(f'[FFmpeg] Ditemukan di: {ffmpeg}')
        return ffmpeg
    # Cek lokasi umum di Railway/Linux
    candidates = [
        '/usr/bin/ffmpeg',
        '/usr/local/bin/ffmpeg',
        '/nix/store/ffmpeg',
    ]
    for path in candidates:
        if os.path.exists(path):
            print(f'[FFmpeg] Ditemukan di: {path}')
            return path
    # Coba cari di /nix/store (Railway pakai Nix)
    import glob
    nix_matches = glob.glob('/nix/store/*/bin/ffmpeg')
    if nix_matches:
        print(f'[FFmpeg] Ditemukan di Nix: {nix_matches[0]}')
        return nix_matches[0]
    print('[FFmpeg] WARNING: ffmpeg tidak ditemukan!')
    return 'ffmpeg'  # fallback ke PATH

def get_cookies_path():
    """Cari cookies.txt di beberapa lokasi, return path yang ada."""
    candidates = [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cookies.txt'),  # sama folder main.py
        '/app/cookies.txt',       # Railway default app root
        'cookies.txt',            # working directory
    ]
    for path in candidates:
        if os.path.exists(path):
            print(f"[Cookies] Ditemukan di: {path}")
            return path
    print("[Cookies] cookies.txt TIDAK ditemukan! YouTube mungkin block download.")
    return None

# ===== HELPER: YT-DLP OPTIONS =====
def get_ydl_opts(output_template='%(id)s.%(ext)s'):
    """Return yt-dlp options dengan cookies jika tersedia."""
    opts = {
        'format': 'bestaudio/best/worstaudio',
        'quiet': True,
        'noplaylist': True,
        'outtmpl': output_template,
        'extractor_args': {
            'youtube': {
                'player_client': ['ios', 'web'],
            }
        },
        'http_headers': {
            'User-Agent': 'com.google.ios.youtube/19.29.1 (iPhone16,2; U; CPU iOS 17_5_1 like Mac OS X;)',
        },
    }
    cookies_path = get_cookies_path()
    if cookies_path:
        opts['cookiefile'] = cookies_path
    return opts

# ================= FIXED BUTTON ROLE =================

# ================= MUSIC CONTROLS VIEW =================
class MusicControlView(View):
    def __init__(self, client, guild, channel):
        super().__init__(timeout=None)
        self.client = client
        self.guild = guild
        self.channel = channel

    @discord.ui.button(emoji="⏭️", label="Skip", style=discord.ButtonStyle.primary)
    async def skip_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        vc = self.guild.voice_client
        now = self.client.now_playing.get(self.guild.id)
        if vc and vc.is_playing():
            title = now["title"] if now else "lagu ini"
            vc.stop()
            await interaction.response.send_message(f"⏭️ Skipped: **{title}**", ephemeral=True)
        else:
            await interaction.response.send_message("❌ Tidak ada musik yang sedang diputar.", ephemeral=True)

    @discord.ui.button(emoji="⏸️", label="Pause", style=discord.ButtonStyle.secondary)
    async def pause_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        vc = self.guild.voice_client
        if vc and vc.is_playing():
            vc.pause()
            button.label = "Resume"
            button.emoji = "▶️"
            button.style = discord.ButtonStyle.success
            await interaction.response.edit_message(view=self)
        elif vc and vc.is_paused():
            vc.resume()
            button.label = "Pause"
            button.emoji = "⏸️"
            button.style = discord.ButtonStyle.secondary
            await interaction.response.edit_message(view=self)
        else:
            await interaction.response.send_message("❌ Tidak ada musik.", ephemeral=True)

    @discord.ui.button(emoji="⏹️", label="Stop", style=discord.ButtonStyle.danger)
    async def stop_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        vc = self.guild.voice_client
        if vc:
            self.client.music_queues[self.guild.id] = []
            self.client.now_playing[self.guild.id] = None
            vc.stop()
            for item in self.children:
                item.disabled = True
            await interaction.response.edit_message(view=self)
            await interaction.followup.send("⏹️ Musik dihentikan.", ephemeral=True)
        else:
            await interaction.response.send_message("❌ Bot tidak di voice channel.", ephemeral=True)

    @discord.ui.button(emoji="👋", label="Leave", style=discord.ButtonStyle.danger)
    async def leave_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        vc = self.guild.voice_client
        if vc:
            self.client.music_queues[self.guild.id] = []
            self.client.now_playing[self.guild.id] = None
            await vc.disconnect()
            for item in self.children:
                item.disabled = True
            await interaction.response.edit_message(view=self)
            await interaction.followup.send("👋 Bot keluar dari voice channel.", ephemeral=True)
        else:
            await interaction.response.send_message("❌ Bot tidak di voice channel.", ephemeral=True)


def _emoji_fallback_for_role(role_label: str) -> str:
    for label, _, _, _, _, fallback_emoji in GAME_ROLE_EMOJI_SOURCES:
        if label == role_label:
            return fallback_emoji
    return "🎮"


async def get_or_create_game_role_emoji(guild: discord.Guild, emoji_name: str, image_path: str, fallback_emoji: str):
    cached = GAME_ROLE_EMOJI_CACHE.get(f"{guild.id}:{emoji_name}")
    if cached is not None:
        return cached

    existing = discord.utils.get(guild.emojis, name=emoji_name)
    if existing is not None:
        GAME_ROLE_EMOJI_CACHE[f"{guild.id}:{emoji_name}"] = existing
        return existing

    if not os.path.exists(image_path):
        GAME_ROLE_EMOJI_CACHE[f"{guild.id}:{emoji_name}"] = fallback_emoji
        return fallback_emoji

    try:
        with open(image_path, "rb") as image_file:
            created = await guild.create_custom_emoji(name=emoji_name, image=image_file.read())
        GAME_ROLE_EMOJI_CACHE[f"{guild.id}:{emoji_name}"] = created
        return created
    except Exception:
        GAME_ROLE_EMOJI_CACHE[f"{guild.id}:{emoji_name}"] = fallback_emoji
        return fallback_emoji


async def build_game_role_options(guild: discord.Guild | None):
    options = []
    for label, role_id, _, image_path, emoji_name, fallback_emoji in GAME_ROLE_EMOJI_SOURCES:
        emoji_value = fallback_emoji
        if guild is not None:
            emoji_value = await get_or_create_game_role_emoji(guild, emoji_name, image_path, fallback_emoji)
        options.append(discord.SelectOption(label=label, value=str(role_id), emoji=emoji_value))
    return options


async def get_or_create_regional_role_emoji(guild: discord.Guild | None, role_label: str):
    if guild is None:
        return "🇲🇾" if role_label == "MALAYSIA" else None

    cache_key = f"{guild.id}:{role_label}"
    cached = REGIONAL_ROLE_EMOJI_CACHE.get(cache_key)
    if cached is not None:
        return cached

    if role_label != "MALAYSIA":
        for label, _, emoji in REGIONAL_ROLES:
            if label == role_label:
                REGIONAL_ROLE_EMOJI_CACHE[cache_key] = emoji
                return emoji
        return None

    emoji_name = "regional_malaysia"
    image_path = os.path.join(BASE_DIR, "malay.jpg")
    existing = discord.utils.get(guild.emojis, name=emoji_name)
    if existing is not None:
        REGIONAL_ROLE_EMOJI_CACHE[cache_key] = existing
        return existing

    if not os.path.exists(image_path):
        REGIONAL_ROLE_EMOJI_CACHE[cache_key] = "🇲🇾"
        return "🇲🇾"

    try:
        with open(image_path, "rb") as image_file:
            created = await guild.create_custom_emoji(name=emoji_name, image=image_file.read())
        REGIONAL_ROLE_EMOJI_CACHE[cache_key] = created
        return created
    except Exception:
        REGIONAL_ROLE_EMOJI_CACHE[cache_key] = "🇲🇾"
        return "🇲🇾"


async def build_regional_role_options(guild: discord.Guild | None):
    options = []
    for label, role_id, fallback_emoji in REGIONAL_ROLES:
        emoji_value = await get_or_create_regional_role_emoji(guild, label)
        if emoji_value is None:
            emoji_value = fallback_emoji
        options.append(discord.SelectOption(label=label, value=str(role_id), emoji=emoji_value))
    return options


class GameRoleSelect(discord.ui.Select):
    def __init__(self, options: list[discord.SelectOption]):
        super().__init__(
            placeholder="Pick one or more roles...",
            min_values=1,
            max_values=max(1, len(options)),
            options=options,
            custom_id="game_role_select",
        )

    async def callback(self, interaction: discord.Interaction):
        guild = interaction.guild
        member = interaction.user

        if guild is None:
            await interaction.response.send_message("Panel ini hanya bisa dipakai di server.", ephemeral=True)
            return

        selected_roles = []
        selected_names = []

        for selected_role_id_str in self.values:
            selected_role = guild.get_role(int(selected_role_id_str))
            if selected_role is None:
                continue
            selected_names.append(selected_role.name)
            if selected_role not in member.roles:
                selected_roles.append(selected_role)

        if not selected_roles:
            await interaction.response.send_message(
                f"Role yang dipilih sudah kamu punya: {', '.join(selected_names)}",
                ephemeral=True,
            )
            return

        await member.add_roles(*selected_roles)
        await interaction.response.send_message(
            f"✅ Role berhasil diberikan: {', '.join(role.name for role in selected_roles)}",
            ephemeral=True,
        )


class RoleButton(discord.ui.Button):
    def __init__(self, label: str, role_id: int, custom_id: str, emoji: str | None = None, row: int | None = None):
        super().__init__(
            label=label,
            style=discord.ButtonStyle.primary,
            custom_id=custom_id,
            emoji=emoji,
            row=row,
        )
        self.role_id = role_id

    async def callback(self, interaction: discord.Interaction):
        # Defer the interaction to avoid "didn't respond in time" when role actions take longer
        try:
            await interaction.response.defer(ephemeral=True)
        except Exception:
            # Already responded or cannot defer; continue anyway
            pass

        guild = interaction.guild
        if guild is None:
            try:
                await interaction.followup.send("Panel ini hanya bisa dipakai di server.", ephemeral=True)
            except Exception:
                pass
            return

        role = guild.get_role(self.role_id)
        if role is None:
            await interaction.followup.send("Role tidak ditemukan.", ephemeral=True)
            return

        member = interaction.user
        try:
            if role in getattr(member, 'roles', []):
                await member.remove_roles(role)
                await interaction.followup.send(f"❌ Role **{role.name}** dihapus dari kamu.", ephemeral=True)
            else:
                await member.add_roles(role)
                await interaction.followup.send(f"✅ Role **{role.name}** berhasil diberikan!", ephemeral=True)
        except discord.Forbidden:
            await interaction.followup.send("Bot tidak punya izin untuk mengubah role.", ephemeral=True)
        except Exception as e:
            await interaction.followup.send(f"Terjadi error saat mengubah role: {e}", ephemeral=True)


class RolePanel(View):
    def __init__(self, options: list[discord.SelectOption]):
        super().__init__(timeout=None)
        self.add_item(GameRoleSelect(options))


class PrincessInfoButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="Princess",
            style=discord.ButtonStyle.primary,
            custom_id="rolepanel2_princess_info"
        )

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Info Princess",
            description="Role Princess perlu verif ke admin/mod.",
            color=discord.Color.pink()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)


class RolePanel2(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RoleButton("Prince", PRINCE_ROLE_ID, "role_prince"))
        self.add_item(PrincessInfoButton())


class ZodiacRoleSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label=name, value=str(role_id), emoji=emoji)
            for name, role_id, emoji in ZODIAC_ROLES
        ]
        super().__init__(
            placeholder="Pilih satu role zodiak...",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="zodiac_role_select"
        )

    async def callback(self, interaction: discord.Interaction):
        guild = interaction.guild
        member = interaction.user

        if guild is None:
            await interaction.response.send_message("Panel ini hanya bisa dipakai di server.", ephemeral=True)
            return

        selected_role_id = int(self.values[0])
        selected_role = guild.get_role(selected_role_id)
        if selected_role is None:
            await interaction.response.send_message("Role zodiak tidak ditemukan.", ephemeral=True)
            return

        zodiac_roles = [guild.get_role(role_id) for role_id in ZODIAC_ROLE_IDS]
        zodiac_roles = [role for role in zodiac_roles if role is not None]

        roles_to_remove = [role for role in zodiac_roles if role.id != selected_role_id and role in member.roles]
        if roles_to_remove:
            await member.remove_roles(*roles_to_remove)

        if selected_role in member.roles:
            message = f"Kamu sudah punya role **{selected_role.name}**. Role zodiak lain sudah disesuaikan."
        else:
            await member.add_roles(selected_role)
            message = f"✅ Role **{selected_role.name}** berhasil diberikan!"

        await interaction.response.send_message(message, ephemeral=True)


class ZodiacRolePanel(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(ZodiacRoleSelect())


class RegionalRoleSelect(discord.ui.Select):
    def __init__(self, options: list[discord.SelectOption]):
        super().__init__(
            placeholder="Pilih satu role regional...",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="regional_role_select"
        )

    async def callback(self, interaction: discord.Interaction):
        guild = interaction.guild
        member = interaction.user

        if guild is None:
            await interaction.response.send_message("Panel ini hanya bisa dipakai di server.", ephemeral=True)
            return

        selected_role_id = int(self.values[0])
        selected_role = guild.get_role(selected_role_id)
        if selected_role is None:
            await interaction.response.send_message("Role regional tidak ditemukan.", ephemeral=True)
            return

        roles_to_remove = remove_other_roles(guild, member, REGIONAL_ROLE_IDS, selected_role_id)
        if roles_to_remove:
            await member.remove_roles(*roles_to_remove)

        if selected_role in member.roles:
            message = f"Kamu sudah punya role **{selected_role.name}**. Role regional lain sudah disesuaikan."
        else:
            await member.add_roles(selected_role)
            message = f"✅ Role **{selected_role.name}** berhasil diberikan!"

        await interaction.response.send_message(message, ephemeral=True)


class RegionalRolePanel(View):
    def __init__(self, options: list[discord.SelectOption]):
        super().__init__(timeout=None)
        self.add_item(RegionalRoleSelect(options))


async def get_or_create_extra_role_emoji(guild: discord.Guild | None, emoji_name: str, image_path: str, fallback_emoji: str):
    if guild is None:
        return fallback_emoji

    cache_key = f"{guild.id}:{emoji_name}"
    cached = EXTRA_ROLE_EMOJI_CACHE.get(cache_key)
    if cached is not None:
        return cached

    existing = discord.utils.get(guild.emojis, name=emoji_name)
    if existing is not None:
        EXTRA_ROLE_EMOJI_CACHE[cache_key] = existing
        return existing

    if not os.path.exists(image_path):
        EXTRA_ROLE_EMOJI_CACHE[cache_key] = fallback_emoji
        return fallback_emoji

    try:
        with open(image_path, "rb") as image_file:
            created = await guild.create_custom_emoji(name=emoji_name, image=image_file.read())
        EXTRA_ROLE_EMOJI_CACHE[cache_key] = created
        return created
    except Exception:
        EXTRA_ROLE_EMOJI_CACHE[cache_key] = fallback_emoji
        return fallback_emoji


async def build_extra_role_options(guild: discord.Guild | None):
    options = []
    for label, role_id, _, image_path, emoji_name, fallback_emoji in EXTRA_ROLE_EMOJI_SOURCES:
        emoji_value = await get_or_create_extra_role_emoji(guild, emoji_name, image_path, fallback_emoji)
        options.append(discord.SelectOption(label=label, value=str(role_id), emoji=emoji_value))
    return options


class ExtraRoleSelect(discord.ui.Select):
    def __init__(self, options: list[discord.SelectOption]):
        super().__init__(
            placeholder="Pick one or more roles...",
            min_values=1,
            max_values=max(1, len(options)),
            options=options,
            custom_id="extra_role_select",
        )

    async def callback(self, interaction: discord.Interaction):
        guild = interaction.guild
        member = interaction.user

        if guild is None:
            await interaction.response.send_message("Panel ini hanya bisa dipakai di server.", ephemeral=True)
            return

        selected_roles = []
        selected_names = []

        for selected_role_id_str in self.values:
            selected_role = guild.get_role(int(selected_role_id_str))
            if selected_role is None:
                continue
            selected_names.append(selected_role.name)
            if selected_role not in member.roles:
                selected_roles.append(selected_role)

        if not selected_roles:
            await interaction.response.send_message(
                f"Role yang dipilih sudah kamu punya: {', '.join(selected_names)}",
                ephemeral=True,
            )
            return

        await member.add_roles(*selected_roles)
        await interaction.response.send_message(
            f"✅ Role berhasil diberikan: {', '.join(role.name for role in selected_roles)}",
            ephemeral=True,
        )


class ExtraRolePanel(View):
    def __init__(self, options: list[discord.SelectOption]):
        super().__init__(timeout=None)
        self.add_item(ExtraRoleSelect(options))


def make_role_panel_embed(title: str, description: str, color: discord.Color, image_url: str = "") -> discord.Embed:
    embed = discord.Embed(
        title=title,
        description=description,
        color=color
    )
    if image_url:
        embed.set_image(url=image_url)
    return embed


def load_role_panel_image(image_path: str, attachment_name: str):
    if os.path.exists(image_path):
        return discord.File(image_path, filename=attachment_name), f"attachment://{attachment_name}"
    return None, ""


class Client(discord.Client):
    music_queues = {}
    now_playing = {}

    async def on_error(self, event, *args, **kwargs):
        print(f"[Discord] Error pada event {event}:")
        traceback.print_exc()
        await super().on_error(event, *args, **kwargs)

    async def play_next(self, guild, channel, message_channel):
        queue = self.music_queues.get(guild.id, [])
        if queue:
            next_track = queue.pop(0)
            self.music_queues[guild.id] = queue
            vc = guild.voice_client
            if not vc:
                vc = await channel.connect()

            ffmpeg_opts = {
                'before_options': '',
                'options': '-vn'
            }
            audio_source = discord.FFmpegPCMAudio(
                executable=get_ffmpeg_path(),
                source=next_track['filename'],
                **ffmpeg_opts
            )
            # Set now playing and actually play the track
            try:
                self.now_playing[guild.id] = next_track

                def _after_play(error):
                    if error:
                        print(f"[Music] Playback error: {error}")
                    try:
                        asyncio.run_coroutine_threadsafe(
                            self._on_track_end(guild, channel, message_channel, next_track),
                            self.loop
                        )
                    except Exception as e:
                        print("[Music] Failed schedule next track:", e)

                vc.play(audio_source, after=_after_play)
                await message_channel.send(f"▶️ Now Playing: **{next_track.get('title', 'Unknown')}**")
            except Exception as e:
                print("[Music] Gagal memulai pemutaran:", e)
                # schedule next track attempt
                try:
                    asyncio.run_coroutine_threadsafe(self.play_next(guild, channel, message_channel), self.loop)
                except Exception:
                    pass

    async def _on_track_end(self, guild, channel, message_channel, played_track):
        # cleanup file if exists
        try:
            filename = played_track.get('filename')
            if filename and os.path.exists(filename):
                try:
                    os.remove(filename)
                except Exception:
                    pass
        except Exception:
            pass

        # clear now playing
        try:
            self.now_playing[guild.id] = None
        except Exception:
            pass

        # play next if queue has items
        queue = self.music_queues.get(guild.id, [])
        if queue:
            await self.play_next(guild, channel, message_channel)

    # ===== HELPER: DOWNLOAD DENGAN FALLBACK =====
    async def download_track(self, query, is_url=False):
        """Coba YouTube dulu, kalau gagal fallback ke SoundCloud."""
        import yt_dlp

        # === Coba YouTube dulu (tanpa cookies supaya error bisa di-catch) ===
        ydl_opts_yt = {
            'format': 'bestaudio/best',
            'quiet': True,
            'noplaylist': True,
            'outtmpl': '%(id)s.%(ext)s',
            'extractor_args': {
                'youtube': {
                    'player_client': ['ios', 'web'],
                }
            },
            'http_headers': {
                'User-Agent': 'com.google.ios.youtube/19.29.1 (iPhone16,2; U; CPU iOS 17_5_1 like Mac OS X;)',
            },
        }
        if not is_url:
            ydl_opts_yt['default_search'] = 'ytsearch1'

        # Coba dengan cookies dulu
        cookies_path = get_cookies_path()
        if cookies_path:
            ydl_opts_yt['cookiefile'] = cookies_path

        yt_success = False
        try:
            with yt_dlp.YoutubeDL(ydl_opts_yt) as ydl:
                info = ydl.extract_info(query, download=True)
                if info is None:
                    raise Exception("YouTube return None")
                if 'entries' in info:
                    info = info['entries'][0]
                if info is None:
                    raise Exception("YouTube entries kosong")
                filename = ydl.prepare_filename(info)
                print(f"[Music] YouTube OK: {info['title']}")
                yt_success = True
                return info, filename, 'YouTube'
        except Exception as e:
            err_str = str(e)
            print(f"[Music] YouTube gagal: {err_str[:200]} — mencoba SoundCloud...")

        # === Fallback SoundCloud ===
        search_query = query
        # Kalau query adalah URL YouTube, coba ambil judulnya untuk dicari di SC
        if is_url and ('youtube.com' in query or 'youtu.be' in query):
            try:
                ydl_info_opts = {
                    'quiet': True,
                    'skip_download': True,
                    'extractor_args': {'youtube': {'player_client': ['ios']}},
                }
                if cookies_path:
                    ydl_info_opts['cookiefile'] = cookies_path
                with yt_dlp.YoutubeDL(ydl_info_opts) as ydl:
                    info_only = ydl.extract_info(query, download=False)
                    if info_only:
                        search_query = info_only.get('title', query)
                        print(f"[Music] Judul dari YT URL: {search_query}")
            except:
                search_query = query

        ydl_opts_sc = {
            'format': 'bestaudio/best',
            'quiet': True,
            'noplaylist': True,
            'outtmpl': '%(id)s.%(ext)s',
            'default_search': 'scsearch1',
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts_sc) as ydl:
                info = ydl.extract_info(search_query, download=True)
                if info is None:
                    raise Exception("SoundCloud return None")
                if 'entries' in info:
                    info = info['entries'][0]
                if info is None:
                    raise Exception("SoundCloud entries kosong")
                filename = ydl.prepare_filename(info)
                print(f"[Music] SoundCloud OK: {info['title']}")
                return info, filename, 'SoundCloud'
        except Exception as e:
            print(f"[Music] SoundCloud juga gagal: {e}")
            raise Exception("YouTube & SoundCloud gagal. Coba lagu lain.")

    # ===== SEARCH & PLAY (!d command) =====
    async def search_and_play(self, message, query):
        if not message.author.voice:
            await message.channel.send("❌ Kamu harus join voice channel dulu!")
            return

        status_msg = await message.channel.send("🔍 Mencari lagu...")

        try:
            info, filename, source = await self.download_track(query, is_url=False)
        except Exception as e:
            await status_msg.edit(content=f"❌ Gagal memutar lagu: {str(e)[:400]}")
            return

        await status_msg.delete()

        channel = message.author.voice.channel
        queue = self.music_queues.setdefault(message.guild.id, [])
        queue.append({
            'title': info['title'],
            'filename': filename,
            'webpage_url': info.get('webpage_url'),
            'uploader': info.get('uploader', source),
            'source': source
        })
        self.music_queues[message.guild.id] = queue

        if not message.guild.voice_client or not message.guild.voice_client.is_playing():
            await self.play_next(message.guild, channel, message.channel)
        else:
            await message.channel.send(f"➕ Ditambahkan ke antrian: {info['title']}")

    # ===== PLAY BY URL (!play command) =====
    async def play_music(self, message, url):
        if not message.author.voice:
            await message.channel.send("❌ Kamu harus join voice channel dulu!")
            return

        status_msg = await message.channel.send("⏳ Memuat lagu...")

        try:
            info, filename, source = await self.download_track(url, is_url=True)
        except Exception as e:
            await status_msg.edit(content=f"❌ Gagal memutar lagu: {str(e)[:400]}")
            return

        await status_msg.delete()

        channel = message.author.voice.channel
        queue = self.music_queues.setdefault(message.guild.id, [])
        queue.append({
            'title': info['title'],
            'filename': filename,
            'webpage_url': info.get('webpage_url'),
            'uploader': info.get('uploader', source),
            'source': source
        })
        self.music_queues[message.guild.id] = queue

        if not message.guild.voice_client or not message.guild.voice_client.is_playing():
            await self.play_next(message.guild, channel, message.channel)
        else:
            await message.channel.send(f"➕ Ditambahkan ke antrian: {info['title']}")

    # ===== MUSIC CONTROLS =====
    async def join_voice(self, message):
        if message.author.voice:
            channel = message.author.voice.channel
            await channel.connect()
            await message.channel.send(f"✅ Bergabung ke voice channel: {channel.name}")
        else:
            await message.channel.send("❌ Kamu harus join voice channel dulu!")

    async def leave_voice(self, message):
        if message.guild.voice_client:
            self.music_queues[message.guild.id] = []
            self.now_playing[message.guild.id] = None
            await message.guild.voice_client.disconnect()
            await message.channel.send("👋 Bot keluar dari voice channel dan antrian dikosongkan.")
        else:
            await message.channel.send("❌ Bot tidak sedang di voice channel.")

    async def stop_music(self, message):
        vc = message.guild.voice_client
        if vc and vc.is_playing():
            vc.stop()
            self.music_queues[message.guild.id] = []
            self.now_playing[message.guild.id] = None
            await message.channel.send("⏹️ Musik dihentikan dan antrian dikosongkan.")
        else:
            await message.channel.send("❌ Tidak ada musik yang sedang diputar.")

    async def skip_music(self, message):
        vc = message.guild.voice_client
        now = self.now_playing.get(message.guild.id)
        if vc and vc.is_playing():
            title = now["title"] if now else "lagu ini"
            vc.stop()  # akan trigger play_next otomatis lewat after callback
            await message.channel.send(f"⏭️ Skipped: **{title}**")
        else:
            await message.channel.send("❌ Tidak ada musik yang sedang diputar.")

    async def remove_track(self, message, index):
        queue = self.music_queues.get(message.guild.id, [])
        if not queue:
            await message.channel.send("❌ Antrian kosong.")
            return
        if index < 1 or index > len(queue):
            await message.channel.send(f"❌ Nomor tidak valid. Antrian punya {len(queue)} lagu.")
            return
        removed = queue.pop(index - 1)
        self.music_queues[message.guild.id] = queue
        await message.channel.send(f"🗑️ Dihapus dari antrian: **{removed['title']}**")

    def __init__(self, *, intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

        @self.tree.command(name="help", description="Lihat semua fitur DPNP Bot")
        async def help_command(interaction: discord.Interaction):
            embed = discord.Embed(title="DPNP Bot Help", color=discord.Color.blurple())
            embed.add_field(name="Musik", value="!play [link_youtube]\n!d [judul lagu]\n!stop\n!join\n!leave\n!queue\n/queue", inline=False)
            embed.add_field(name="XP", value="!profile\n!daily", inline=False)
            embed.add_field(name="Role", value="/rolepanel (game role)\n/rolepanel3 (zodiak)\n/rolepanel4 (regional)\n/rolepanel5 (role extra)\n!pubg\n!clashofclans\n!deadbydaylight\n!minecraft\n!efootball\n!catur\n!cm", inline=False)
            embed.add_field(name="Fun", value="!kiss, !slap, !hug, !bite, !pat, !kill", inline=False)
            embed.set_footer(text="DPNP Bot by wuwa5741-art")
            await interaction.response.send_message(embed=embed, ephemeral=True)

        @self.tree.command(name="queue", description="Lihat antrian lagu saat ini")
        async def queue_command(interaction: discord.Interaction):
            queue = self.music_queues.get(interaction.guild_id, [])
            now = self.now_playing.get(interaction.guild_id)
            desc = ""
            if now:
                desc += f"▶️ Now Playing: {now['title']}\n"
            if queue:
                for idx, track in enumerate(queue, 1):
                    desc += f"{idx}. {track['title']}\n"
            else:
                desc += "(Antrian kosong)"
            embed = discord.Embed(title="Music Queue", description=desc, color=discord.Color.orange())
            await interaction.response.send_message(embed=embed)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        print(f"[Startup] message_content intent: {self.intents.message_content}")
        # Cek cookies saat startup
        cookies_path = get_cookies_path()
        if cookies_path:
            print(f"[Startup] cookies.txt OK: {cookies_path}")
        else:
            print("[Startup] WARNING: cookies.txt tidak ditemukan!")

        try:
            startup_guild = self.guilds[0] if self.guilds else None
            startup_options = await build_game_role_options(startup_guild)
            self.add_view(RolePanel(startup_options))
            print("Persistent RolePanel loaded")
            # Register RolePanel2 as persistent so Prince/Princess buttons work after restarts
            try:
                self.add_view(RolePanel2())
                print("Persistent RolePanel2 loaded")
            except Exception as e:
                print("Gagal load RolePanel2:", e)
            self.add_view(ZodiacRolePanel())
            print("Persistent ZodiacRolePanel loaded")
            regional_options = await build_regional_role_options(startup_guild)
            self.add_view(RegionalRolePanel(regional_options))
            print("Persistent RegionalRolePanel loaded")
            extra_options = await build_extra_role_options(startup_guild)
            self.add_view(ExtraRolePanel(extra_options))
            print("Persistent ExtraRolePanel loaded")
        except Exception as e:
            print("Gagal load RolePanel:", e)

    # ===== XP FUNCTION =====
    def add_xp(self, member, amount):
        user_id = str(member.id)
        if user_id not in xp_data:
            xp_data[user_id] = {"xp": 0, "level": 1}
        xp_data[user_id]["xp"] += amount
        level = xp_data[user_id]["level"]
        xp_needed = level * 100
        if xp_data[user_id]["xp"] >= xp_needed:
            xp_data[user_id]["xp"] -= xp_needed
            xp_data[user_id]["level"] += 1
            save_xp()
            return True
        save_xp()
        return False

    # ================= VOICE XP =================
    async def on_voice_state_update(self, member, before, after):
        return

    # ================= WELCOME =================
    async def on_member_join(self, member):
        channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
        if channel:
            welcome_file, welcome_image_url = load_role_panel_image(WELCOME_GOODBYE_IMAGE_PATH, "dpnp-welcome.png")
            embed = discord.Embed(
                title="Selamat Datang",
                description=f"Halo {member.mention}, selamat datang di DPNP. Semoga enjoy!",
                color=discord.Color.blue()
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            if welcome_image_url:
                embed.set_image(url=welcome_image_url)
            if welcome_file:
                await channel.send(embed=embed, file=welcome_file)
            else:
                await channel.send(embed=embed)

        rules_channel = member.guild.get_channel(RULES_CHANNEL_ID)
        take_role_channel = member.guild.get_channel(TAKE_ROLE_CHANNEL_ID)
        rules_mention = rules_channel.mention if rules_channel else 'rules'
        take_role_mention = take_role_channel.mention if take_role_channel else 'take role'

        greet_channel = member.guild.get_channel(JOIN_GREET_CHANNEL_ID)
        if greet_channel:
            await greet_channel.send(
                f"Halo {member.mention}, selamat datang di DPNP. Semoga enjoy! Cek {rules_mention} dan ambil role di {take_role_mention} ya."
            )

        role = member.guild.get_role(AUTO_ROLE_ID)
        if role:
            try:
                await member.add_roles(role)
            except discord.Forbidden:
                print("Tidak punya izin kasih role")

        try:
            await member.send(f"Hai {member.name}, selamat datang di {member.guild.name}! 🎊")
        except:
            pass

        if rules_channel:
            try:
                embed = discord.Embed(
                    title=f"Selamat datang di {member.guild.name} 🎉",
                    description=(
                        f"Halo {member.name}, selamat datang!\n"
                        f"Baca {rules_mention} dulu, lalu ambil role di {take_role_mention}.\n"
                        f"Semoga betah di sini."
                    ),
                    color=discord.Color.blue()
                )
                embed.set_thumbnail(url=member.guild.icon.url if member.guild.icon else None)
                await member.send(embed=embed)
            except:
                print(f"Gagal kirim DM ke {member.name}")

    # ================= GOODBYE =================
    async def on_member_remove(self, member):
        channel = member.guild.get_channel(GOODBYE_CHANNEL_ID)
        if channel:
            goodbye_file, goodbye_image_url = load_role_panel_image(WELCOME_GOODBYE_IMAGE_PATH, "dpnp-goodbye.png")
            embed = discord.Embed(
                title="Bye Bye",
                description=f"{member.name} telah keluar dari DPNP. Bye bye, semoga kita bertemu lagi!",
                color=discord.Color.red()
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            if goodbye_image_url:
                embed.set_image(url=goodbye_image_url)
            if goodbye_file:
                await channel.send(embed=embed, file=goodbye_file)
            else:
                await channel.send(embed=embed)

        try:
            dm_embed = discord.Embed(
                title="Bye Bye",
                description=(
                    f"Hai {member.name},\n\n"
                    f"Bye bye, semoga kita bertemu lagi di DPNP.\n"
                    f"Semoga hal-hal baik selalu datang ke kamu.\n\n"
                    f"Pintu kami selalu terbuka kalau suatu saat mau kembali ✨"
                ),
                color=discord.Color.dark_blue()
            )
            dm_embed.set_footer(text="Salam dari komunitas DPNP")
            await member.send(embed=dm_embed)
        except discord.Forbidden:
            print(f"Tidak bisa kirim DM ke {member.name}")

    # ================= Booster =================
    async def on_member_update(self, before, after):
        if before.premium_since is None and after.premium_since is not None:
            channel = after.guild.get_channel(BOOST_CHANNEL_ID)
            if channel:
                embed = discord.Embed(
                    title="🚀 SERVER BOOST!",
                    description=f"Terima kasih {after.mention} sudah boost **{after.guild.name}**! 💜",
                    color=discord.Color.purple()
                )
                embed.add_field(name="Total Boost Server", value=after.guild.premium_subscription_count)
                embed.set_thumbnail(url=after.display_avatar.url)
                await channel.send(embed=embed)

            role = after.guild.get_role(BOOSTER_ROLE_ID)
            if role:
                try:
                    await after.add_roles(role)
                except discord.Forbidden:
                    print("Tidak punya izin kasih role booster")

            try:
                await after.send(f"Terima kasih sudah boost {after.guild.name}! Kamu dapat role spesial 💜")
            except:
                pass

        if before.guild.premium_tier < after.guild.premium_tier:
            channel = after.guild.get_channel(BOOST_CHANNEL_ID)
            if channel:
                await channel.send(
                    f"@everyone 🎉 Server naik ke **LEVEL {after.guild.premium_tier}** berkat para booster! Terima kasih 💜"
                )

    # ================= COMMAND =================
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.author.bot:
            return

        msg = message.content.strip().lower()
        if msg.startswith('!!'):
            msg = msg[1:]

        # ===== MUSIC COMMANDS =====
        if msg.startswith('!join'):
            await self.join_voice(message)
            return
        elif msg.startswith('!leave'):
            await self.leave_voice(message)
            return
        elif msg.startswith('!play '):
            url = message.content.split(' ', 1)[1]
            await self.play_music(message, url)
            return
        elif msg.startswith('!stop'):
            await self.stop_music(message)
            return
        elif msg.startswith('!d '):
            query = message.content.split(' ', 1)[1]
            await self.search_and_play(message, query)
            return
        elif msg.startswith('!skip'):
            await self.skip_music(message)
            return
        elif msg.startswith('!remove '):
            try:
                index = int(message.content.split(' ', 1)[1])
                await self.remove_track(message, index)
            except ValueError:
                await message.channel.send('❌ Pakai: !remove [nomor] contoh: !remove 2')
            return
        elif msg.startswith('!queue'):
            queue = self.music_queues.get(message.guild.id, [])
            now = self.now_playing.get(message.guild.id)
            desc = ""
            if now:
                desc += f"▶️ Now Playing: {now['title']}\n"
            if queue:
                for idx, track in enumerate(queue, 1):
                    desc += f"{idx}. {track['title']}\n"
            else:
                desc += "(Antrian kosong)"
            embed = discord.Embed(title="Music Queue", description=desc, color=discord.Color.orange())
            await message.channel.send(embed=embed)
            return

        # ===== XP SYSTEM CHAT =====
        now = datetime.datetime.now().timestamp()
        last_time = last_message_time.get(message.author.id, 0)

        secret_word_detected = "bran baik dan ganteng" in message.content.lower()
        xp_multiplier = 2 if secret_word_detected else 1

        if now - last_time >= XP_COOLDOWN:
            last_message_time[message.author.id] = now
            xp_gain = random.randint(5, 15) * xp_multiplier
            self.add_xp(message.author, xp_gain)

        if msg == '!halo':
            await message.channel.send('Halo juga! 👋')
        elif msg == '!pagi':
            await message.channel.send('morning jga udh sarapan blm')
        elif msg == '!turu':
            await message.channel.send('tidur ya jaga kesehatan mu')
        elif msg == '!ping':
            await message.channel.send('Pong! 🏓')
        elif msg == '!among':
            await message.channel.send(f"{role_mention(message.guild, AMONG_US_ROLE_ID, 'Among Us')} Ayo Among Us!")
        elif msg == '!pubg':
            await message.channel.send(f"{role_mention(message.guild, PUBG_ROLE_ID, 'PUBG')} Ayo PUBG!")
        elif msg == '!clashofclans':
            await message.channel.send(f"{role_mention(message.guild, CLASH_OF_CLANS_ROLE_ID, 'Clash of Clans')} Ayo Clash of Clans!")
        elif msg == '!deadbydaylight':
            await message.channel.send(f"{role_mention(message.guild, DEAD_BY_DAYLIGHT_ROLE_ID, 'Dead by Daylight')} Ayo Dead by Daylight!")
        elif msg == '!minecraft':
            await message.channel.send(f"{role_mention(message.guild, MINECRAFT_ROLE_ID, 'Minecraft')} Ayo Minecraft!")
        elif msg == '!efootball':
            await message.channel.send(f"{role_mention(message.guild, E_FOOTBALL_ROLE_ID, 'E-football')} Ayo E-football!")
        elif msg == '!catur':
            await message.channel.send(f"{role_mention(message.guild, CATUR_ROLE_ID, 'Catur')} Ayo Catur!")
        elif msg == '!cm':
            await message.channel.send(f"{role_mention(message.guild, CODENAME_ROLE_ID, 'Codename')} Ayo Codename main!")
        
        # ===== LIRIK COMMAND =====
        elif msg.startswith('!lirik '):
            if not genius:
                await message.channel.send('❌ Fitur lirik belum aktif. Admin perlu set GENIUS_TOKEN di .env')
                return
            query = message.content.split(' ', 1)[1]
            status_msg = await message.channel.send(f'🔎 Mencari lirik: **{query}** ...')
            try:
                song = genius.search_song(query)
                if song and song.lyrics:
                    # Bagi lirik jika terlalu panjang
                    lyrics = song.lyrics
                    if len(lyrics) > 1800:
                        await status_msg.edit(content=f'**{song.title}** by **{song.artist}**\n\n{lyrics[:1800]}... (lirik dipotong)')
                    else:
                        await status_msg.edit(content=f'**{song.title}** by **{song.artist}**\n\n{lyrics}')
                else:
                    await status_msg.edit(content='❌ Lirik tidak ditemukan.')
            except Exception as e:
                await status_msg.edit(content=f'❌ Error ambil lirik: {str(e)[:300]}')
            return
        elif msg == '!roblox':
            await message.channel.send(f"{role_mention(message.guild, ROBLOX_ROLE_ID, 'Roblox')} Langsung aja Roblox!")
        elif msg == '!epep':
            await message.channel.send(f"{role_mention(message.guild, FREE_FIRE_ROLE_ID, 'Free Fire')} Langsung aja Free Fire yang mau ikut!")
        elif msg == '!valo':
            await message.channel.send(f"{role_mention(message.guild, VALORANT_ROLE_ID, 'Valorant')} Langsung aja Valorant yang mau ikut!")
        elif msg == '!yuka':
            await message.channel.send('hallo kak cantik gmn kabarnya')
        elif msg == '!ryan':
            await message.channel.send('Hallo Ganteng')
        elif msg == '!kiwi':
            await message.channel.send('Apeeeeeeeeee')
        elif msg == '!ml':
            await message.channel.send(f"{role_mention(message.guild, MOBILE_LEGENDS_ROLE_ID, 'Mobile Legends')} Langsung aja ml yg mau ikut!")
        elif msg == '!gg':
            await message.channel.send('ga suka ara ara, sukanya rara')
        elif msg == '!brann':
            await message.channel.send('Hallo owner baik dan ganteng')
        elif msg == '!ludo':
            await message.channel.send(f"{role_mention(message.guild, LUDOKING_ROLE_ID, 'LudoKing')} Ayo ada king ludo ga disini selain brann")
        elif msg == '!king':
            await message.channel.send('diatas owner masih ada king')
        elif msg == '!maul':
            await message.channel.send('maul berak celana di sekolah')
        elif msg == '!yeay':
            await message.channel.send('adik terbaik sedipienpi ')
        elif msg == '!wann':
            await message.channel.send('wann Login ada yang mau minta gendong tuh')
        elif msg == '!itik':
            await message.channel.send('info roblox/ml  brannn')
        elif msg == '!putra':
            await message.channel.send('ytta')
        elif msg == '!diyana':
            await message.channel.send('Apakabar anak anak absen dlu satu satu')
        elif msg == '!bii':
            await message.channel.send('Hallo my Kisah 📖')
        elif msg == '!melar':
            await message.channel.send('di sok sok an lu')
        elif msg == '!caci':
            await message.channel.send('sayang moja')
        elif msg == '!mile':
            await message.channel.send('Ketua gengster, bikin gemeter🫦🫦')
        elif msg == '!wahyu':
            await message.channel.send('sehat sehat all, banyak olahraga')
        elif msg == '!natan':
            await message.channel.send('jarvis apakan dlu le biar ga apa kali')
        elif msg == '!amouw':
            await message.channel.send('karl milik amour')
        elif msg == '!malam':
            await message.channel.send('@everyone good night guys, mimpi indah semoga sehat selalu,  mimpiin aku yaaa')
        elif msg == '!rin':
            await message.channel.send('omakkkkk')
        elif msg == '!jikan':
            await message.channel.send('info sparing mole')
        elif msg == '!vann':
            await message.channel.send('pria ganteng idaman 😘😘😘')
        elif msg == '!shera':
            await message.channel.send('inpokan by1 ml')
        elif msg == '!karl':
            await message.channel.send('noo my kisah')
        elif msg == '!loping':
            await message.channel.send('karawang nih boss')
        elif msg == '!mojil':
            await message.channel.send('apasiii')
        elif msg == '!arul':
            await message.channel.send('karl suka ak dia bilang sendiri')
        elif msg == '!iloy':
            await message.channel.send('Iloy sayang Go Youn Jung')
        elif msg == '!sogili':
            await message.channel.send('mancing guys')
        elif msg == '!araa':
            await message.channel.send('adik ka bii')
        elif msg == '!zhaa':
            await message.channel.send('ZHA ANAK TEKNIK')
        elif msg == '!xeno':
            await message.channel.send('xeno pemutus ws')
        elif msg == '!alex':
            await message.channel.send('handsome man in this server')
        elif msg == '!henn':
            await message.channel.send('ceo mbg')
        elif msg == '!milaa':
            await message.channel.send('orang sibuk jangan diganggu')
        elif msg == '!hazel':
            await message.channel.send('Halo Perempuan Cantik dan Manis')
        elif msg == '!kajell':
            await message.channel.send('Hallo dengan Princess disini👋🏻')
        elif msg == '!kai':
            await message.channel.send('Halo halo bandung')
        elif msg == '!mila':
            await message.channel.send('sibuk jangan di ganggu')
        elif msg == '!ramaa':
            await message.channel.send('halo tuan muda jakarta')
        elif msg == '!kira':
            await message.channel.send('KETUA PEJANTAN TANGGUH')
        elif msg == '!ryn':
            await message.channel.send('hadir bagimana kabar kalian semua')




        elif msg.startswith('!profile'):
            member = message.mentions[0] if message.mentions else message.author
            roles = [role.mention for role in member.roles if role.name != "@everyone"]
            roles_text = ", ".join(roles) if roles else "Tidak punya role"
            embed = discord.Embed(
                title=f"👤 Profil {member.name}",
                color=member.color if member.color != discord.Color.default() else discord.Color.blue()
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.add_field(name="🆔 User ID", value=member.id, inline=False)
            embed.add_field(name="📛 Username", value=member.name, inline=False)
            embed.add_field(name="📅 Akun Dibuat", value=member.created_at.strftime("%d %B %Y"), inline=False)
            embed.add_field(name="📆 Gabung Server", value=member.joined_at.strftime("%d %B %Y"), inline=False)
            embed.add_field(name="🎭 Roles", value=roles_text, inline=False)
            await message.channel.send(embed=embed)

        elif msg.startswith('!kiss'):
            if message.mentions:
                target = message.mentions[0]
                gif_url = random.choice([
                    "https://media1.tenor.com/m/1fNT0SY5cjwAAAAd/nene-nene-amano.gif",
                    "https://media1.tenor.com/m/Fvwt33eN3hUAAAAC/anime-cute.gif",
                    "https://media1.tenor.com/m/iDQT9BjSSXsAAAAC/kimsoohyun-kimjiwon.gif"
                ])
                embed = discord.Embed(description=f"{message.author.mention} mencium {target.mention} 😘", color=discord.Color.pink())
                embed.set_image(url=gif_url)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Tag orangnya dulu ya 😉")

        elif msg.startswith('!slap'):
            if message.mentions:
                target = message.mentions[0]
                gif_url = random.choice([
                    "https://media1.tenor.com/m/bO1H2Zv_5doAAAAC/mai-mai-san.gif",
                    "https://media1.tenor.com/m/WYmal-WAnksAAAAd/yuzuki-mizusaka-nonoka-komiya.gif"
                ])
                embed = discord.Embed(description=f"{message.author.mention} menampar {target.mention} 🖐️", color=discord.Color.red())
                embed.set_image(url=gif_url)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Tag orangnya dulu ya 😉")

        elif msg.startswith('!hug'):
            if message.mentions:
                target = message.mentions[0]
                gif_url = "https://media1.tenor.com/m/G_IvONY8EFgAAAAC/aharen-san-anime-hug.gif"
                embed = discord.Embed(description=f"{message.author.mention} memeluk {target.mention} 🤗", color=discord.Color.green())
                embed.set_image(url=gif_url)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Tag orangnya dulu ya 😉")

        elif msg.startswith('!bite'):
            if message.mentions:
                target = message.mentions[0]
                gif_url = "https://c.tenor.com/8YpRZ4H7dWkAAAAC/anime-bite.gif"
                embed = discord.Embed(description=f"{message.author.mention} menggigit {target.mention} 😈", color=discord.Color.orange())
                embed.set_image(url=gif_url)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Tag orangnya dulu ya 😉")

        elif msg.startswith('!pat'):
            if message.mentions:
                target = message.mentions[0]
                gif_url = "https://c.tenor.com/LUqLUEvFZ8kAAAAC/anime-head-pat.gif"
                embed = discord.Embed(description=f"{message.author.mention} menepuk kepala {target.mention} 🥰", color=discord.Color.blurple())
                embed.set_image(url=gif_url)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Tag orangnya dulu ya 😉")

        elif msg.startswith('!kill'):
            if message.mentions:
                target = message.mentions[0]
                gif_url = random.choice([
                    "https://media.tenor.com/HqHu-BqxJUEAAAAi/anime-xd.gif",
                    "https://media1.tenor.com/m/230mTazmYVYAAAAC/anime-anime-boy.gif"
                ])
                embed = discord.Embed(description=f"{message.author.mention} menyerang {target.mention} ⚔️", color=discord.Color.dark_red())
                embed.set_image(url=gif_url)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Tag orangnya dulu ya 😉")

        elif msg == '!daily':
            today = datetime.date.today()
            last_claim = daily_claims.get(message.author.id)
            if last_claim == today:
                await message.channel.send("Kamu sudah ambil daily XP hari ini 🎁")
            else:
                daily_claims[message.author.id] = today
                self.add_xp(message.author, DAILY_XP)
                await message.channel.send(f"🎁 Kamu dapat {DAILY_XP} XP hari ini!")


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True

client = Client(intents=intents)

@client.tree.command(name="rolepanel", description="Kirim panel ambil role")
async def rolepanel(interaction: discord.Interaction):
    games_file, games_image_url = load_role_panel_image(GAMES_PANEL_IMAGE_PATH, "dpnpgameserverrole.png")
    game_options = await build_game_role_options(interaction.guild)
    embed = make_role_panel_embed(
        title="DPNP SERVER - GAME ROLES",
        description="Pilih satu atau banyak role game di bawah, lalu submit untuk ambil semuanya.",
        color=discord.Color.blurple(),
        image_url=games_image_url,
    )
    if games_file:
        await interaction.response.send_message(embed=embed, view=RolePanel(game_options), file=games_file)
    else:
        await interaction.response.send_message(embed=embed, view=RolePanel(game_options))


@client.tree.command(name="rolepanel2", description="Kirim panel info role princess")
async def rolepanel2(interaction: discord.Interaction):
    gender_file, gender_image_url = load_role_panel_image(GENDER_PANEL_IMAGE_PATH, "gender.png")
    embed = make_role_panel_embed(
        title="Verif Gender",
        description=(
            "Klik tombol sesuai yang ingin anda pilih\n\n"
            "🤵 Role prince menandakan bahwa anda adalah pria di server ini\n\n"
            "👸 Role princess menandakan bahwa anda adalah perempuan di server ini\n\n"
            "Note: Untuk Role princess sendiri anda bisa menghubungi @The Aristocracy untuk melakukan verifikasi bahwa nyaa memang benar benar princess silahkan create tiket melalui #❓︱help untuk terhubung dengan administrator server."
        ),
        color=discord.Color.pink(),
        image_url=gender_image_url,
    )
    if gender_file:
        await interaction.response.send_message(embed=embed, view=RolePanel2(), file=gender_file)
    else:
        await interaction.response.send_message(embed=embed, view=RolePanel2())


@client.tree.command(name="rolepanel3", description="Kirim panel role zodiak")
async def rolepanel3(interaction: discord.Interaction):
    zodiac_file, zodiac_image_url = load_role_panel_image(ZODIAC_PANEL_IMAGE_PATH, "dpnpzodiak.png")
    if not zodiac_image_url:
        zodiac_image_url = ZODIAC_PANEL_IMAGE_URL
    embed = make_role_panel_embed(
        title="DPNP SERVER - ZODIAC ROLES",
        description="Pilih satu role zodiak dari menu di bawah.",
        color=discord.Color.blurple(),
        image_url=zodiac_image_url,
    )
    if zodiac_file:
        await interaction.response.send_message(embed=embed, view=ZodiacRolePanel(), file=zodiac_file)
    else:
        await interaction.response.send_message(embed=embed, view=ZodiacRolePanel())


@client.tree.command(name="rolepanel4", description="Kirim panel role regional")
async def rolepanel4(interaction: discord.Interaction):
    regional_file, regional_image_url = load_role_panel_image(REGIONAL_PANEL_IMAGE_PATH, "dpnpregional.png")
    if not regional_image_url:
        regional_image_url = REGIONAL_PANEL_IMAGE_URL
    regional_options = await build_regional_role_options(interaction.guild)
    embed = make_role_panel_embed(
        title="DPNP SERVER - REGIONAL ROLES",
        description="Pilih satu role regional dari menu di bawah.",
        color=discord.Color.green(),
        image_url=regional_image_url,
    )
    if regional_file:
        await interaction.response.send_message(embed=embed, view=RegionalRolePanel(regional_options), file=regional_file)
    else:
        await interaction.response.send_message(embed=embed, view=RegionalRolePanel(regional_options))


@client.tree.command(name="rolepanel5", description="Kirim panel role extra")
async def rolepanel5(interaction: discord.Interaction):
    extra_file, extra_image_url = load_role_panel_image(EXTRA_ROLE_PANEL_IMAGE_PATH, "dpnproleextra.png")
    extra_options = await build_extra_role_options(interaction.guild)
    embed = make_role_panel_embed(
        title="DPNP SERVER - ROLE EXTRA",
        description="Pilih satu atau banyak role extra di bawah, lalu submit untuk ambil semuanya.",
        color=discord.Color.blurple(),
        image_url=extra_image_url,
    )
    if extra_file:
        await interaction.response.send_message(embed=embed, view=ExtraRolePanel(extra_options), file=extra_file)
    else:
        await interaction.response.send_message(embed=embed, view=ExtraRolePanel(extra_options))

if not TOKEN:
    raise RuntimeError("TOKEN belum di-set. Isi environment variable TOKEN di Railway.")

client.run(TOKEN)