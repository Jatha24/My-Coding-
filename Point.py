import pygame
import random

# Inisialisasi pygame
pygame.init()

# Konstanta
LEBAR_LAYAR = 800
TINGGI_LAYAR = 600
WARNA_HITAM = (0, 0, 0)
WARNA_PUTIH = (255, 255, 255)
WARNA_MERAH = (255, 0, 0)
WARNA_HIJAU = (0, 255, 0)

# Membuat layar
layar = pygame.display.set_mode((LEBAR_LAYAR, TINGGI_LAYAR))
pygame.display.set_caption("Game RPG Sederhana")

# Kelas untuk karakter pemain
class Pemain:
    def __init__(self):
        self.lebar = 50
        self.tinggi = 50
        self.x = LEBAR_LAYAR // 2
        self.y = TINGGI_LAYAR // 2
        self.kesehatan = 20

    def gambar(self):
        pygame.draw.rect(layar, WARNA_HIJAU, (self.x, self.y, self.lebar, self.tinggi))

# Kelas untuk musuh
class Musuh:
    def __init__(self):
        self.lebar = 50
        self.tinggi = 50
        self.x = random.randint(0, LEBAR_LAYAR - self.lebar)
        self.y = random.randint(0, TINGGI_LAYAR - self.tinggi)
        self.kesehatan = 50

    def gambar(self):
        pygame.draw.rect(layar, WARNA_MERAH, (self.x, self.y, self.lebar, self.tinggi))

# Fungsi untuk menampilkan teks
def tampilkan_teks(teks, ukuran, warna, x, y):
    font = pygame.font.Font(None, ukuran)
    surface = font.render(teks, True, warna)
    rect = surface.get_rect(center=(x, y))
    layar.blit(surface, rect)

# Fungsi utama
def main():
    clock = pygame.time.Clock()
    pemain = Pemain()
    musuh = Musuh()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Menggerakkan pemain
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and pemain.x > 0:
            pemain.x -= 5
        if keys[pygame.K_d] and pemain.x < LEBAR_LAYAR - pemain.lebar:
            pemain.x += 5
        if keys[pygame.K_w] and pemain.y > 0:
            pemain.y -= 5
        if keys[pygame.K_s] and pemain.y < TINGGI_LAYAR - pemain.tinggi:
            pemain.y += 5

        # Cek tabrakan dengan musuh
        if (pemain.x < musuh.x + musuh.lebar and
            pemain.x + pemain.lebar > musuh.x and
            pemain.y < musuh.y + musuh.tinggi and
            pemain.y + pemain.tinggi > musuh.y):
            pemain.kesehatan -= 1
            musuh.x = random.randint(0, LEBAR_LAYAR - musuh.lebar)
            musuh.y = random.randint(0, TINGGI_LAYAR - musuh.tinggi)

        # Cek kesehatan
        if pemain.kesehatan <= 0:
            game_over = True

        # Menggambar
        layar.fill(WARNA_PUTIH)
        pemain.gambar()
        musuh.gambar()
        tampilkan_teks(f"Kesehatan: {pemain.kesehatan}", 30, WARNA_HITAM, 100, 30)
        pygame.display.flip()

        # Mengatur frame rate
        clock.tick(30)

    # Menampilkan Game Over
    layar.fill(WARNA_PUTIH)
    tampilkan_teks("Game Over!", 74, WARNA_HITAM, LEBAR_LAYAR // 2, TINGGI_LAYAR // 2)
    pygame.display.flip()
    pygame.time.delay(2000)

    pygame.quit()

if __name__ == "__main__":
    main()