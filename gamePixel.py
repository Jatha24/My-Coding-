import pygame
import random

# Inisialisasi pygame
pygame.init()

# Konstanta
LEBAR_LAYAR = 800
TINGGI_LAYAR = 600
WARNA_PUTIH = (255, 255, 255)
WARNA_HITAM = (0, 0, 0)
WARNA_MERAH = (255, 0, 0)
WARNA_BIRU = (0, 0, 255)
KECEPATAN_RINTANGAN = 5

# Membuat layar
layar = pygame.display.set_mode((LEBAR_LAYAR, TINGGI_LAYAR))
pygame.display.set_caption("Game Menghindari Rintangan")

# Kelas untuk pemain
class Pemain:
    def __init__(self):
        self.lebar = 50
        self.tinggi = 50
        self.x = LEBAR_LAYAR // 2
        self.y = TINGGI_LAYAR - self.tinggi - 10

    def gambar(self):
        pygame.draw.rect(layar, WARNA_HITAM, (self.x, self.y, self.lebar, self.tinggi))

# Kelas untuk rintangan
class Rintangan:
    def __init__(self):
        self.lebar = random.randint(20, 100)
        self.tinggi = 20
        self.x = random.randint(0, LEBAR_LAYAR - self.lebar)
        self.y = 0

    def gambar(self):
        pygame.draw.rect(layar, WARNA_MERAH, (self.x, self.y, self.lebar, self.tinggi))

    def jatuh(self):
        self.y += KECEPATAN_RINTANGAN

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
    rintangan = Rintangan()
    skor = 0
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Menggerakkan pemain
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and pemain.x > 0:
            pemain.x -= 5
        if keys[pygame.K_RIGHT] and pemain.x < LEBAR_LAYAR - pemain.lebar:
            pemain.x += 5

        # Menggerakkan rintangan
        rintangan.jatuh()

        # Cek tabrakan
        if (rintangan.y + rintangan.tinggi > pemain.y and
            rintangan.x < pemain.x + pemain.lebar and
            rintangan.x + rintangan.lebar > pemain.x):
            game_over = True

        # Reset rintangan
        if rintangan.y > TINGGI_LAYAR:
            rintangan = Rintangan()
            skor += 1

        # Menggambar
        layar.fill(WARNA_PUTIH)
        pemain.gambar()
        rintangan.gambar()
        pygame.display.flip()

        # Mengatur frame rate
        clock.tick(30)

    # Animasi Game Over
    for i in range(50):
        layar.fill(WARNA_PUTIH)
        tampilkan_teks("Game Over!", 74, WARNA_BIRU, LEBAR_LAYAR // 2, TINGGI_LAYAR // 2)
        pygame.display.flip()
        pygame.time.delay(50)

    print(f"Game Over! Skor Anda: {skor}")
    pygame.quit()

if __name__ == "__main__":
    main()