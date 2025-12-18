import random
import time
import os
from datetime import datetime

class HauntedLogicGame:
    def __init__(self):
        self.lives = 3
        self.level = 1
        self.score = 0
        self.max_level = 10
        self.player_name = ""
        self.ghost_type = ""
        self.ghost_power = ""
        self.ghost_emoji = ""
        
        # Database hantu Indonesia
        self.ghosts = {
            "1": {
                "name": "KUNTILANAK",
                "desc": "Hantu wanita berambut panjang yang suka menakuti di malam hari",
                "power": "Tawa Mengerikan",
                "emoji": "👻"
            },
            "2": {
                "name": "POCONG",
                "desc": "Hantu berkafan putih yang melompat-lompat mencari korban",
                "power": "Lompatan Mistis",
                "emoji": "🧟"
            },
            "3": {
                "name": "GENDERUWO",
                "desc": "Hantu berbulu hitam dengan kekuatan supernatural yang mengerikan",
                "power": "Kekuatan Gaib",
                "emoji": "👹"
            }
        }
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_slow(self, text, delay=0.03):
        """Print text dengan efek mengetik"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def show_intro(self):
        """Intro cerita rumah hantu"""
        self.clear_screen()
        print("\n" + "="*60)
        print("👻" * 30)
        print("="*60)
        print()
        self.print_slow("       🏚️  SELAMAT DATANG DI RUMAH HANTU LOGIKA  🏚️")
        print()
        print("="*60)
        print("👻" * 30)
        print("="*60)
        time.sleep(1)
        
        self.clear_screen()
        print("\n🌙 MALAM YANG KELAM...\n")
        time.sleep(1)
        self.print_slow("Kamu tersesat di dalam rumah hantu yang terkutuk...")
        time.sleep(1)
        self.print_slow("Untuk keluar, kamu harus menyelesaikan teka-teki logika...")
        time.sleep(1)
        self.print_slow("Setiap jawaban salah akan mengurangi NYAWA mu...")
        time.sleep(1)
        self.print_slow("Jika nyawa habis... kamu akan TERJEBAK SELAMANYA! 💀")
        time.sleep(2)
    
    def login(self):
        """Login dan pilih karakter hantu"""
        self.clear_screen()
        print("\n" + "🔮" * 30)
        print("\n         🎭 TRANSFORMASI MENJADI HANTU 🎭\n")
        print("🔮" * 30 + "\n")
        
        self.player_name = input("👤 Siapa nama mu, pemberani? ").strip()
        if not self.player_name:
            self.player_name = "Penjelajah Misterius"
        
        print(f"\n🌟 Selamat datang, {self.player_name}!")
        time.sleep(1)
        print("\n💀 Kamu akan bertransformasi menjadi hantu untuk bertahan hidup...")
        time.sleep(1)
        
        print("\n" + "="*60)
        print("           🎭 PILIH JENIS HANTU MU 🎭")
        print("="*60 + "\n")
        
        for key, ghost in self.ghosts.items():
            print(f"{key}. {ghost['emoji']} {ghost['name']}")
            print(f"   📜 {ghost['desc']}")
            print(f"   ⚡ Kekuatan: {ghost['power']}")
            print()
        
        while True:
            choice = input("Pilih hantu mu (1/2/3): ").strip()
            if choice in self.ghosts:
                ghost = self.ghosts[choice]
                self.ghost_type = ghost['name']
                self.ghost_power = ghost['power']
                self.ghost_emoji = ghost['emoji']
                break
            else:
                print("❌ Pilihan tidak valid! Pilih 1, 2, atau 3\n")
        
        self.clear_screen()
        print("\n" + "✨" * 30)
        self.print_slow(f"\n🌀 TRANSFORMASI DIMULAI... 🌀")
        time.sleep(1)
        self.print_slow(f"\n{self.ghost_emoji} Kamu sekarang adalah {self.ghost_type}!")
        self.print_slow(f"⚡ Kekuatan: {self.ghost_power}")
        time.sleep(2)
    
    def display_status(self):
        """Tampilkan status pemain"""
        print("\n" + "🕷️ " * 30)
        print(f"  🏚️  RUMAH HANTU - RUANGAN KE-{self.level}  🏚️")
        print("🕷️ " * 30)
        print(f"\n{self.ghost_emoji} Hantu: {self.ghost_type} ({self.player_name})")
        print(f"❤️  Nyawa: {'💖' * self.lives}{'💔' * (3-self.lives)}")
        print(f"🚪 Ruangan: {self.level}/{self.max_level}")
        print(f"⭐ Skor: {self.score}")
        print("\n" + "🕸️ " * 30 + "\n")
    
    def negasi(self, p):
        """Operasi logika: Negasi"""
        return not p
    
    def konjungsi(self, p, q):
        """Operasi logika: Konjungsi (AND)"""
        return p and q
    
    def disjungsi(self, p, q):
        """Operasi logika: Disjungsi (OR)"""
        return p or q
    
    def implikasi(self, p, q):
        """Operasi logika: Implikasi"""
        return (not p) or q
    
    def biimplikasi(self, p, q):
        """Operasi logika: Biimplikasi"""
        return p == q
    
    def generate_question(self):
        """Generate soal dengan tema hantu"""
        p = random.choice([True, False])
        q = random.choice([True, False])
        
        p_str = "BENAR" if p else "SALAH"
        q_str = "BENAR" if q else "SALAH"
        
        # Pertanyaan dengan tema hantu
        scary_statements_p = [
            "Ada suara tangisan di kamar sebelah",
            "Pintu terbuka sendiri tengah malam",
            "Bayangan hitam melintas di koridor",
            "Lampu mati mendadak tanpa sebab",
            "Terdengar langkah kaki di loteng",
            "Cermin retak dengan sendirinya",
            "Suara ketukan di jendela",
            "Kabut hitam menutupi ruangan"
        ]
        
        scary_statements_q = [
            "Kamu harus segera lari",
            "Hantu sedang mendekat",
            "Kamu dalam bahaya",
            "Ada sesuatu di belakangmu",
            "Ruangan ini terkutuk",
            "Jiwamu terancam",
            "Kematian menghampiri",
            "Arwah gentayangan berkeliaran"
        ]
        
        stmt_p = random.choice(scary_statements_p)
        stmt_q = random.choice(scary_statements_q)
        
        if self.level <= 2:
            question = f"👻 NEGASI: '{stmt_p}' adalah {p_str}\n   Maka NEGASINYA adalah?"
            answer = self.negasi(p)
            explanation = f"¬{p_str} = {'BENAR' if answer else 'SALAH'}"
            
        elif self.level <= 4:
            question = f"👻 KONJUNGSI: '{stmt_p}' adalah {p_str} DAN\n   '{stmt_q}' adalah {q_str}\n   Maka hasilnya?"
            answer = self.konjungsi(p, q)
            explanation = f"{p_str} ∧ {q_str} = {'BENAR' if answer else 'SALAH'}"
            
        elif self.level <= 6:
            question = f"👻 DISJUNGSI: '{stmt_p}' adalah {p_str} ATAU\n   '{stmt_q}' adalah {q_str}\n   Maka hasilnya?"
            answer = self.disjungsi(p, q)
            explanation = f"{p_str} ∨ {q_str} = {'BENAR' if answer else 'SALAH'}"
            
        elif self.level <= 8:
            question = f"👻 IMPLIKASI: JIKA '{stmt_p}' adalah {p_str}\n   MAKA '{stmt_q}' adalah {q_str}\n   Hasilnya?"
            answer = self.implikasi(p, q)
            explanation = f"{p_str} → {q_str} = {'BENAR' if answer else 'SALAH'}"
            
        else:
            question = f"👻 BIIMPLIKASI: '{stmt_p}' adalah {p_str}\n   JIKA DAN HANYA JIKA '{stmt_q}' adalah {q_str}\n   Hasilnya?"
            answer = self.biimplikasi(p, q)
            explanation = f"{p_str} ↔ {q_str} = {'BENAR' if answer else 'SALAH'}"
        
        return question, answer, explanation
    
    def show_tutorial(self):
        """Tampilkan tutorial logika matematika"""
        self.clear_screen()
        print("\n" + "📖" * 30)
        print("    📚 BUKU MANTRA LOGIKA MATEMATIKA 📚")
        print("📖" * 30 + "\n")
        
        print("1. 🔮 NEGASI (¬): Kebalikan dari pernyataan")
        print("   ¬BENAR = SALAH | ¬SALAH = BENAR\n")
        
        print("2. 🔮 KONJUNGSI (∧): DAN - Benar jika KEDUA benar")
        print("   BENAR ∧ BENAR = BENAR | Lainnya = SALAH\n")
        
        print("3. 🔮 DISJUNGSI (∨): ATAU - Benar jika SALAH SATU benar")
        print("   SALAH ∨ SALAH = SALAH | Lainnya = BENAR\n")
        
        print("4. 🔮 IMPLIKASI (→): Jika...maka...")
        print("   BENAR → SALAH = SALAH | Lainnya = BENAR\n")
        
        print("5. 🔮 BIIMPLIKASI (↔): Jika dan hanya jika")
        print("   Keduanya SAMA = BENAR | Berbeda = SALAH\n")
        
        print("📖" * 30)
        input("\n⚡ Tekan Enter untuk memasuki rumah hantu...")
    
    def play(self):
        """Main game loop"""
        self.show_intro()
        self.login()
        self.show_tutorial()
        
        while self.lives > 0 and self.level <= self.max_level:
            self.clear_screen()
            self.display_status()
            
            question, correct_answer, explanation = self.generate_question()
            
            print(f"🚪 RUANGAN KE-{self.level}:\n")
            print(f"   {question}\n")
            print("   1. BENAR ✓")
            print("   2. SALAH ✗")
            print()
            
            try:
                choice = input(f"{self.ghost_emoji} Jawaban mu (1/2): ").strip()
                
                if choice == "1":
                    user_answer = True
                elif choice == "2":
                    user_answer = False
                else:
                    print("\n❌ Pilihan tidak valid! Pilih 1 atau 2")
                    time.sleep(2)
                    continue
                
                if user_answer == correct_answer:
                    print(f"\n✅ BENAR! {explanation}")
                    points = 10 * self.level
                    self.score += points
                    print(f"   ⚡ Kekuatan {self.ghost_power} memberikan +{points} poin!")
                    print(f"   🚪 Pintu terbuka... Lanjut ke ruangan berikutnya!")
                    self.level += 1
                    time.sleep(3)
                else:
                    print(f"\n❌ SALAH! {explanation}")
                    self.lives -= 1
                    print(f"   💔 Hantu lain menyerangmu! Nyawa tersisa: {self.lives}")
                    if self.lives > 0:
                        print(f"   {self.ghost_emoji} Gunakan {self.ghost_power} untuk bertahan!")
                    time.sleep(3)
                    
            except KeyboardInterrupt:
                print("\n\n👋 Kamu melarikan diri dari rumah hantu!")
                return
        
        # Game Over
        self.clear_screen()
        print("\n" + "="*60)
        if self.level > self.max_level:
            print("🎉" * 30)
            self.print_slow("\n    ✨ SELAMAT! KAMU BERHASIL KELUAR! ✨")
            print()
            self.print_slow(f"    {self.ghost_emoji} {self.ghost_type} {self.player_name} menang!")
            print("\n🎉" * 30)
        else:
            print("💀" * 30)
            self.print_slow("\n      ⚰️  GAME OVER - TERJEBAK SELAMANYA  ⚰️")
            print()
            self.print_slow(f"    {self.ghost_emoji} {self.player_name} gagal melarikan diri...")
            print("\n💀" * 30)
        
        print("="*60)
        print(f"\n📊 Statistik Akhir:")
        print(f"   {self.ghost_emoji} Hantu: {self.ghost_type}")
        print(f"   🚪 Ruangan tercapai: {self.level - 1}/{self.max_level}")
        print(f"   ⭐ Total skor: {self.score}")
        print(f"   ⏰ Waktu: {datetime.now().strftime('%H:%M:%S')}")
        print("\n" + "="*60 + "\n")


# Jalankan game
if __name__ == "__main__":
    print("\n🌙 Memuat Rumah Hantu...")
    time.sleep(1)
    game = HauntedLogicGame()
    game.play()