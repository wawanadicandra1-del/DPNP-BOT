# Discord Bot

A Discord bot project.

Command role/game:

- `!amouw` (nama lama `!amor` sudah tidak dipakai)
- `!ludo`
- `/rolepanel` atau `/rolepanel1` untuk panel role game

## Role Panel Images

Banner gambar disimpan langsung di repository dan ikut disalin ke image Railway melalui `COPY . .` di `Dockerfile`.
Saat startup bot juga memeriksa aset panel dan menulis hasilnya ke log.

Environment variables berikut hanya diperlukan jika ingin memakai URL eksternal:

- `ZODIAC_PANEL_IMAGE_URL` for `rolepanel3`
- `REGIONAL_PANEL_IMAGE_URL` for `rolepanel4`
