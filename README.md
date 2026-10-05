# Discord Bot

A Discord bot project.

Command role/game:

- `!amour` — `karl milik amour`
- `!amouw` — `midlaner lucu disini`
- `!ludo`
- `/rolepanel` atau `/rolepanel1` untuk panel role game
- `/quickchatpanel` untuk mengatur command quick chat (khusus administrator)

## Quick Chat Panel

Administrator dapat menjalankan `/quickchatpanel` untuk membuka panel pengaturan:

- **Tambah**: membuat command baru, misalnya `!brann`, beserta responsnya.
- **Edit**: mengubah respons command yang sudah ada.
- **Hapus**: menghapus command.
- **Refresh**: memuat daftar terbaru pada panel.

Konfigurasi disimpan per server di `quick_chats.json` dan tidak dimasukkan ke Git.

## Role Panel Images

Banner gambar disimpan langsung di repository dan ikut disalin ke image Railway melalui `COPY . .` di `Dockerfile`.
Saat startup bot juga memeriksa aset panel dan menulis hasilnya ke log.

Environment variables berikut hanya diperlukan jika ingin memakai URL eksternal:

- `ZODIAC_PANEL_IMAGE_URL` for `rolepanel3`
- `REGIONAL_PANEL_IMAGE_URL` for `rolepanel4`
