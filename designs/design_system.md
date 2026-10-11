# Panorra Design System (Branch: `ui/components`)

Berdasarkan eksplorasi pada branch `ui/components` di repositori [GoThruMedia/panorra](https://github.com/GoThruMedia/panorra), aplikasi ini sedang bertransisi atau sudah menggunakan **NativeWind (Tailwind CSS untuk React Native)**.

Sistem desain diatur melalui CSS Variables di `src/global.css` dan di-sync ke TypeScript via token di `src/components/lib/design-tokens.ts`. Tailwind dikonfigurasi melalui `src/tailwind.config.js`. Konsep warnanya sangat mirip dengan _shadcn/ui_.

Berikut ekstraksi variabel Design System utama yang digunakan pada branch ini:

## 1. Typography (Font)
Aplikasi memetakan font di konfigurasi Tailwind (dan App.js) sebagai berikut:

* **Title/Heading (`font-title`)**: Memakai `font-semibold` (BlinkMacSystemFont-Semibold)
* **Body/Text (`font-body`)**: Memakai `font-regular` (BlinkMacSystemFont-Regular)
* **Special/Display (`font-fraunces`)**: Memakai custom font `Fraunces`

---

## 2. Terminology & Semantic Colors (Tailwind Classes)
Tema mendukung Dark Mode (`.dark:root`) dan Light Mode (`:root`). Warna diimplementasikan dengan utilities Tailwind seperti `bg-primary`, `text-muted-foreground`, dll.

**Brand Colors & Primary:**
* **Primary**: `hsl(var(--primary))` — **#5B4BFF** (Panorra Blue Violet). Digunakan untuk Accent utama. Warnanya konstan di light / dark mode.
* **Primary Foreground**: White (`#FFFFFF`). Terbaca sangat baik di atas background Primary (5.4:1 contrast ratio).

**Backgrounds / Surfaces:**
* **Background (`bg-background`)**:
  * Light: `#F7F8FB` (Abu-abu sangat terang)
  * Dark: `#0B1020` (Biru dongker sangat gelap)
* **Card (`bg-card`)**: 
  * Light: `#FFFFFF` 
  * Dark: `#12182A` (Surface default)
* **Popover (`bg-popover`)**:
  * Light: `#FFFFFF`
  * Dark: `#182036` (Surface untuk modals, dialogs)
* **Secondary (`bg-secondary`)**:
  * Light: `#F3F4F6` (Muted surface / hover box)
  * Dark: `#1D2740` (Surface hover)

**Text & Foregrounds:**
* **Foreground (`text-foreground`)**: Hitam/putih utama untuk teks (`#1F2937` di Light, `#F8FAFC` di Dark).
* **Muted Foreground (`text-muted-foreground`)**: Teks sekunder yang redup (`#6B7280` di Light, `#94A3B8` di Dark).

**Status Colors:**
* **Destructive / Error**: `#EF4444` (Light) / `#F87171` (Dark)
* **Accent (Selected/Pressed states)**: Merupakan variasi pudar dari warna primary. `#ECEBFF` (Light) / `#282452` (Dark)

**Charts / Data Viz Palette:**
Aplikasi juga mendefinisikan palet warna spesifik untuk Chart/Grafik:
* `--chart-1`: `#FF7ACB` (Magenta)
* `--chart-2`: `#A78BFF` (Violet)
* `--chart-3`: `#8B80FF` (Periwinkle)
* `--chart-4`: `#5B4BFF` (Primary)
* `--chart-5`: `#3B82F6` (Info Blue)

*Catatan: Terdapat juga varian `BRAND_GRADIENT` menggunakan urutan Magenta -> Violet -> Primary.*

---

## 3. Spacing, Gap, & Border Radius 
Konfigurasi Base Tailwind untuk struktur desain komponen:

* **Border Radius Khusus (`var(--radius)`)**: Default `0.75rem` (12px).
  * Tailwind Classes:
    * `rounded-lg` menggunakan *var(--radius)* (**12px**)
    * `rounded-md` menggunakan `calc(var(--radius) - 2px)` (**10px**)
    * `rounded-sm` menggunakan `calc(var(--radius) - 4px)` (**8px**)
    * Pada card, disebutkan untuk menggunakan `rounded-2xl` (**16px**)

* **Border Line (`border-width`)**:
  * Komponen ini mendukung ukuran khusus `border-hairline` untuk border tipis yang disesuaikan dengan NativeWind `hairlineWidth()`. Warna standard border diambil dari `var(--border)` (terang: `#E5E7EB`, gelap: `#283149`).
